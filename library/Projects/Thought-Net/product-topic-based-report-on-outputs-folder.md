---
title: "Product topic based report on outputs folder"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Prompt Summary:** You asked for a script that can analyze files in the outputs folder and produce a report on the main topics emerging over time, without relying on paid APIs.

### Approach to Topic Analysis Without Paid APIs

Yes, it's possible to perform topic analysis on your Markdown files without using paid APIs. You can use **open-source natural language processing (NLP) tools** and libraries to extract main topics and generate a basic report. Here’s how you can do it:

### General Steps for Topic Analysis

1. **Text Preprocessing:**
   - Clean the text by removing stop words, punctuation, and any unnecessary characters.
   - Tokenize the text into words or phrases.

2. **Topic Modeling with Latent Dirichlet Allocation (LDA):**
   - Use **LDA** to identify topics in your dataset. LDA can determine clusters of words that frequently appear together and assign them as "topics."
   - You can then extract and interpret these topics to understand the main themes emerging over time.

3. **Visualize Topic Trends:**
   - Group your data by time (e.g., by month or week) to see how topics change over time.
   - Generate visualizations (e.g., line charts) to show the prevalence of each topic over time.

### Example Python Script for Topic Analysis Using Open-Source Tools

**Dependencies:**
Make sure you have the following Python libraries installed:
```bash
pip install nltk gensim matplotlib pandas
```

**Script:**

```python
import os
import re
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gensim import corpora
from gensim.models import LdaModel

# Download stopwords if not already done
import nltk
nltk.download('stopwords')
nltk.download('punkt')

def clean_text(text):
    # Remove special characters and stopwords
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())
    words = [re.sub(r'\W+', '', word) for word in words]
    words = [word for word in words if word.isalpha() and word not in stop_words]
    return words

def process_files(directory):
    # Prepare a list to store file data and timestamps
    file_data = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    cleaned_content = clean_text(content)
                    # Get file modification time as a proxy for when the output was generated
                    mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                    file_data.append((cleaned_content, mod_time))
    
    return file_data

def extract_topics(file_data, num_topics=5):
    # Prepare corpus for LDA model
    documents = [data[0] for data in file_data]
    dictionary = corpora.Dictionary(documents)
    corpus = [dictionary.doc2bow(doc) for doc in documents]
    
    # Train LDA model
    lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=10)
    
    # Extract topics
    topics = lda_model.print_topics(num_words=5)
    print("\nTop Topics Detected:")
    for topic in topics:
        print(topic)
    
    return lda_model, dictionary

def analyze_trends(file_data, lda_model, dictionary):
    # Group data by month
    df = pd.DataFrame(file_data, columns=["words", "timestamp"])
    df['month'] = df['timestamp'].dt.to_period('M')
    grouped = df.groupby('month')

    # Calculate topic prevalence over time
    topic_trends = []
    for period, group in grouped:
        # Create corpus for the group
        corpus = [dictionary.doc2bow(doc) for doc in group['words']]
        # Calculate topic distribution
        topic_counts = [0] * lda_model.num_topics
        for doc in corpus:
            topics_in_doc = lda_model.get_document_topics(doc)
            for topic_id, weight in topics_in_doc:
                topic_counts[topic_id] += weight
        
        # Normalize counts
        total = sum(topic_counts)
        topic_trends.append((period, [count / total for count in topic_counts]))
    
    # Convert to DataFrame for plotting
    trends_df = pd.DataFrame(topic_trends, columns=["Month", "Topic Distribution"])
    trends_df = trends_df.explode("Topic Distribution")
    trends_df["Topic ID"] = trends_df.groupby("Month").cumcount()
    
    return trends_df

def plot_topic_trends(trends_df):
    # Plot each topic trend over time
    trends_df['Month'] = trends_df['Month'].astype(str)  # Convert to string for plotting
    unique_topics = trends_df['Topic ID'].unique()
    
    for topic_id in unique_topics:
        topic_data = trends_df[trends_df['Topic ID'] == topic_id]
        plt.figure(figsize=(10, 6))
        plt.plot(topic_data['Month'], topic_data['Topic Distribution'], marker='o', linestyle='-')
        plt.title(f"Topic {topic_id} Trend Over Time")
        plt.xlabel("Month")
        plt.ylabel("Prevalence")
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f"topic_{topic_id}_trend.png")
        plt.close()

if __name__ == "__main__":
    # Directory containing markdown files
    directory = "/home/daniel/Vaults/outputhub_vault/Output_Hub/Outputs"
    
    # Process files and extract clean data
    file_data = process_files(directory)
    
    # Extract topics using LDA
    lda_model, dictionary = extract_topics(file_data, num_topics=5)
    
    # Analyze trends in topic prevalence over time
    trends_df = analyze_trends(file_data, lda_model, dictionary)
    n
    # Plot and save trends
    plot_topic_trends(trends_df)
    
    print("Topic analysis and plots generated.")
```

### Explanation

1. **Text Preprocessing:**
   - The `clean_text` function removes stopwords, punctuation, and special characters, then tokenizes the text. This is essential for accurate topic modeling.

2. **Processing Files:**
   - The script walks through the directory to read each Markdown file. It stores the cleaned content and file modification timestamp (as a proxy for when the content was generated).

3. **Topic Extraction with LDA:**
   - Using **Gensim's LDA model**, the script identifies the main topics across the Markdown files. It prints out the top topics, each represented by a set of keywords.

4. **Analyzing Trends Over Time:**
   - The script groups the files by month and calculates the prevalence of each topic in that period. This creates a time-series dataset that can be used to track how certain topics emerge or decline over time.

5. **Plotting Topic Trends:**
   - It generates line plots to show the trends of each topic over time, saving them as `topic_X_trend.png`.

### Requirements:
- **NLTK** and **Gensim**: To handle text processing and topic modeling.
- **Pandas** and **Matplotlib**: For data handling and visualization.

### Customization:
- **Adjust `num_topics`:** Change the number of topics you want to extract by modifying the `num_topics` parameter in `extract_topics`.
- **Improve Text Cleaning:** You can refine the `clean_text` function for better results (e.g., removing specific jargon or adding custom stopwords).

### Conclusion:
This script will help you identify the main topics emerging from your Markdown files and track how they change over time. You can do this entirely with open-source tools, avoiding the need for paid APIs. The final result provides visual insights into how topics evolve, which can be particularly valuable for understanding trends in your outputs.