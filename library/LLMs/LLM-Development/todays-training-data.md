---
title: "Where does today's training data come from? What's being used?"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



The leading sources of training data for the latest large language models (LLMs) are vast, diverse, and often publicly available datasets. These datasets are typically composed of large amounts of text data, including web crawls, books, research papers, and code repositories. Some of the most prominent sources include:

### 1. Common Crawl

Common Crawl is one of the largest and most widely used datasets for training LLMs. It consists of billions of web pages crawled from the internet, providing a massive amount of text data that is freely available and regularly updated. Many LLMs, such as GPT-3, LLaMA, Falcon, and others, heavily rely on Common Crawl due to its size and diversity\[4]\[5].

### 2. The Pile

The Pile is another major dataset used for training LLMs. It is an 800 GB corpus curated from 22 diverse sources such as academic papers, books, and web content. The Pile is designed to enhance generalization across different domains and has been used in models like GPT-Neo and OPT\[3].

### 3. C4 (Colossal Clean Crawled Corpus)

C4 is derived from Common Crawl but undergoes extensive cleaning to remove non-natural language data (e.g., gibberish text). It is a 750 GB English corpus that has been used in models like T5 and MPT-7B\[3].

### 4. RefinedWeb

RefinedWeb is a dataset that offers over 5 trillion tokens of textual data, with a focus on high-quality content. It was developed for models like Falcon-40B and provides a more curated version of web crawl data\[3].

### 5. Wikipedia

Wikipedia datasets are commonly used for training LLMs due to their structured nature and high-quality content across various languages. This dataset has been utilized in many models to provide factual knowledge and improve generalization\[3].

### 6. Specialized Datasets

In addition to general web data, specialized datasets are also increasingly important:

- **Starcoder Data**: A dataset focused on programming languages with 783 GB of code from GitHub and Jupyter Notebooks\[3].
- **OpenMathInstruct-1**: A dataset combining natural language instructions with Python code for solving math problems\[1].
- **BookCorpus**: A dataset containing text from unpublished books, used in models like RoBERTa and XLNet\[3].
- **ROOTS**: A multilingual dataset curated from 59 languages, used to train the BLOOM model\[3].

### 7. Synthetic Data

Synthetic datasets like Cosmopedia are also becoming more common. These datasets are generated artificially but are designed to mimic real-world text patterns and provide additional diversity in training data\[1].

Overall, the leading sources of training data for LLMs are large-scale web crawls (especially Common Crawl), curated corpora like The Pile and C4, as well as specialized or synthetic datasets tailored to specific tasks such as programming or mathematics. These datasets ensure that LLMs can generalize across various domains while maintaining high performance on specific tasks.

&#x20;
