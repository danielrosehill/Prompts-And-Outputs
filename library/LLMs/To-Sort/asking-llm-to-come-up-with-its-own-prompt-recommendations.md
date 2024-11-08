---
title: "Asking LLM to come up with its own prompt recommendations"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Is there a name for the process of using an LLM to come up with prompts for the same LLM? Is it a recognised and legitimate technique?

# Output

The process of using a **Large Language Model (LLM)** to generate prompts for itself or another LLM is generally referred to as **"recursive prompting"** or **"self-reflective prompting."** It is a recognized and increasingly studied technique, particularly within the field of **prompt engineering** and **meta-learning**.

### Names and Concepts Associated with the Process

1. **Recursive Prompting**:
   - This term refers to generating prompts from an LLM and then using these prompts to further refine or enhance responses from the same or another LLM. It is called "recursive" because the output of the model is used as input again in a loop-like manner.

2. **Self-Reflective Prompting**:
   - Self-reflective prompting involves asking the model to evaluate its own output and suggest ways to improve it. This can include generating a new prompt that might yield better answers, effectively refining the inquiry process.

3. **Auto-Prompting**:
   - Auto-prompting refers to leveraging the LLM to generate optimal prompts for future iterations. The goal is to create an increasingly effective set of prompts based on initial attempts and results, which the model "learns" through recursive application.

### Is It Recognized and Legitimate?

Yes, **recursive prompting** is a recognized and legitimate technique that is particularly useful in **prompt engineering** for several reasons:

1. **Iterative Improvement**:
   - By using an LLM to generate prompts for itself, users can iteratively improve the output, ensuring that the final response is more detailed, insightful, or tailored to their specific requirements. This iterative process allows for more precise and complex interactions.

2. **Enhancing Output Quality**:
   - This method helps in **expanding the quality of responses**. For example, if the initial prompt yields a vague answer, asking the LLM to refine the question can generate a better prompt that leads to richer content.

3. **Research and Applications**:
   - Researchers have found that recursive prompting can be useful in scenarios such as **document summarization**, **coding assistance**, and **complex problem-solving**, where the model is used to guide itself through multiple steps or prompts until a satisfying output is achieved.
   - The technique is used to help LLMs produce **multi-step reasoning** by generating intermediate questions or breaking down complex tasks into smaller parts.

### Examples of Legitimate Use

- **Chain-of-Thought Prompting**:
  - A related recognized strategy is **chain-of-thought prompting**, where the model generates a step-by-step breakdown of its thought process. Recursive prompting can be used in this context to keep refining or guiding those intermediate thoughts, ensuring the output remains consistent and logical.

- **Meta-Prompting**:
  - **Meta-prompting** involves using the LLM to help create prompts that control or modify its behavior. This can involve asking the LLM to think about how it would best respond to a particular type of inquiry, generating more efficient or well-structured prompts.

- **Human-in-the-Loop Scenarios**:
  - In many practical applications, humans work alongside LLMs to generate and refine prompts, using the LLM's ability to propose new prompts to speed up the **discovery of optimal inquiries**. This workflow reduces the trial-and-error involved in crafting effective prompts from scratch.

### Studies and Tools
- There are studies and tools that explicitly explore recursive prompting. For instance, the concept of **"ReAct"** (Reasoning and Acting) combines chain-of-thought prompting with actions, where the model keeps prompting itself to act or reason further based on earlier responses.
- Tools like **AutoGPT** utilize recursive prompting strategies to generate complex tasks and sub-tasks automatically. **AutoGPT** essentially operates by having the LLM generate actions and prompts that it then executes iteratively, showcasing a practical use of the recursive approach.

### Practical Benefits
- Recursive prompting can **reduce the cognitive load** on users trying to craft complex queries and help the model itself generate better-phrased and more efficient prompts.
- It allows non-experts to leverage the LLM's capabilities to generate more advanced prompts, making powerful use of the model accessible without needing deep knowledge of prompt engineering techniques.

### Summary
Using an LLM to generate prompts for itself is known as **recursive prompting** or **self-reflective prompting**, and it is a legitimate and effective technique for improving interaction quality. It’s commonly used in areas such as **prompt engineering**, **document summarization**, **multi-step reasoning**, and as part of sophisticated workflows like **AutoGPT**. This iterative prompting helps achieve more precise, detailed, and context-aware responses, enhancing the overall utility of LLMs.