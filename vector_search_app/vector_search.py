import json
from pathlib import Path

import numpy as np
from openai import OpenAI

from common.config import (
    OPENAI_API_KEY,
    EMBEDDINGS_MODEL_NAME,
)


DATA_PATH = Path(
    "vector_search_app/data/documents_with_embeddings.json"
)


class VectorSearchEngine:
    def __init__(self, data_path: Path):
        self.client = OpenAI(
            api_key=OPENAI_API_KEY,
        )

        self.documents = json.loads(
            data_path.read_text(encoding="utf-8")
        )

        embeddings = [
            doc["embedding"]
            for doc in self.documents
        ]

        self.X = np.array(embeddings)

        print("Matrix shape:", self.X.shape)

    def search(
        self,
        query: str,
        top_k: int = 5,
    ):
        response = self.client.embeddings.create(
            model=EMBEDDINGS_MODEL_NAME,
            input=query,
        )

        query_vector = np.array(
            response.data[0].embedding
        )

        print(
            "Query vector shape:",
            query_vector.shape,
        )

        scores = self.X.dot(query_vector) / (
            np.linalg.norm(self.X, axis=1)
            * np.linalg.norm(query_vector)
        )

        top_indices = np.argsort(scores)[-top_k:][::-1]

        for idx in top_indices:
            print("=" * 80)
            print("Score:", scores[idx])
            print(
                "Question:",
                self.documents[idx]["question"],
            )
            print(
                "Answer:",
                self.documents[idx]["answer"],
            )

