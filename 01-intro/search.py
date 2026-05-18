from elasticsearch import Elasticsearch


INDEX_NAME = "course-faq"

es_client = Elasticsearch("http://localhost:9200")

from typing import Any


def search_from_elastic(
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

    response = es_client.search(index=INDEX_NAME, body=search_query)

    results = []

    for hit in response["hits"]["hits"]:
        doc = hit["_source"]

        results.append(
            {
                # "score": hit["_score"],
                "id": doc.get("id"),
                "course": doc.get("course"),
                "section": doc.get("section"),
                "question": doc.get("question"),
                "answer": doc.get("answer"),
            }
        )

    return results