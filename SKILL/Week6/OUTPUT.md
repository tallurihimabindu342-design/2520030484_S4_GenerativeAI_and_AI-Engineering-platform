# Week 6 – Golden Question Set and Baseline Evaluation

## 1. Objective

To create a golden question set of 30 Generative AI questions, evaluate the Llama 3.2 model using Ollama, calculate keyword-based scores, and document the first baseline evaluation as Release v0.1.

## 2. Concepts Learned

- Golden Question Set
- Llama 3.2 and Ollama
- Expected answers and keywords
- LLM response generation
- Keyword-based evaluation
- Keyword coverage score
- PASS and REVIEW classification
- Baseline evaluation
- CSV result generation
- Release version v0.1

## 3. Golden Question Set

A total of 30 questions were prepared in `golden_set.json`.

Topics covered:

- Tokenization, BPE, WordPiece, and SentencePiece
- Token counts and API costs
- Context window and rate limits
- Autoregressive generation and next-token prediction
- Greedy decoding and sampling
- Temperature, top-k, and top-p
- Token IDs and embeddings
- Positional encoding and Transformers

Each question contains an ID, question, expected answer, keywords, and reference source.

## 4. Baseline Evaluation

The Llama 3.2 model was configured through Ollama for evaluating the golden question set.

### Evaluation Settings

| **Parameter** | **Value** |
| --- | --- |
| Model | Llama 3.2 |
| Platform | Ollama |
| Total Questions | 30 |
| Temperature | 0 |
| Evaluation Method | Keyword Matching |
| Passing Threshold | 60% |
| Release Version | v0.1 |

### Keyword Scoring

**Keyword Coverage (%) = (Matched Keywords / Total Expected Keywords) × 100**

- **PASS:** Score ≥ 60%
- **REVIEW:** Score < 60%
- **ERROR:** Model request failed

## 5. Baseline Results

The program is designed to generate `baseline_results.csv` containing the model responses, keyword scores, and evaluation status.

### Evaluation Summary

| **Metric** | **Result** |
| --- | --- |
| Total Questions | 30 |
| Successful Responses | Pending |
| Passed Questions | Pending |
| Questions for Review | Pending |
| Failed Requests | Pending |
| Average Keyword Coverage | Pending |
| Release Version | v0.1 |

### Observation

The keyword-based evaluation measures how closely the generated responses match the expected keywords. Questions scoring below 60% are marked for review. The final results will be recorded after execution.

## 6. Generated Files

- `golden_set.json` – Contains 30 questions, expected answers, keywords, and sources
- `main.py` – Main baseline evaluation program
- `requirements.txt` – Required Python libraries
- `baseline_results.csv` – Stores model responses and evaluation scores after execution
- `output.md` – Experiment summary

## 7. Conclusion

The Week 6 experiment establishes a golden question set and baseline evaluation process using Llama 3.2 and Ollama. The program evaluates generated responses using keyword matching, calculates scores, and classifies results as PASS or REVIEW. The evaluation results are saved in a CSV file for Release v0.1, providing a baseline for future model performance comparisons.
