---
title: "Prompting a custom agent to build frontend"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

  
Here's an approach that perhaps might work: I could create a custom AI agent which has that DDL as knowledge. I'd like to be able to prompt it repeatedly to build the frontend. Can you suggest the best LLM/AI for this project?

# Output

Your approach of creating a custom AI agent with the DDL as knowledge is an excellent idea. It would allow for a more tailored and iterative process in building your frontend. Let me suggest some options for the best LLM/AI for this project.





# AI Models Comparison for Custom Frontend Development Agent

## 1. GPT-4

### Pros:
- Exceptional natural language understanding and generation
- Strong coding capabilities across multiple languages
- Can understand and generate complex, multi-file projects
- Excellent at following detailed instructions and maintaining context

### Cons:
- Can be expensive for high-volume usage
- May have rate limits or queues for API access

### Best for:
- Complex, multi-step development tasks
- Generating entire applications or large components
- Handling intricate database schemas and relationships

## 2. Claude 2

### Pros:
- Strong coding abilities and language understanding
- Good at maintaining context over long conversations
- Can handle large amounts of input data (like your DDL)
- Generally faster response times than GPT-4

### Cons:
- Slightly less powerful than GPT-4 for some complex tasks
- May require more specific prompting for best results

### Best for:
- Iterative development with frequent back-and-forth
- Handling large schemas and generating corresponding frontend code

## 3. CodeGen 16B

### Pros:
- Specifically designed for code generation
- Can generate high-quality code across various programming languages
- Potentially faster and more cost-effective for pure coding tasks

### Cons:
- Less versatile in natural language understanding compared to GPT-4 or Claude
- May require more structured input

### Best for:
- Rapid generation of specific code snippets or functions
- Focusing purely on code generation rather than explanation or natural language interaction

## 4. GitHub Copilot (powered by OpenAI Codex)

### Pros:
- Integrated directly into development environments
- Excellent at understanding context from existing code
- Can generate code in real-time as you type

### Cons:
- Less suitable for generating entire applications from scratch
- Requires integration with an IDE or editor

### Best for:
- Augmenting your development process in real-time
- Generating smaller components or individual functions

## 5. GPT-3.5 Turbo

### Pros:
- More cost-effective than GPT-4
- Faster response times
- Still capable of generating good quality code

### Cons:
- Less powerful than GPT-4, especially for complex tasks
- May require more iterations to achieve desired results

### Best for:
- Rapid prototyping and initial code generation
- Cost-effective development of smaller components

## Recommendation

For your specific use case of creating a custom agent with DDL knowledge for iterative frontend development, I would recommend either GPT-4 or Claude 2.

GPT-4 would be the top choice if budget is not a primary concern and you need the most powerful option for handling complex schemas and generating comprehensive frontend code.

Claude 2 would be an excellent alternative, offering a good balance of power, speed, and potentially lower cost. It's particularly well-suited for handling large inputs (like your DDL) and maintaining context over extended interactions.

Both of these models would allow you to create a custom agent that can understand your database schema, generate appropriate frontend code, and engage in an iterative development process based on your prompts and feedback.


Based on this comparison, I believe GPT-4 or Claude 2 would be the best choices for your project. Here's how you could proceed:

1. Choose either GPT-4 or Claude 2 as your base model.

2. Create a custom prompt that includes:
   - Your entire DDL as context
   - Instructions for generating frontend code (e.g., preferred framework, styling approach)
   - Any specific requirements or conventions you want to follow

3. Use this custom prompt to create your AI agent, essentially giving it the "knowledge" of your database schema and the task of frontend development.

4. Interact with this agent iteratively, asking it to generate different parts of your frontend, make modifications, or explain its choices.

This approach allows you to have a "conversation" with an AI that understands your specific database structure, making the frontend development process more tailored and efficient.

Would you like me to help you draft an initial prompt for creating this custom agent?## Extracted Prompts
[[Prompts/Autocapture/Prompting a custom agent to build frontend.md#Prompt 1|Prompt 1]]





## Extracted Prompts
[[Prompts/Prompting a custom agent to build frontend.md#Prompt 1|Prompt 1]]
