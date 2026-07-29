from openai import OpenAI
from metrics import RAGWithMetrics
from common.config import MODEL_NAME, OPENAI_API_KEY
from common.rag_helper import INSTRUCTIONS
from common.rag_pipeline import RAGPipeline
from vector_search_app.elastic_search_knn import ElasticVectorRetriever
from db_save import save_conversation


def create_assistant() -> RAGWithMetrics:
    client = OpenAI(api_key=OPENAI_API_KEY)
    retriever = ElasticVectorRetriever()

    return RAGWithMetrics(
        retriever=retriever,
        llm_client=client,
        model_name=MODEL_NAME,
        instructions=INSTRUCTIONS,
    )


def main() -> None:
    question = "When I can join the course?"

    assistant = create_assistant()
    answer = assistant.ask(question)

    print(answer)
    save_conversation(assistant.last_call, question, "llm-zoomcamp")


if __name__ == "__main__":
    main()
    