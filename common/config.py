from dotenv import load_dotenv
import os

load_dotenv()
OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY")
LLAMA_MODEL_NAME = os.getenv("MODEL_NAME")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")
EMBEDDINGS_MODEL_NAME = os.getenv("EMBEDDINGS_MODEL_NAME")