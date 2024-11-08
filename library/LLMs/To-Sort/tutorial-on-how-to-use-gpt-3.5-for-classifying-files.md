---
title: "Tutorial on how to use GPT 3.5 for classifying files"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Let's go for 3.5 turbo. Could you give me a tutorial on how to set up the script. And a way to run it over 100 files to make sure the accuracy is good before doing the rest

# Output

To set up and run your text classification task using **OpenAI's GPT-3.5 Turbo API**, here’s a detailed tutorial. This will guide you through running the script over 100 markdown files first to test accuracy before scaling up to the full 1,500 files.

---

### **Step 1: Set Up Your Python Environment**

If you haven’t already, you’ll need Python and the required libraries installed.

#### **Install Python**
If Python is not installed, download and install it from [python.org](https://www.python.org/downloads/).

#### **Install OpenAI SDK**
OpenAI provides an SDK to interact with its APIs. Install it using pip:

```bash
pip install openai
```

#### **Set Up Your API Key**
Get your **OpenAI API key** from [OpenAI's platform](https://platform.openai.com/account/api-keys). Once you have it, you can add it to your environment variables or directly in the script.

---

### **Step 2: Write the Python Script**

Here’s a Python script that will iterate through the first 100 markdown files, send their content to GPT-3.5 Turbo, and classify them as "Tech Tutorial" or "Other". It will move the files to respective folders based on the classification.

#### **Script:**
```python
import openai
import os
import shutil

# Set up your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Define file paths
source_folder = "/path/to/your/markdown/folder"
tutorials_folder = "/path/to/your/subfolder/for/tutorials"
others_folder = "/path/to/your/subfolder/for/others"

# Ensure destination folders exist
os.makedirs(tutorials_folder, exist_ok=True)
os.makedirs(others_folder, exist_ok=True)

# Function to classify the content of each file
def classify_file(content):
    prompt = f"Classify the following markdown file as 'Tech Tutorial' or 'Other':\n\n{content}"
    
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # Using GPT-3.5-Turbo model
            prompt=prompt,
            max_tokens=10  # Short response needed
        )
        classification = response.choices[0].text.strip()
        return classification
    except Exception as e:
        print(f"Error processing file: {e}")
        return None

# Iterate over markdown files and classify (limiting to first 100 files for testing)
file_count = 0
for file_name in os.listdir(source_folder):
    if file_count >= 100:
        break

    if file_name.endswith(".md"):  # Only process markdown files
        file_path = os.path.join(source_folder, file_name)
        
        # Read file content
        with open(file_path, "r") as file:
            content = file.read()

        # Classify the file
        classification = classify_file(content)
        if classification:
            print(f"File: {file_name}, Classification: {classification}")
            
            # Move the file based on classification
            if "Tech Tutorial" in classification:
                shutil.move(file_path, os.path.join(tutorials_folder, file_name))
                print(f"Moved {file_name} to Tech Tutorials folder.")
            else:
                shutil.move(file_path, os.path.join(others_folder, file_name))
                print(f"Moved {file_name} to Others folder.")
                
        file_count += 1
```

---

### **Step 3: Running the Script**

1. **Save the script** as a `.py` file, such as `classify_markdown_files.py`.
2. **Update paths**: Replace `"/path/to/your/markdown/folder"`, `"/path/to/your/subfolder/for/tutorials"`, and `"/path/to/your/subfolder/for/others"` with your actual file paths.
3. **Set your API key**: Replace `YOUR_OPENAI_API_KEY` with your actual OpenAI API key.
4. **Run the script**:

```bash
python classify_markdown_files.py
```

This script will classify the first 100 markdown files and move them to the appropriate folders based on the GPT-3.5 Turbo response.

---

### **Step 4: Test Accuracy**

After the script processes 100 files:
1. **Review the Results**: Check the `tutorials_folder` and `others_folder` to see how well GPT-3.5 Turbo has classified the files. If most technical setup guides end up in the **tutorials** folder, the model is working well.
2. **Refine the Prompt**: If needed, you can tweak the prompt in the script to make it more specific. For example, you could ask the model to look for specific keywords or give examples of technical setup guides:
   ```python
   prompt = ("You are an expert in classifying markdown files. A 'Tech Tutorial' includes step-by-step instructions for setting up or configuring software or hardware. "
             "All other files should be classified as 'Other'. Here is the content of the file:\n\n{content}")
   ```

---

### **Step 5: Run on All Files**

Once you are satisfied with the accuracy:
1. **Remove the 100-file limit**:
   ```python
   if file_count >= 100:
       break
   ```
   Delete this line from the script to allow it to run on all files.
   
2. **Run the script again** to classify all 1,500 markdown files.

---

### **Cost Estimate for GPT-3.5 Turbo**

Here’s a rough cost estimate based on the pricing and token usage:

- **Tokens per file**: Each markdown file is estimated to be around **1,500 tokens** (input).
- **Cost per 1K tokens**: **$0.0015 for input** and **$0.002 for output**.
- **Cost per file**: 
  - For **1,500 tokens**, input cost is **$0.00225** and output cost (minimal) is **$0.002**.
  - Total cost per file: **~$0.00425**.
  
- **For 100 files**: 
  - **100 files** x **$0.00425** = **$0.425**.
  
- **For 1,500 files**:
  - **1,500 files** x **$0.00425** = **~$6.38** total cost for the entire job.

---

### **Summary**

- Use **GPT-3.5 Turbo** via OpenAI API to classify your markdown files.
- Test accuracy by running the script on 100 files and adjusting the prompt if necessary.
- Approximate cost for 1,500 markdown files is around **$6.38** using GPT-3.5 Turbo, making it a cost-effective solution.

Let me know if you need further assistance or adjustments to the script!