from openai import OpenAI
from config import MODEL_NAME
from search import ElasticRetriever
from rag_helper import INSTRUCTIONS
from rag_pipeline import RAGPipeline
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url=os.getenv("OLLAMA_BASE_URL"),
    api_key=os.getenv("OLLAMA_API_KEY"),
)

retriever = ElasticRetriever()

rag = RAGPipeline(
    retriever=retriever,
    llm_client=client,
    model_name=MODEL_NAME,
    instructions=INSTRUCTIONS,
)


QUESTION = "hey,can i still join the course?"
answer = rag.ask(QUESTION)
print(answer)











