---
title: "More advanced system for creating analytics elements for vault reporting"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Prompt Summary:** You asked for a way to directly generate plots showing the growth in the number of outputs and words over time. You are looking for the script to store data in a format that is ideal for plotting, and you would like separate charts for each.

### Improved Script with Data Logging and Plotting

To track growth over time, you need to store the data in a way that captures **daily snapshots** of the total number of files and words. This can then be used to create time-series plots. The following updated script will:

1. **Log the total files and word count over time** to a CSV file.
2. **Generate and save two separate plots**:
   - One showing the growth in the number of outputs over time.
   - Another showing the growth in the number of words over time.

### Python Script

```python
import os
import csv
from datetime import datetime
import matplotlib.pyplot as plt

def count_files_and_words(directory):
    total_files = 0
    total_words = 0
    total_chars = 0

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                total_files += 1
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    total_words += len(content.split())
                    total_chars += len(content)

    return total_files, total_words, total_chars

def log_data_to_csv(total_files, total_words, csv_file):
    # Create the CSV file with headers if it doesn't exist
    if not os.path.exists(csv_file):
        with open(csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Total Files", "Total Words"])

    # Append today's data
    with open(csv_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().strftime("%Y-%m-%d"), total_files, total_words])

def plot_growth(csv_file):
    # Read data from CSV
    dates = []
    total_files = []
    total_words = []

    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            dates.append(datetime.strptime(row[0], "%Y-%m-%d"))
            total_files.append(int(row[1]))
            total_words.append(int(row[2]))

    # Plot Total Files Over Time
    plt.figure(figsize=(10, 6))
    plt.plot(dates, total_files, marker='o', linestyle='-')
    plt.title("Growth in Number of Outputs Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Outputs")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("total_outputs_over_time.png")
    plt.close()

    # Plot Total Words Over Time
    plt.figure(figsize=(10, 6))
    plt.plot(dates, total_words, marker='o', linestyle='-')
    plt.title("Growth in Number of Words Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Words")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("total_words_over_time.png")
    plt.close()

if __name__ == "__main__":
    # Set the directory to scan
    directory = "/home/daniel/Vaults/outputhub_vault/Output_Hub/Outputs"
    
    # Generate report
    total_files, total_words, total_chars = count_files_and_words(directory)
    
    # Define the CSV file for logging
    csv_file = "output_growth.csv"
    
    # Log data to CSV
    log_data_to_csv(total_files, total_words, csv_file)
    
    # Generate plots
    plot_growth(csv_file)
    
    print("Data logged and plots generated.")
```

### Explanation

1. **`count_files_and_words(directory)`:** 
   - Counts the total Markdown files, words, and characters in the specified directory.

2. **`log_data_to_csv(total_files, total_words, csv_file)`:**
   - Logs the total number of files and words, along with the current date, to a CSV file (`output_growth.csv`). This allows you to track changes over time.
   - If the CSV file doesn’t exist, it creates one with headers.

3. **`plot_growth(csv_file)`:**
   - Reads the logged data from the CSV file and generates two line plots:
     - **Total Outputs Over Time**
     - **Total Words Over Time**
   - Saves the plots as `total_outputs_over_time.png` and `total_words_over_time.png` in the same directory as the script.

4. **How to Use:**
   - Save the script as `generate_report_and_plot.py`.
   - Open a terminal and navigate to the directory containing the script.
   - Run the script using:
     ```bash
     python3 generate_report_and_plot.py
     ```
   - This will log the data to `output_growth.csv` and generate the two plots, which will be saved in the same directory as `total_outputs_over_time.png` and `total_words_over_time.png`.

5. **Dependencies:**
   - Install `matplotlib` if you haven’t already:
     ```bash
     pip install matplotlib
     ```
   - The script uses built-in libraries for file handling and CSV manipulation.

### Benefits
- **Automation:** You can run this script periodically (e.g., using a cron job) to log daily snapshots and keep track of growth without manual effort.
- **Data Logging:** Having a CSV log allows you to track progress over time and revisit historical data for additional analysis.
- **Visualizations:** Easily see trends in output growth and word count, helping you analyze productivity over time.

This solution simplifies both data logging and visualization, giving you a streamlined way to monitor the growth of your Markdown outputs.