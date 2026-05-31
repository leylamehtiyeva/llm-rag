import json
from pathlib import Path


DATA_PATH = Path("intro/data/documents.json")
OUTPUT_PATH = Path("vector_search_app/data/embedded_documents.json")


def load_documents(data_path: Path) -> list[dict]:
    return json.loads(data_path.read_text(encoding="utf-8"))


def build_text(doc: dict) -> str:
    return f"""
Question: {doc["question"]}
Answer: {doc["answer"]}
""".strip()


def prepare_documents_for_embeddings(documents: list[dict]) -> list[dict]:
    embedded_documents = []

    for doc in documents:
        text = build_text(doc)

        embedded_documents.append(
            {
                "id": doc["id"],
                "course": doc["course"],
                "section": doc["section"],
                "question": doc["question"],
                "answer": doc["answer"],
                "text": text,
            }
        )

    return embedded_documents


def save_documents(documents: list[dict], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    output_path.write_text(
        json.dumps(documents, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def main():
    documents = load_documents(DATA_PATH)
    embedded_documents = prepare_documents_for_embeddings(documents)
    save_documents(embedded_documents, OUTPUT_PATH)

    print(f"Loaded documents: {len(documents)}")
    print(f"Saved embedding-ready documents: {len(embedded_documents)}")
    print(f"Output path: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()