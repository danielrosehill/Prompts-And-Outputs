---
title: "Where will a Python script save its output by default"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


By default, the **CSV file** will be saved in the **current working directory (PWD)** from which you run the script. The **PWD** is typically the directory you are in when you execute the Python script in the terminal.

### **How to Control the CSV File Location**:
1. **Default Behavior**:
   - If you don't specify a path, Python will save the `dynamic_articles.csv` in the **same directory** where the script is being executed.
   - For example, if you run the script from `/home/daniel/scripts`, then the **CSV file** will be saved in `/home/daniel/scripts`.

2. **Specify a Custom Path** (Optional):
   - If you want to save the file in a **specific directory**, you can modify the file path:
   ```python
   with open("/home/daniel/reports/dynamic_articles.csv", "w", newline='', encoding='utf-8') as csv_file:
   ```
   - In this example, the CSV will be saved to the folder `/home/daniel/reports/`.

3. **Use Relative Paths**:
   - If you want to create a subdirectory relative to your script's location:
   ```python
   with open("./output/dynamic_articles.csv", "w", newline='', encoding='utf-8') as csv_file:
   ```
   - This will create the CSV inside an `output` folder (if it exists) in the current working directory.

### **How to Confirm the File Location**:
- If you're unsure where your script's **PWD** is, you can add a print statement in your script to confirm:
  ```python
  import os
  print("Current Working Directory:", os.getcwd())
  ```
  - This will print the **current working directory** before saving the file, helping you ensure it's being saved where you want it.

By default, your **dynamic_articles.csv** will be saved in the directory from which you **run the script**, unless you explicitly specify another location. You can customize the file path if you have a dedicated location where you want to store the output files.