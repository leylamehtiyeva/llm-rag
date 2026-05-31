from openai import OpenAI
from common.rag_helper import INSTRUCTIONS
from common.rag_pipeline import RAGPipeline
from common.config import OPENAI_API_KEY, MODEL_NAME
from openai import OpenAI
from vector_search_app.elastic_search_knn import ElasticVectorRetriever


from pathlib import Path


client = OpenAI(
    api_key=OPENAI_API_KEY,
)

DATA_PATH = Path(
    "vector_search_app/data/documents_with_embeddings.json"
)

retriever = ElasticVectorRetriever()

rag = RAGPipeline(
    retriever=retriever,
    llm_client=client,
    model_name=MODEL_NAME,
    instructions=INSTRUCTIONS,
)


QUESTION = "can I use ollama?"
answer = rag.ask(QUESTION)
print(answer)