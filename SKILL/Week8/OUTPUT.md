# Week 8 – Scaled Dot-Product Attention and Multi-Head Attention

## 1. Objective

To implement Scaled Dot-Product Attention and Multi-Head Attention from scratch using PyTorch and understand how attention weights and output representations are calculated.

## 2. Concepts Learned

- Attention mechanism
- Query, Key, and Value matrices
- Matrix multiplication
- Scaled Dot-Product Attention
- Softmax function
- Causal masking
- Multi-Head Attention
- Linear projection
- Tensor reshaping and transposition

## 3. Scaled Dot-Product Attention

Scaled Dot-Product Attention calculates the similarity between Query and Key matrices, scales the scores, applies softmax, and multiplies the resulting attention weights with the Value matrix.

### Experimental Configuration

| **Parameter** | **Value** |
| --- | --- |
| Batch Size | 1 |
| Sequence Length | 3 |
| Query Shape | [1, 3, 4] |
| Key Shape | [1, 3, 4] |
| Value Shape | [1, 3, 4] |
| Key Dimension | 4 |
| Scaling Factor | 2 |

### Attention Weights

| **Query** | **Key 1** | **Key 2** | **Key 3** |
| --- | --- | --- | --- |
| Query 1 | 0.5993 | 0.1230 | 0.2777 |
| Query 2 | 0.6748 | 0.2799 | 0.0453 |
| Query 3 | 0.1560 | 0.2224 | 0.6216 |

### Attention Output

| **Token** | **Dimension 1** | **Dimension 2** | **Dimension 3** | **Dimension 4** |
| --- | --- | --- | --- | --- |
| Token 1 | 0.1584 | -0.0585 | -0.5101 | -0.0795 |
| Token 2 | -0.0819 | -0.2993 | -0.7085 | -0.5652 |
| Token 3 | 0.0398 | 0.0107 | -0.4126 | 1.1796 |

**Output Shape:** [1, 3, 4]

## 4. Multi-Head Attention

Multi-Head Attention divides the input embeddings into multiple attention heads. Each head performs Scaled Dot-Product Attention independently, and their outputs are combined using a final linear projection.

### Experimental Configuration and Results

| **Parameter** | **Value** |
| --- | --- |
| Batch Size | 1 |
| Sequence Length | 3 |
| Embedding Dimension | 8 |
| Number of Heads | 2 |
| Dimension per Head | 4 |
| Input Shape | [1, 3, 8] |
| Attention Weights Shape | [1, 2, 3, 3] |
| Output Shape | [1, 3, 8] |

### Multi-Head Attention Output

```text
Token 1:
[-0.4926, -0.0318, 0.2735, 0.1753,
 -0.0680, 0.2593, 0.1891, -0.2646]

Token 2:
[-0.4559, 0.0233, 0.1900, 0.1605,
 -0.0565, 0.1918, 0.1885, -0.2357]

Token 3:
[-0.5777, 0.0802, 0.1703, 0.2695,
 0.0198, 0.2114, 0.0735, -0.1807]
```

## 5. Results and Observations

- Scaled Dot-Product Attention successfully generated attention weights and output tensors.
- The attention weights in each row sum to 1.
- Query 1 and Query 2 assigned the highest attention weight to Key 1.
- Query 3 assigned the highest attention weight to Key 3.
- Multi-Head Attention successfully processed the input using two attention heads.
- The final Multi-Head Attention output retained the original input shape.
- Numerical results may vary because randomly generated tensors are used.
- Optional causal masking was implemented but was not enabled during this experiment.

## 6. Generated Files

- `main.py` – Implementation of Scaled Dot-Product Attention and Multi-Head Attention
- `requirements.txt` – Required PyTorch library
- `output.md` – Experiment results and summary

## 7. Conclusion

The experiment successfully implemented Scaled Dot-Product Attention and Multi-Head Attention from scratch using PyTorch. Attention weights were calculated using matrix multiplication, scaling, and softmax. Multiple attention heads were combined to produce the final output. This experiment helped in understanding the attention mechanism used in Transformer architectures.
