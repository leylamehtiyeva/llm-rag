import json
from pathlib import Path

from openai import OpenAI
from tqdm.auto import tqdm

from common.config import (
    OPENAI_API_KEY,
    EMBEDDINGS_MODEL_NAME,
)


DATA_PATH = Path(
    "vector_search_app/data/embedded_documents.json"
)

OUTPUT_PATH = Path(
    "vector_search_app/data/documents_with_embeddings.json"
)

BATCH_SIZE = 100


client = OpenAI(
    api_key=OPENAI_API_KEY,
)


def load_documents(data_path: Path) -> list[dict]:
    return json.loads(
        data_path.read_text(encoding="utf-8")
    )


def generate_embeddings(
    texts: list[str],
    batch_size: int,
) -> list[list[float]]:
    all_embeddings = []

    for i in tqdm(
        range(0, len(texts), batch_size)
    ):
        batch = texts[i:i + batch_size]

        response = client.embeddings.create(
            model=EMBEDDINGS_MODEL_NAME,
            input=batch,
        )

        batch_embeddings = [
            item.embedding
            for item in response.data
        ]

        all_embeddings.extend(batch_embeddings)

    return all_embeddings


def main():
    documents = load_documents(DATA_PATH)

    texts = [
        doc["text"]
        for doc in documents
    ]

    embeddings = generate_embeddings(
        texts=texts,
        batch_size=BATCH_SIZE,
    )

    for doc, embedding in zip(documents, embeddings):
        doc["embedding"] = embedding

    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    OUTPUT_PATH.write_text(
        json.dumps(documents),
        encoding="utf-8",
    )

    print(
        f"Saved {len(documents)} documents with embeddings"
    )


if __name__ == "__main__":
    main()