import logging
from openai import  (APITimeoutError,
                     APIConnectionError,
                     RateLimitError)
import random
import time
import asyncio




logger = logging.getLogger(__name__)

RETRYABLE_ERRORS = (
    APITimeoutError,
    APIConnectionError,
    RateLimitError,
)

def gen_llm_questions(instructions, user_prompt, client, questions, MODEL_NAME):
    messages = [
    {"role": "developer", "content": instructions},
    {"role": "user", "content": user_prompt}
    ]

    response = client.responses.parse(
        model=MODEL_NAME,
        input=messages,
        text_format=questions
    )
    
    return response.output_parsed, response.usage


def gen_llm_questions_with_retry(instructions, 
                                 user_prompt, 
                                 client, 
                                 questions, 
                                 MODEL_NAME,
                                 RETRYABLE_ERRORS,
                                 max_retries = 3,
                                 base_delay = 1.0):
    for attempt in range(max_retries):
        try:
            return gen_llm_questions(instructions, 
                                     user_prompt, 
                                     client, 
                                     questions, 
                                     MODEL_NAME)
        except RETRYABLE_ERRORS as error:
            is_last_attempt = attempt == max_retries - 1
            if is_last_attempt:
                logger.error(
                    f"LLM call failed after {max_retries} attempts. "
                    f"Error: {error}"
                    )
                raise 
            delay = base_delay * (2 ** attempt)
            jitter = random.uniform(0, 0.5)
            sleep_time = delay + jitter

            logger.warning(
                    f"LLM call failed. "
                    f"Retrying in {sleep_time:.2f}s. "
                    f"Attempt {attempt + 1}/{max_retries}. "
                    f"Error: {error}"
                )

            time.sleep(sleep_time)
    


def calc_price(usage):
    input_price_per_million = 0.75
    output_price_per_million = 4.50

    input_cost = (usage.input_tokens / 1_000_000) * input_price_per_million
    output_cost = (usage.output_tokens / 1_000_000) * output_price_per_million
    total_cost = input_cost + output_cost

    return {
        "input_cost": input_cost,
        "output_cost": output_cost,
        "total_cost": total_cost,
    }
    
    
    
#--------ASYNC Versions------------

async def gen_llm_questions_async(instructions, user_prompt, client, questions, MODEL_NAME):
    messages = [
    {"role": "developer", "content": instructions},
    {"role": "user", "content": user_prompt}
    ]

    response = await client.responses.parse(
        model=MODEL_NAME,
        input=messages,
        text_format=questions
    )
    
    return response.output_parsed, response.usage
    

    
async def gen_llm_questions_with_retry_async(instructions, 
                                 user_prompt, 
                                 client, 
                                 questions, 
                                 MODEL_NAME,
                                 RETRYABLE_ERRORS,
                                 max_retries = 3,
                                 base_delay = 1.0):
    for attempt in range(max_retries):
        try:
            return await gen_llm_questions_async(instructions, 
                                     user_prompt, 
                                     client, 
                                     questions, 
                                     MODEL_NAME)
        except RETRYABLE_ERRORS as error:
            is_last_attempt = attempt == max_retries - 1
            if is_last_attempt:
                logger.error(
                    f"LLM call failed after {max_retries} attempts. "
                    f"Error: {error}"
                    )
                raise 
            delay = base_delay * (2 ** attempt)
            jitter = random.uniform(0, 0.5)
            sleep_time = delay + jitter

            logger.warning(
                    f"LLM call failed. "
                    f"Retrying in {sleep_time:.2f}s. "
                    f"Attempt {attempt + 1}/{max_retries}. "
                    f"Error: {error}"
                )

            await asyncio.sleep(sleep_time)
    