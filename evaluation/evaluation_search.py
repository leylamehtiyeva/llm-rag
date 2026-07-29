from pathlib import Path

import numpy as np
import pandas as pd
from tqdm import tqdm

from vector_search_app.elastic_search_knn import ElasticVectorRetriever


GROUND_TRUTH_PATH = Path("data/ground_truth_new.csv")
OUTPUT_PATH = Path("data/search_evaluation_metrics.csv")
MAX_TOP_N = 5

ground_truth_df = pd.read_csv(GROUND_TRUTH_PATH)
retriever = ElasticVectorRetriever()


def evaluate_search(
    df: pd.DataFrame,
    search_fn,
    top_n: int,
) -> pd.DataFrame:
    results = []

    for row in tqdm(
        df.reset_index().itertuples(),
        total=len(df),
        desc=f"Evaluating top-{top_n}",
    ):
        question_id = row.Index
        question = row.question
        expected_document_id = row.document

        answers = search_fn(question, top_n=top_n)

        for rank, answer in enumerate(answers, start=1):
            results.append(
                {
                    "question_id": question_id,
                    "question": question,
                    "expected_document_id": expected_document_id,
                    "retrieved_document_id": answer["id"],
                    "retrieved_text": answer["answer"],
                    "score": answer["score"],
                    "rank": rank,
                    "is_relevant": expected_document_id == answer["id"],
                }
            )

    return pd.DataFrame(results)


def filter_top_k(results_df: pd.DataFrame, k: int) -> pd.DataFrame:
    return results_df[results_df["rank"] <= k]


def calculate_hit_rate_at_k(results_df: pd.DataFrame) -> float:
    return (
        results_df
        .groupby("question_id")["is_relevant"]
        .any()
        .mean()
    )


def calculate_mrr_at_k(results_df: pd.DataFrame) -> float:
    reciprocal_rank = np.where(
        results_df["is_relevant"],
        1 / results_df["rank"],
        0,
    )

    return (
        results_df
        .assign(reciprocal_rank=reciprocal_rank)
        .groupby("question_id")["reciprocal_rank"]
        .max()
        .mean()
    )


bm25_results_df = evaluate_search(
    df=ground_truth_df,
    search_fn=retriever.search_bm25,
    top_n=MAX_TOP_N,
)

vector_results_df = evaluate_search(
    df=ground_truth_df,
    search_fn=retriever.search,
    top_n=MAX_TOP_N,
)


metrics_df = pd.DataFrame(
    [
        {
            "method": "BM25",
            "hit_rate_1": calculate_hit_rate_at_k(filter_top_k(bm25_results_df, 1)),
            "hit_rate_3": calculate_hit_rate_at_k(filter_top_k(bm25_results_df, 3)),
            "hit_rate_5": calculate_hit_rate_at_k(filter_top_k(bm25_results_df, 5)),
            "mrr_5": calculate_mrr_at_k(filter_top_k(bm25_results_df, 5)),
        },
        {
            "method": "Vector Search",
            "hit_rate_1": calculate_hit_rate_at_k(filter_top_k(vector_results_df, 1)),
            "hit_rate_3": calculate_hit_rate_at_k(filter_top_k(vector_results_df, 3)),
            "hit_rate_5": calculate_hit_rate_at_k(filter_top_k(vector_results_df, 5)),
            "mrr_5": calculate_mrr_at_k(filter_top_k(vector_results_df, 5)),
        },
    ]
)

metrics_df.to_csv(OUTPUT_PATH, index=False)

print(f"Metrics saved to: {OUTPUT_PATH}")
print(metrics_df)



# Params boost experiment

# question_boost_params = [0.5, 1.0, 3.0, 5.0, 10.0]

# results = []

# for question_boost in question_boost_params:

#     bm25_params_results_df = evaluate_search(
#         df=ground_truth_df,
#         search_fn=lambda query, top_n, question_boost=question_boost:
#             retriever.search_bm25_param(
#                 query=query,
#                 top_n=top_n,
#                 question_boost=question_boost,
#             ),
#         top_n=MAX_TOP_N,
#     )

#     results.append(
#         {
#             "question_boost": question_boost,
#             "hit_rate_1": calculate_hit_rate_at_k(
#                 filter_top_k(bm25_params_results_df, 1)
#             ),
#             "hit_rate_3": calculate_hit_rate_at_k(
#                 filter_top_k(bm25_params_results_df, 3)
#             ),
#             "hit_rate_5": calculate_hit_rate_at_k(
#                 filter_top_k(bm25_params_results_df, 5)
#             ),
#             "mrr_5": calculate_mrr_at_k(
#                 filter_top_k(bm25_params_results_df, 5)
#             ),
#         }
#     )

# metrics_df = pd.DataFrame(results)

# print(metrics_df)


# Because of grid search we understand that the best question_boost params is 1.0
# Lets compare it with Vector search again 
