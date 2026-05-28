from typing import Any

from elasticsearch import Elasticsearch
from openai import OpenAI

from common.config import (
    OPENAI_API_KEY,
    EMBEDDINGS_MODEL_NAME,
)


class ElasticVectorRetriever:
    def __init__(
        self,
        index_name: str = "course-faq-vector",
        elastic_url: str = "http://localhost:9200",
    ):
        self.index_name = index_name
        self.es_client = Elasticsearch(elastic_url)

        self.openai_client = OpenAI(
            api_key=OPENAI_API_KEY,
        )

    def embed_query(self, query: str) -> list[float]:
        response = self.openai_client.embeddings.create(
            model=EMBEDDINGS_MODEL_NAME,
            input=query,
        )

        return response.data[0].embedding

    def search(
        self,
        query: str,
        course_type: str = "llm-zoomcamp",
        top_n: int = 5,
    ) -> list[dict[str, Any]]:
        query_vector = self.embed_query(query)

        response = self.es_client.search(
            index=self.index_name,
            knn={
                "field": "embedding",
                "query_vector": query_vector,
                "k": top_n,
                "num_candidates": 100,
                "filter": {
                    "term": {
                        "course": course_type,
                    }
                },
            },
            source=[
                "id",
                "course",
                "section",
                "question",
                "answer",
                "text",
            ],
        )

        results = []

        for hit in response["hits"]["hits"]:
            doc = hit["_source"]

            results.append(
                {
                    "score": hit["_score"],
                    "id": doc.get("id"),
                    "course": doc.get("course"),
                    "section": doc.get("section"),
                    "question": doc.get("question"),
                    "answer": doc.get("answer"),
                    "text": doc.get("text"),
                }
            )

        return results