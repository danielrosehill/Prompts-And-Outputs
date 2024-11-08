---
title: "How to run GGUF for text classification"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

ok so i'm using lm studio. how do i get gguf to identify all the tech tutorials in my md repo?

# Output

To get **GGUF models** in **LM Studio** to identify all the tech tutorials in your markdown (MD) repository, you will need to follow these steps:

### **1. Load the LLaMa-2-7B-GGUF Model in LM Studio**

- Start by launching **LM Studio** and selecting the **LLaMa-2-7B-GGUF** model from the list.
- Download and configure the model if you haven’t done so already.

### **2. Prepare Your Markdown Repository for Input**
- Ensure your markdown files are accessible within your local system. Organize them in a folder structure or a file list so that you can easily load them into LM Studio for categorization.
  
### **3. Write a Prompt for Categorization**

Since LLaMa models rely on **text-based prompts**, you’ll need to construct a prompt that instructs the model to identify and categorize markdown files as technical tutorials or otherwise.

Here’s an example of a categorization prompt:
```plaintext
You are an expert at reading and categorizing documents. You will now be given a list of markdown files. Your task is to identify which of these files are technical setup guides or tutorials. If the document is a tutorial, classify it as 'Tech Tutorial'; if not, classify it as 'Other'. Begin by analyzing the following document:
```

For each markdown file, append its content after the prompt and feed it into the model.

### **4. Load the Markdown Files and Automate Input**

You can automate the process of reading markdown files from your repository and feeding them into LM Studio by:

- Writing a **Python script** (or another programming language) to batch-load the files.
- For each file, pass the content into the model’s prompt and store the output (either as "Tech Tutorial" or "Other").
  
Example Python script to iterate through the markdown files:
```python
import os
import openai  # if you're using the OpenAI API, adjust for LM Studio integration

# Define the prompt for categorization
categorization_prompt = "You are an expert at categorizing markdown files as technical tutorials or other. Here's the file content: \n\n"

# Path to your markdown repository
md_repo_path = "/path/to/your/markdown/repo"

# Iterate through the markdown files in the repository
for file_name in os.listdir(md_repo_path):
    if file_name.endswith(".md"):
        with open(os.path.join(md_repo_path, file_name), "r") as file:
            md_content = file.read()
            # Combine the prompt with the markdown file's content
            input_text = categorization_prompt + md_content
            
            # Use LM Studio's API for text completion (adjust this part for LM Studio's interaction method)
            # For instance, you could automate using HTTP requests, depending on your setup
            # output = call_lm_studio_api(input_text)

            # Analyze and store the result
            print(f"File: {file_name} - Categorization: {output}")
```

### **5. Review the Output**

Once the model processes the files, it should provide output for each one, either marking them as **"Tech Tutorial"** or **"Other"**. You can store this categorization in a CSV file or another format for later review.

### **6. Post-Processing and Manual Verification**
- After LM Studio provides its results, you can review and manually verify the categorization, especially if there are files that the model wasn’t able to classify properly.

---

### **Additional Tips**:
- **Tuning the Prompt**: If the model struggles with certain documents, you can adjust the prompt to include more specific instructions or provide examples to guide its classification logic.
- **Batch Processing**: Depending on LM Studio's capabilities, you may be able to send multiple documents in one request or loop through them using scripts.

Let me know if you need further help on automating the process in **LM Studio**!