---
title: "Library of prompts for testing LLMs"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I would like to build a repository of prompts.
The purpose of this repository of prompts would be specifically to evaluate LLMs for specific tasks that are of interest to me. 
Can you suggest what I might call this repository?
Help me think of the variety of prompts that I may wish to include
How can I record the prompts in a way that notes a little bit of metadata like the date I wrote the prompt? What else might I wish to note for the prompts?

# Output
### Name for Your Repository:
- **LLM Task Evaluator**
- **PromptBench**
- **TaskPrompt Library**
- **LLM Evaluation Prompts**
- **Promptify for LLMs**
- **PromptLab**

### Variety of Prompts You Might Include:
- **Summarization**: Provide summaries of articles, essays, or books.
- **Sentiment Analysis**: Evaluate the tone of text (positive, negative, neutral).
- **Question Answering**: Answer factual questions based on a given context.
- **Code Generation**: Generate code in Python, JavaScript, etc.
- **Creative Writing**: Write stories, poems, or creative content.
- **Translation**: Translate text between languages.
- **Text Classification**: Classify text into predefined categories.
- **Data Extraction**: Extract specific data from documents or tables.
- **Reasoning and Logic**: Answer logic puzzles or perform reasoning tasks.
- **Math Problems**: Solve algebraic or arithmetic problems.
- **Role-Playing**: Engage in dialogue simulations (e.g., customer service interactions).

### Metadata to Record for Each Prompt:
- **Date Created**: When the prompt was written.
- **Task Type**: The specific task or evaluation (e.g., summarization, translation).
- **Prompt ID**: A unique identifier for reference.
- **Expected Output**: A description of the desired or expected output.
- **Evaluation Metrics**: Criteria for evaluating the LLM's response (e.g., accuracy, creativity).
- **LLM Tested**: Which model(s) were tested with this prompt.
- **Notes on Prompt**: Observations or additional context for the prompt's creation.
- **Response Date**: Date the model generated the output.
- **Model Settings**: Notes on temperature, max tokens, or other model parameters.

### How to Record Prompts:
You can structure your prompt library using a **Markdown** or **JSON** format to track metadata, or use a **CSV** file for easier sorting. Here's a sample format:

#### Markdown Example:
```markdown
### Prompt ID: SUM-001
- **Date Created**: 2024-10-13
- **Task Type**: Summarization
- **Prompt**: "Summarize the following text in 50 words or fewer: [insert text]."
- **Expected Output**: A concise summary capturing the main idea.
- **LLM Tested**: GPT-4, GPT-3.5
- **Evaluation Metrics**: Accuracy, clarity, brevity
- **Response Date**: 2024-10-14
- **Model Settings**: Temperature: 0.7, Max Tokens: 100
```

#### JSON Example:
```json
{
  "prompt_id": "SUM-001",
  "date_created": "2024-10-13",
  "task_type": "Summarization",
  "prompt": "Summarize the following text in 50 words or fewer: [insert text].",
  "expected_output": "A concise summary capturing the main idea.",
  "llm_tested": ["GPT-4", "GPT-3.5"],
  "evaluation_metrics": ["Accuracy", "Clarity", "Brevity"],
  "response_date": "2024-10-14",
  "model_settings": {
    "temperature": 0.7,
    "max_tokens": 100
  }
}
```

This approach will help you systematically evaluate and compare different LLMs based on tasks of interest.