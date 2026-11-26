# Week 7 – Next-Token Probabilities and Logits

## 1. Objective

To inspect logits and next-token probabilities using the GPT-2 model with Hugging Face Transformers and identify the top five predicted tokens for different input prompts.

## 2. Concepts Learned

- Next-token prediction
- GPT-2 language model
- Hugging Face Transformers
- Tokenization and token IDs
- Logits
- Softmax function
- Probability distribution
- Top-k token selection

## 3. Experimental Configuration

| **Parameter** | **Value** |
| --- | --- |
| Model | GPT-2 |
| Framework | Hugging Face Transformers |
| Library | PyTorch |
| Total Prompts | 4 |
| Top-k Value | 5 |
| Total Predictions | 20 |

## 4. Next-Token Prediction Experiment

The input prompts were converted into token IDs and passed to the GPT-2 model. The model generated logits, which were converted into probabilities using the softmax function. The five tokens with the highest probabilities were selected for each prompt.

### Prompt 1: The cat is

| **Rank** | **Candidate Token** | **Token ID** | **Probability** |
| --- | --- | --- | --- |
| 1 | a | 257 | 0.064336 |
| 2 | still | 991 | 0.033349 |
| 3 | not | 407 | 0.029782 |
| 4 | now | 783 | 0.023039 |
| 5 | in | 287 | 0.020841 |

### Prompt 2: Artificial intelligence is

| **Rank** | **Candidate Token** | **Token ID** | **Probability** |
| --- | --- | --- | --- |
| 1 | a | 257 | 0.120448 |
| 2 | the | 262 | 0.052541 |
| 3 | not | 407 | 0.043239 |
| 4 | an | 281 | 0.030922 |
| 5 | now | 783 | 0.020620 |

### Prompt 3: India is a

| **Rank** | **Candidate Token** | **Token ID** | **Probability** |
| --- | --- | --- | --- |
| 1 | country | 1499 | 0.078008 |
| 2 | very | 845 | 0.030765 |
| 3 | nation | 3277 | 0.030166 |
| 4 | major | 1688 | 0.024701 |
| 5 | world | 995 | 0.019369 |

### Prompt 4: Machine learning helps

| **Rank** | **Candidate Token** | **Token ID** | **Probability** |
| --- | --- | --- | --- |
| 1 | us | 514 | 0.298620 |
| 2 | you | 345 | 0.126127 |
| 3 | to | 284 | 0.085233 |
| 4 | people | 661 | 0.027375 |
| 5 | the | 262 | 0.017392 |

## 5. Results and Observations

### Highest Probability Tokens

| **Prompt** | **Predicted Token** | **Probability (%)** |
| --- | --- | --- |
| The cat is | a | 6.4336% |
| Artificial intelligence is | a | 12.0448% |
| India is a | country | 7.8008% |
| Machine learning helps | us | 29.8620% |

### Observations

- GPT-2 predicts different next tokens based on the input context.
- The token "us" for the prompt "Machine learning helps" achieved the highest probability among all tested candidates.
- Softmax converts raw logits into probabilities between 0 and 1.
- Top-k selection identifies the five most probable next tokens.
- The probabilities of all vocabulary tokens sum to 1, but the top five probabilities alone do not necessarily sum to 1.

## 6. Generated Files

- `main.py` – Main next-token prediction program
- `requirements.txt` – Required Python libraries
- `week7_probability_results.csv` – Contains 20 next-token prediction records
- `output.md` – Experiment summary

## 7. Conclusion

The experiment successfully demonstrated next-token prediction using GPT-2 and Hugging Face Transformers. Logits were converted into probabilities using softmax, and the top five candidate tokens were identified for each input prompt. The results were saved in a CSV file, helping to understand how language models predict tokens based on the input context.
