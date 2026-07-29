import time

from dataclasses import dataclass, field
from datetime import datetime

from common.config import MODEL_NAME
from common.rag_pipeline import RAGPipeline

@dataclass
class LLMCallRecord:
    model: str
    prompt: str
    instructions: str
    answer: str
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
    response_time: float
    cost: float
    timestamp: datetime = field(default_factory=datetime.now)
    
def calculate_cost(model, usage):
    cost = 0
    if model == MODEL_NAME:
        cost = (usage.input_tokens * 0.15 + usage.output_tokens * 0.60) / 1_000_000
    return cost


class RAGWithMetrics(RAGPipeline):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_call: LLMCallRecord | None = None

    def llm(self, user_prompt: str) -> str:
        start_time = time.time()

        response = self.llm_client.responses.create(
            model=self.model_name,
            input=[
                {"role": "developer", "content": self.instructions},
                {"role": "user", "content": user_prompt},
            ],
        )

        response_time = time.time() - start_time
        usage = response.usage

        self.last_call = LLMCallRecord(
            model=self.model_name,
            prompt=user_prompt,
            instructions=self.instructions,
            answer=response.output_text,
            prompt_tokens=usage.input_tokens,
            completion_tokens=usage.output_tokens,
            total_tokens=usage.total_tokens,
            response_time=response_time,
            cost=calculate_cost(self.model_name, usage),
        )

        return response.output_text