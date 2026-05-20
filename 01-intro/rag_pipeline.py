from rag_helper import use_llm, build_prompt

class RAGPipeline:
    def __init__(
        self,
        retriever,
        llm_client,
        model_name: str,
        instructions: str,
        course_type: str = "llm-zoomcamp",
        top_n: int = 2,
    ):
        self.retriever = retriever
        self.llm_client = llm_client
        self.model_name = model_name
        self.instructions = instructions
        self.course_type = course_type
        self.top_n = top_n

    def ask(self, question: str) -> str:
        search_result = self.retriever.search(
            query=question,
            course_type=self.course_type,
            top_n=self.top_n,
        )

        user_prompt = build_prompt(question, search_result)

        return use_llm(
            self.instructions,
            user_prompt,
            client=self.llm_client,
            model=self.model_name,
        )