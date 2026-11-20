# Week 5 – Tokenization and Token Economics

## 1. Objective
To compare tokenization techniques for English, Telugu, and Hindi languages and understand LLM API cost calculation, budgeting, and context window usage.

## 2. Concepts Learned
- Tokenization
- BPE (GPT-2)
- WordPiece (Multilingual BERT)
- SentencePiece (mT5)
- Token count and token ratio
- Input and output token pricing
- API cost calculation
- Daily and monthly budgeting
- Context window calculation

## 3. Tokenization Experiment

Three tokenizer models were tested:
- BPE (GPT-2)
- WordPiece (Multilingual BERT)
- SentencePiece (mT5)

Languages tested:
- English
- Telugu
- Hindi

### Tokenization Results

| Language | Tokenizer | Word Count | Token Count | Token Ratio |
|---|---|---:|---:|---:|
| English | BPE (GPT-2) | 7 | 9 | 1.286 |
| English | WordPiece | 7 | 9 | 1.286 |
| English | SentencePiece | 7 | 11 | 1.571 |
| Telugu | BPE (GPT-2) | 7 | 214 | 30.571 |
| Telugu | WordPiece | 7 | 39 | 5.571 |
| Telugu | SentencePiece | 7 | 25 | 3.571 |
| Hindi | BPE (GPT-2) | 11 | 102 | 9.273 |
| Hindi | WordPiece | 11 | 25 | 2.273 |
| Hindi | SentencePiece | 11 | 27 | 2.455 |

### Observation
English sentences required fewer tokens compared to Telugu and Hindi with GPT-2. Telugu produced a particularly high token count with GPT-2 because of its limited multilingual representation.

## 4. API Cost Calculation

### Chatbot Usage
- Number of students: 1000
- Requests per student: 10
- Total daily requests: 10,000
- Input tokens per request: 1500
- Output tokens per request: 500

### Pricing Assumptions
- Input rate: $0.50 per million tokens
- Output rate: $2.00 per million tokens

### Cost Results

| Calculation | Result |
|---|---:|
| Daily Input Cost | $7.50 |
| Daily Output Cost | $10.00 |
| Total Daily Cost | $17.50 |
| Total Monthly Cost | $525.00 |

## 5. Context Window Calculation

| Parameter | Tokens |
|---|---:|
| Maximum Context Window | 128,000 |
| System Tokens | 2,000 |
| Conversation Tokens | 10,000 |
| Current User Input Tokens | 1,500 |
| Total Used Context | 13,500 |
| Remaining Context | 114,500 |

## 6. Generated Files
- `main.py` – Main experiment code
- `requirements.txt` – Required Python libraries
- `week5_token_comparison.csv` – Tokenization results

## 7. Conclusion
The experiment compared tokenization across English, Telugu, and Hindi using three tokenizer models. It also calculated daily and monthly API costs and remaining context window capacity. This experiment helped understand token efficiency, LLM budgeting, and context management.
