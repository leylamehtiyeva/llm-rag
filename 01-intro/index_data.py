import json
from pathlib import Path

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


DATA_PATH = Path("01-intro/data/documents.json")
INDEX_NAME = "course-faq"

es_client = Elasticsearch("http://localhost:9200")


def index_documents():
    documents = json.loads(DATA_PATH.read_text(encoding="utf-8"))

    if es_client.indices.exists(index=INDEX_NAME):
        es_client.indices.delete(index=INDEX_NAME)

    es_client.indices.create(
        index=INDEX_NAME,
        mappings={
            "properties": {
                "id": {"type": "keyword"},
                "course": {"type": "keyword"},
                "section": {"type": "text"},
                "question": {"type": "text"},
                "answer": {"type": "text"},
            }
        },
    )

    actions = []

    for doc in documents:
        actions.append(
            {
                "_index": INDEX_NAME,
                "_id": doc["id"],
                "_source": doc,
            }
        )

    bulk(es_client, actions)

    es_client.indices.refresh(index=INDEX_NAME)

    print(es_client.count(index=INDEX_NAME))


if __name__ == "__main__":
    index_documents()