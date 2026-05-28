import json
from pathlib import Path

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


DATA_PATH = Path(
    "vector_search_app/data/documents_with_embeddings.json"
)

INDEX_NAME = "course-faq-vector"


es_client = Elasticsearch(
    "http://localhost:9200"
)


index_settings = {
    "mappings": {
        "properties": {
            "id": {
                "type": "keyword"
            },
            "course": {
                "type": "keyword"
            },
            "section": {
                "type": "text"
            },
            "question": {
                "type": "text"
            },
            "answer": {
                "type": "text"
            },
            "text": {
                "type": "text"
            },
            "embedding": {
                "type": "dense_vector",
                "dims": 1536,
                "index": True,
                "similarity": "cosine",
            },
        }
    }
}


def load_documents(path: Path) -> list[dict]:
    return json.loads(
        path.read_text(encoding="utf-8")
    )


def create_index():
    if es_client.indices.exists(index=INDEX_NAME):
        es_client.indices.delete(index=INDEX_NAME)

    es_client.indices.create(
        index=INDEX_NAME,
        body=index_settings,
    )


def generate_actions(documents: list[dict]):
    for doc in documents:
        yield {
            "_index": INDEX_NAME,
            "_id": doc["id"],
            "_source": doc,
        }


def main():
    documents = load_documents(DATA_PATH)

    create_index()

    bulk(
        es_client,
        generate_actions(documents),
    )

    print(
        f"Indexed {len(documents)} documents into {INDEX_NAME}"
    )


if __name__ == "__main__":
    main()