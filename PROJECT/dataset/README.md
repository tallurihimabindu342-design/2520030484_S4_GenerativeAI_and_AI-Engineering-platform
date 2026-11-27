## 📊 Dataset – RouterBench

**Source:** [RouterBench – Hugging Face](https://huggingface.co/datasets/withmartian/routerbench)

RouterBench is an open-source research dataset designed to evaluate and compare multiple Large Language Models (LLMs) based on response quality and inference cost.

**Selected Dataset:** `routerbench_0shot.pkl`

**Dataset Details:**
- Total records: 36,497
- Total columns: 37
- Format: Pickle (`.pkl`)
- Size: Approximately 99.6 MB
- Includes prompts, model responses, performance scores, inference costs and oracle routing decisions.

**Why RouterBench?**

It provides research-based examples of how different LLMs perform on the same queries, making it useful for studying quality-cost trade-offs in intelligent model selection.

**How We Use It:**

We use RouterBench as our research-based question source. We generate fresh responses using our local Llama 1B and 3B models, evaluate their performance, and create project-specific routing labels to train our ML-based router.

**Note:** Existing RouterBench routing labels are not treated as direct ground truth for our local models.
