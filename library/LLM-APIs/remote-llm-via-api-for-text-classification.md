---
title: "Remote LLM via API for text classification"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Can you suggest how I could run this classification workload using a remote LLM via an API. I'd also like to get approximate costs. There are 1500 or so markdown files. And perhaps you can suggest the most appropriate LLM/API for this task.

# Output

To run the **text classification workload** on your 1500 markdown files using a **remote LLM API**, you can use services like **OpenAI**, **Hugging Face Inference API**, or **Cohere**. These APIs provide access to powerful models that can handle your classification task effectively.

Here’s how you can structure the process and get an **approximate cost estimate**:

---

### **1. Choosing the Most Appropriate API**

Here are a few API options and LLMs that are suitable for this task:

#### **a. OpenAI GPT-4 API**
- **Why**: OpenAI's GPT models are robust for understanding and categorizing text. GPT-4, in particular, is good at text classification and can process the markdown content efficiently.
- **Cost Estimate**:
  - GPT-4’s pricing is **$0.03 per 1K tokens for input** and **$0.06 per 1K tokens for output**.
  - Assuming the average markdown file is **1,000 words** (~1,500 tokens), the cost per file would be around **$0.045** (input + output).
  - For 1,500 files, the total cost would be approximately **$67.5** for GPT-4.

#### **b. Hugging Face Inference API (Falcon or LLaMA models)**
- **Why**: Hugging Face offers several models (e.g., **Falcon**, **LLaMA**) through their Inference API. These models are open-source and may offer good performance for text categorization tasks.
- **Cost Estimate**:
  - Hugging Face charges **$0.06 per second of compute time** for their inference API.
  - For text classification, if we assume each classification takes **2-5 seconds**, the cost per file would be **$0.12 to $0.30**.
  - For 1,500 files, the total cost would range from **$180 to $450**, depending on the model and time taken.

#### **c. Cohere API (Classify Endpoint)**
- **Why**: **Cohere** provides a dedicated **classification endpoint**, which is highly optimized for this kind of task. You can train a classifier on your own labels (e.g., "Tech Tutorial" or "Other").
- **Cost Estimate**:
  - Cohere's **classify API** charges around **$0.0025 per token**.
  - Assuming an average markdown file has 1,500 tokens, the cost per file would be around **$3.75**.
  - For 1,500 files, the total cost would be approximately **$5,625**, making it a more expensive option, but with specialized features.

---

### **2. Implementation Steps (for OpenAI GPT-4)**

Here’s how you can run the classification task using **OpenAI's GPT-4 API**. You can adapt this method for Hugging Face or Cohere as needed.

#### **a. Set Up OpenAI API**
First, install the **OpenAI Python SDK**:
```bash
pip install openai
```

#### **b. Write a Python Script for File Classification**
This script will loop through your markdown files, send them to the GPT-4 API, and move them based on the classification result.

```python
import openai
import os
import shutil

# Set up your OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Define file paths
source_folder = "/path/to/markdown/files"
tutorials_folder = "/path/to/tutorials"
others_folder = "/path/to/others"

# Ensure destination folders exist
os.makedirs(tutorials_folder, exist_ok=True)
os.makedirs(others_folder, exist_ok=True)

# Function to classify the content of each file
def classify_file(content):
    prompt = f"Classify the following markdown file as 'Tech Tutorial' or 'Other':\n\n{content}"
    
    response = openai.Completion.create(
        model="gpt-4",  # Use "gpt-4" or "gpt-3.5-turbo" for lower cost
        prompt=prompt,
        max_tokens=10  # Short response needed
    )
    
    classification = response.choices[0].text.strip()
    return classification

# Iterate over markdown files and classify
for file_name in os.listdir(source_folder):
    if file_name.endswith(".md"):  # Only process markdown files
        file_path = os.path.join(source_folder, file_name)
        
        # Read file content
        with open(file_path, "r") as file:
            content = file.read()

        # Classify the file
        classification = classify_file(content)
        print(f"File: {file_name}, Classification: {classification}")
        
        # Move the file based on classification
        if "Tech Tutorial" in classification:
            shutil.move(file_path, os.path.join(tutorials_folder, file_name))
        else:
            shutil.move(file_path, os.path.join(others_folder, file_name))
```

#### **c. Running the Script**
- Save the script and run it in your Python environment.
- The script will:
  - Loop through each markdown file.
  - Send the content to GPT-4 (or another LLM).
  - Based on the response, move the file to the appropriate subfolder.

---

### **3. Cost-Effective Alternatives**
If the cost of GPT-4 is too high for the entire set of markdown files, you can consider:
- **OpenAI GPT-3.5-Turbo**: It costs significantly less at **$0.0015 per 1K tokens (input)** and **$0.002 per 1K tokens (output)**. For 1,500 markdown files, this would cost approximately **$5-10** for the entire job.
- **Hugging Face with Smaller Models**: Using a smaller, less compute-heavy model on Hugging Face (like **DistilGPT-2** or **GPT-Neo**) can reduce the per-request cost.

---

### **4. Deployment Options**
- **Local Automation**: The Python script above automates classification by directly interfacing with the chosen API. You can run it locally.
- **Serverless Options (e.g., Pipedream)**: If you prefer a cloud-based workflow, services like **Pipedream** or **Zapier** can automate API calls and file handling, though they will have additional costs.

---

### **Summary**

- **Best API**: For text classification, OpenAI’s **GPT-4** or **GPT-3.5-Turbo** will likely be the most cost-effective, providing high accuracy for identifying technical setup guides.
- **Cost Estimates**:
  - **GPT-4**: Approximately **$67.5** for 1,500 markdown files.
  - **GPT-3.5-Turbo**: Much more affordable, around **$5-10**.
  - **Hugging Face**: Depending on the model, it could range from **$180 to $450**.
  - **Cohere Classify API**: Around **$5,625**, making it one of the most expensive options.

If you're looking for a balance of **cost-effectiveness** and **accuracy**, **GPT-3.5-Turbo** is a strong choice. Let me know if you need further assistance in setting up the process!