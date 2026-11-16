# Week 4 – Tokenizer Comparison Lab

## 1. AIM
To understand and compare BPE, WordPiece, and SentencePiece tokenization approaches using English, Telugu, and Hindi text.

## 2. OBJECTIVE
To observe how different tokenizers divide sentences into tokens and compare their token counts and token ratios.

## 3. CONCEPTS LEARNED
- Tokenization
- Byte Pair Encoding (BPE)
- WordPiece
- SentencePiece
- Subword tokenization
- Token count
- Token ratio
- Multilingual tokenization

## 4. FILES USED

| File | Description |
|---|---|
| main.py | Python program for tokenizer comparison |
| requirements.txt | Required Python libraries |
| tokenizer_results.csv | Stores tokenization comparison results |
| OUTPUT.md | Experiment documentation |

## 5. PROCEDURE
1. Installed the required Python libraries.
2. Loaded BPE, WordPiece, and SentencePiece tokenizers.
3. Provided English, Telugu, and Hindi sentences as input.
4. Tokenized each sentence using all three tokenizers.
5. Calculated word count, token count, and token ratio.
6. Displayed the comparison results in the terminal.
7. Exported the results into tokenizer_results.csv.

## 6. RESULTS

| Language | Tokenizer | Word Count | Token Count | Token Ratio |
|---|---|---:|---:|---:|
| English | BPE (GPT-2) | 7 | 9 | 1.286 |
| English | WordPiece | 7 | 11 | 1.571 |
| English | SentencePiece | 7 | 11 | 1.571 |
| Telugu | BPE (GPT-2) | 7 | 148 | 21.143 |
| Telugu | WordPiece | 7 | 22 | 3.143 |
| Telugu | SentencePiece | 7 | 18 | 2.571 |
| Hindi | BPE (GPT-2) | 10 | 96 | 9.6 |
| Hindi | WordPiece | 10 | 22 | 2.2 |
| Hindi | SentencePiece | 10 | 19 | 1.9 |

## 7. OBSERVATION
- BPE produced fewer tokens for English compared to the other two tokenizers.
- BPE produced significantly more tokens for Telugu and Hindi.
- SentencePiece produced the lowest token counts for Telugu and Hindi.
- Token counts differ depending on the tokenizer and language.

## 8. CONCLUSION
The experiment compared three tokenizers across English, Telugu, and Hindi. It showed that tokenization differs by language, with SentencePiece producing fewer tokens for Telugu and Hindi.

## 9. OUTPUT
The experiment completed successfully, and the comparison results were saved in tokenizer_results.csv.
