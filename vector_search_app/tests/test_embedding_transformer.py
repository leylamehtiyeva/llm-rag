from openai import OpenAI
import numpy as np
from common.config import OPENAI_API_KEY, EMBEDDINGS_MODEL_NAME

# client = OpenAI(api_key=OPENAI_API_KEY)

# texts = [
#     "I just found out about the program, can I still enroll?",
#     "Can I still join the course after the start date?",
#     "You don't need to register. You're accepted. You can also just start learning and submitting homework without registering.",
# ]

# response = client.embeddings.create(
#     model=EMBEDDINGS_MODEL_NAME,
#     input=texts,
# )

# embeddings = [item.embedding for item in response.data]

# embedding1 = np.array(embeddings[0])
# embedding2 = np.array(embeddings[1])
# embedding3 = np.array(embeddings[2])

# def cosine_similarity(v1, v2):
#     return np.dot(v1, v2) / (
#         np.linalg.norm(v1) * np.linalg.norm(v2)
#     )


# similarity_1_3 = cosine_similarity(embedding1, embedding3)
# similarity_2_3 = cosine_similarity(embedding2, embedding3)
# similarity_1_2 = cosine_similarity(embedding1, embedding2)


# print("Similarity (1, 3):", similarity_1_3)
# print("Similarity (2, 3):", similarity_2_3)
# print("Similarity (1, 2):", similarity_1_2)


import json
from pathlib import Path


DATA_PATH = Path(
    "vector_search_app/data/documents_with_embeddings.json"
)

documents = json.loads(
    DATA_PATH.read_text(encoding="utf-8")
)

first_embedding = documents[0]["embedding"]

print(len(first_embedding))
print(documents[0].keys())

