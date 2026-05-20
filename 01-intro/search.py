from typing import Any

from elasticsearch import Elasticsearch


class ElasticRetriever:
    def __init__(
        self,
        index_name: str = "course-faq",
        elastic_url: str = "http://localhost:9200",
    ):
        self.index_name = index_name
        self.es_client = Elasticsearch(elastic_url)

    def search(
        self,
        query: str,
        course_type: str = "llm-zoomcamp",
        top_n: int = 5,
    ) -> list[dict[str, Any]]:
        search_query = {
            "size": top_n,
            "query": {
                "bool": {
                    "must": {
                        "multi_match": {
                            "query": query,
                            "fields": ["question^3", "section", "answer"],
                        }
                    },
                    "filter": {
                        "term": {
                            "course": course_type,
                        }
                    },
                }
            },
        }

        response = self.es_client.search(
            index=self.index_name,
            body=search_query,
        )

        results = []

        for hit in response["hits"]["hits"]:
            doc = hit["_source"]

            results.append(
                {
                    "id": doc.get("id"),
                    "course": doc.get("course"),
                    "section": doc.get("section"),
                    "question": doc.get("question"),
                    "answer": doc.get("answer"),
                }
            )

        return results