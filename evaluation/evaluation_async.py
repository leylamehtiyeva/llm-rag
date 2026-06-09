from pathlib import Path
from vector_search_app.generate_embeddings import load_documents
from common.config import MODEL_NAME, OPENAI_API_KEY
from openai import OpenAI
import json
from evaluation.shema import Questions
import pandas as pd
from tqdm.auto import tqdm
import asyncio
from openai import AsyncOpenAI

from evaluation.eval_utils import (gen_llm_questions_async, 
                                   calc_price, 
                                   gen_llm_questions_with_retry_async,
                                   RETRYABLE_ERRORS)



DATA_PATH = Path(
    "vector_search_app/data/embedded_documents.json"
)

documents = load_documents(DATA_PATH)


#Lets filter our documents stor only for llm-zoomcamp course for simplicity
documents_llm = []

for doc in documents:
    if doc["course"] == "llm-zoomcamp":
        documents_llm.append(doc)

# print(len(documents_llm))

documents = documents_llm
doc = documents[0]

data_gen_instructions = """
You emulate a student who's taking our course.
Formulate 5 questions this student might ask based on a FAQ record. The record
should contain the answer to the questions, and the questions should be complete and not too short.
If possible, use as fewer words as possible from the record.

The output should resemble how people ask questions
on the internet. Not too formal, not too short, not too long.
""".strip()

#Instead of standart OpenAI we use async method AsyncOpenAI

async_openai_client = AsyncOpenAI()
user_prompt = json.dumps(doc)
answer = doc['answer']


#STEP4: Lets generate questions for all answers
async def generate_ground_truth(doc):
    user_prompt = json.dumps(doc)

    out, usage = await gen_llm_questions_with_retry_async(
            data_gen_instructions, 
            user_prompt, 
            async_openai_client, 
            Questions, 
            MODEL_NAME,
            RETRYABLE_ERRORS
    )

    results = []

    for q in out.questions:
        results.append({
            "question": q,
            "document": doc["id"]
        })

    return results, usage


MAX_CONCURRENT_REQUESTS = 3
semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)
async def generate_ground_truth_limited(doc):
    async with semaphore:
        return await generate_ground_truth(doc)


async def main():
    tasks = [
        generate_ground_truth_limited(doc)
        for doc in documents[:5]
    ]

    results = await asyncio.gather(*tasks)

    ground_truth = []
    usages = []

    for records, usage in results:
        ground_truth.extend(records)
        usages.append(usage)

    return ground_truth, usages


if __name__ == "__main__":
    ground_truth, usages = asyncio.run(main())
    
