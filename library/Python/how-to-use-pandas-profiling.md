---
title: "How to use pandas profiling"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Certainly! **Pandas Profiling** is a fantastic Python library that automatically generates an in-depth exploratory data analysis (EDA) report for any dataset in a `pandas` DataFrame. It’s a time-saving tool for quickly getting an overview of the structure, quality, and essential statistics of your data.

Below, I will guide you through installing and using Pandas Profiling, along with some examples.

### **Step 1: Install Pandas Profiling**
To install Pandas Profiling, you can use `pip`. Run the following command in your terminal:

```sh
pip install pandas-profiling
```

Note: Sometimes, the library name changes to `pandas-profiling` or `ydata-profiling`. You can use:
```sh
pip install ydata-profiling
```
This is due to its recent rebranding, and it can sometimes be better supported with the `ydata-profiling` version.

### **Step 2: Import Pandas Profiling**
Once the library is installed, you can import it into your Python script or Jupyter notebook:

```python
import pandas as pd
from ydata_profiling import ProfileReport
```

### **Step 3: Load a Dataset**
First, you need a dataset to analyze. Let's assume you have a CSV file called `sales_data.csv`:

```python
# Load the dataset using pandas
df = pd.read_csv('sales_data.csv')
```

### **Step 4: Generate a Profile Report**
You can now use Pandas Profiling to generate a detailed report of the data:

```python
# Create a profile report of the dataset
profile = ProfileReport(df, title='Sales Data Report', explorative=True)
```

### **Step 5: Export or View the Report**
You can either display the report within a Jupyter notebook or export it as an HTML file to view in your browser:

#### **Option 1: Display in Jupyter Notebook**
If you are using Jupyter Notebook, you can display the report directly:

```python
profile.to_notebook_iframe()
```

This will embed the profiling report within the notebook cell, making it easy to explore.

#### **Option 2: Save as an HTML File**
To save the report as an HTML file for future use or sharing:

```python
profile.to_file("sales_data_report.html")
```

This command will save the profiling report as `sales_data_report.html`, which you can open in a browser.

### **Key Features of the Report**
The generated report includes several insightful sections, such as:

1. **Overview**:
   - Number of variables (columns) and observations (rows).
   - Data types used (numerical, categorical, date, etc.).
   - Missing values and duplicates.

2. **Variables**:
   - Details about each variable, such as:
     - **Missing Values**: How many null values are present.
     - **Unique Values**: Number of unique entries.
     - **Descriptive Statistics**: Mean, standard deviation, minimum, maximum, etc.
  
3. **Correlations**:
   - **Correlation Matrix**: Shows how different numerical features are related. It highlights strong positive or negative correlations between variables.

4. **Missing Values**:
   - **Heatmap** and **Summary**: Visual representation of missing data and patterns within missing values.

5. **Data Quality Warnings**:
   - **Constant Features**: Identifies columns with constant values (which may be irrelevant for analysis).
   - **High Correlation**: Flags highly correlated features.
   - **High Cardinality**: Flags columns with a large number of unique categories, which might require special handling.

### **Example: Full Workflow**
Here’s how you can put it all together in a script or a Jupyter notebook:

```python
import pandas as pd
from ydata_profiling import ProfileReport

# Load the dataset
df = pd.read_csv('sales_data.csv')

# Generate a profile report
profile = ProfileReport(df, title='Sales Data Report', explorative=True)

# Display the report in a Jupyter notebook
# profile.to_notebook_iframe()

# Alternatively, save the report as an HTML file
profile.to_file("sales_data_report.html")
```

### **Common Use Cases for Pandas Profiling**
1. **Initial Exploratory Data Analysis (EDA)**:
   - It is very useful for quickly understanding the structure and quality of a dataset before delving into more advanced analysis.
  
2. **Data Quality Assessment**:
   - Detect missing data, outliers, or problematic variables that may require data cleaning.
  
3. **Dataset Documentation**:
   - Use the generated report to provide stakeholders or colleagues with an overview of the data.
  
4. **Feature Selection**:
   - Quickly identify highly correlated features or columns with little variance, which could be excluded from modeling.

### **Explorative Mode vs Minimal Mode**
- **Explorative Mode (`explorative=True`)**: Generates a more detailed report with additional analysis and visuals, such as correlations, interactions, and distributions. This is the default and provides a broad overview.
- **Minimal Mode (`minimal=True`)**: Use this to generate a simplified version of the report, especially useful when dealing with very large datasets, as it reduces processing time by excluding some of the detailed analyses.

### **Tips and Best Practices**
1. **Handling Large Datasets**:
   - Pandas Profiling can take a long time for very large datasets. In such cases, you can:
     - Use the `minimal=True` option.
     - Filter a sample of the dataset to profile.
     - Specify `df.sample(n)` to create a smaller dataset with `n` rows.

2. **Suppressing Warnings**:
   - If Pandas Profiling generates warnings about data quality issues that you’re already aware of, you can customize which warnings to disable using report settings.

3. **Use with Interactive Environments**:
   - It’s most effective when used in Jupyter notebooks, as the report is rendered interactively, and you can drill into each section of the report in real-time.

### **Example: Generate Minimal Report for Large Datasets**
If you have a very large dataset and want to speed up the process:

```python
profile = ProfileReport(df, title='Sales Data Report', minimal=True)
profile.to_file("sales_data_report_minimal.html")
```

### Summary
- **Pandas Profiling** is a powerful and time-saving tool for quickly understanding datasets.
- You can install it using `pip install ydata-profiling` and generate rich HTML reports.
- These reports provide a comprehensive overview of the dataset, including missing values, correlations, and descriptive statistics.
- Using options like **explorative** or **minimal** mode, you can control the level of detail in the report.
- It's particularly well-suited for exploratory data analysis, dataset documentation, and feature selection.

Feel free to try it out and let me know if you need more examples or details on using it effectively!