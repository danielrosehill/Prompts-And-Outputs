import os
import datetime
import matplotlib.pyplot as plt

# Define paths
library_dir = '/home/daniel/Git/prompts-and-outputs/library'
metrics_dir = '/home/daniel/Git/prompts-and-outputs/metrics'
count_file = os.path.join(metrics_dir, 'count_log.md')
graph_file = os.path.join(metrics_dir, 'graph.png')

# Function to count markdown files recursively
def count_markdown_files(directory):
    md_count = 0
    for root, dirs, files in os.walk(directory):
        md_count += len([f for f in files if f.endswith('.md')])
    return md_count

# Function to append count to markdown table
def update_markdown_table(date_str, count):
    header = "| Date       | Markdown Files |\n|------------|----------------|\n"
    row = f"| {date_str} | {count}            |\n"
    
    # Check if file exists and has content
    if not os.path.exists(count_file) or os.stat(count_file).st_size == 0:
        # If file doesn't exist or is empty, write the header and first row
        with open(count_file, 'w') as f:
            f.write(header)
            f.write(row)
    else:
        # Append new row to the existing table
        with open(count_file, 'a') as f:
            f.write(row)

# Function to plot graph of counts over time
def plot_graph():
    dates = []
    counts = []
    
    # Read data from the markdown file
    with open(count_file, 'r') as f:
        lines = f.readlines()[2:]  # Skip header lines
    
    for line in lines:
        parts = line.split('|')
        date_str = parts[1].strip()
        count = int(parts[2].strip())
        
        dates.append(datetime.datetime.strptime(date_str, '%d-%m-%y'))
        counts.append(count)
    
    # Plotting the graph
    plt.figure(figsize=(10, 6))
    plt.plot(dates, counts, marker='o', linestyle='-', color='b')
    plt.xlabel('Date')
    plt.ylabel('Markdown Files Count')
    plt.title('Markdown Files Count Over Time')
    plt.grid(True)
    
    # Save the graph as PNG file
    plt.savefig(graph_file)
    plt.close()

# Main script logic
if __name__ == "__main__":
    # Get current date and formatted string (dd-mm-yy)
    current_date = datetime.datetime.now().strftime('%d-%m-%y')
    
    # Count markdown files in the library directory
    md_count = count_markdown_files(library_dir)
    
    # Update markdown table with new data
    update_markdown_table(current_date, md_count)
    
    # Plot and save the graph
    plot_graph()
