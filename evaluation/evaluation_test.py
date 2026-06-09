from pathlib import Path
from vector_search_app.generate_embeddings import load_documents
from common.config import MODEL_NAME, OPENAI_API_KEY
from openai import OpenAI
import json
from evaluation.shema import Questions
from evaluation.eval_utils import (gen_llm_questions, 
                                   calc_price, 
                                   gen_llm_questions_with_retry,
                                   RETRYABLE_ERRORS)
import pandas as pd
from tqdm.auto import tqdm




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
# print(doc["id"])
# print(doc["question"])
# print(doc["answer"])

#Step2 Generating questions with structured output

data_gen_instructions = """
You emulate a student who's taking our course.
Formulate 5 questions this student might ask based on a FAQ record. The record
should contain the answer to the questions, and the questions should be complete and not too short.
If possible, use as fewer words as possible from the record.

The output should resemble how people ask questions
on the internet. Not too formal, not too short, not too long.
""".strip()


openai_client = OpenAI()
user_prompt = json.dumps(doc)
answer = doc['answer']


#Lets wrap it into function
result, usage = gen_llm_questions(data_gen_instructions, user_prompt, 
                                  openai_client, Questions, MODEL_NAME)


# print(f"Generated questions: {result.questions}")
# print(f"Answer for these questions: {answer}")
# print(calc_price(usage))


#STEP3: Lets save our result into view below

records = []

for q in result.questions:
    records.append({
        "question": q,
        "document": doc["id"]
    })

print(records)



#STEP4: Lets generate questions for all answers
def generate_ground_truth(doc):
    user_prompt = json.dumps(doc)

    out, usage = gen_llm_questions_with_retry(
            data_gen_instructions, 
            user_prompt, 
            openai_client, 
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


ground_truth = []
usages = []

for doc in tqdm(documents[:5]):
    records, usage = generate_ground_truth(doc)
    ground_truth.extend(records)
    usages.append(usage)
    
