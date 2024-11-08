---
title: "Feasibility testing on an LLM to run over my Obsidian vault"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'm wondering if you could advise upon the following

I'm storing my LLM outputs in an Obsidian vault. It's rapidly growing. At the time I'm writing this, I have almost 800 outputs stored, all of them markdown files.

I would love to develop a program which is itself based on an LLM and which I can use to mine the data in my own output repo.

To give you an example use-case:

I would love to be able to mine my outputs repository in order to find the most interesting outputs which showcase some of the most creative uses of AI. I might wish to use that list to share some of those snippets in a blog

Before we talk about how to make this, I'm wondering if it's possible. 

From a technical standpoint, I'm wondering whether it's possible for an LLM agent I'm using via an LLM to recurse over a folder structure in this manner.

Please advise!

# Output

Yes, it is certainly possible to develop a program that uses an LLM to analyze and mine data from your Obsidian vault containing LLM outputs. Here's an overview of how you could approach this:

## Technical Feasibility

From a technical standpoint, it is indeed possible for an LLM-based agent to recursively analyze a folder structure containing markdown files[3]. This can be achieved through a combination of file system operations and LLM-powered analysis.

## Implementation Approach

To create such a system, you would need to combine several components:

1. **File System Traversal**: Use Python's built-in libraries like `os` or `glob` to recursively traverse your Obsidian vault and identify all markdown files[1].

2. **File Content Extraction**: Read the content of each markdown file.

3. **LLM Integration**: Use an LLM (such as GPT-3 or a local alternative) to analyze the content of each file.

4. **Retrieval-Augmented Generation (RAG)**: Implement a RAG system to allow the LLM to access and reference the content of your vault when answering queries[2].

## Key Components

### File System Analysis

You can use Python's `os.walk()` or `glob.glob()` functions to recursively traverse your Obsidian vault:

```python
import os

for root, dirs, files in os.walk('/path/to/obsidian/vault'):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            # Process the markdown file
```

### LLM Integration

You'll need to choose an LLM and an appropriate library or API to interact with it. For local deployment, you might consider options like LlamaIndex or Langchain[2].

### Retrieval-Augmented Generation (RAG)

RAG is crucial for allowing the LLM to access and utilize the information in your vault. This involves indexing your markdown files and providing relevant context to the LLM during query time[2].

## Potential Challenges

1. **Performance**: With 800+ files, ensure your system can handle the volume efficiently.

2. **Context Limitations**: Most LLMs have token limits for input, so you'll need to implement strategies to summarize or chunk large files.

3. **Relevance Ranking**: Developing a system to accurately rank outputs based on "interestingness" or "creativity" may require fine-tuning or careful prompt engineering.

## Next Steps

1. Choose your tech stack (e.g., Python + LlamaIndex + GPT-3).
2. Implement file system traversal and content extraction.
3. Set up RAG system to index your vault.
4. Develop prompts for the LLM to analyze creativity and interestingness.
5. Create a query interface to interact with your system.

With these components in place, you should be able to create a powerful tool for mining insights from your LLM output repository, including identifying creative and interesting uses of AI for your blog.

 