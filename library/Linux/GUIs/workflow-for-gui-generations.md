---
title: "Workflow for GUI generations"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt
Please help me to define an iterative workflow for working with LLMs to generate software I'm using LLMs to create python programs My current workflow is 1: i write a prompt 2: llm generates 3: i copy in the code and test it out I'm not sure if it's best to move to a new spec addressing the errors in the first version the llm generates or to give feedback in the chat. what are your thoughts? Finally suggest a skeleton I could use in github in order to capture this unique workflow. I want to keep my prompts and the versions together in folders like v1/ v1/prompt v1/generatedprogram.py


# Output

Based on your current workflow and goals, I can suggest an improved iterative approach for working with LLMs to generate software. Here's a more structured and efficient workflow:

## Improved Iterative Workflow

1. **Initial Prompt Creation**
   - Write a detailed initial prompt specifying the program requirements.

2. **LLM Generation**
   - Use the LLM to generate the initial code based on your prompt.

3. **Code Review and Testing**
   - Copy the generated code into a file and test it.
   - Document any errors or improvements needed.

4. **Iterative Refinement**
   - Create a new prompt that includes:
     a) The original requirements
     b) The generated code
     c) Specific feedback on errors or desired improvements
   - Submit this new prompt to the LLM for refinement.

5. **Version Control**
   - Save each iteration as a new version in your project structure.

6. **Repeat Steps 3-5**
   - Continue this process until the code meets your requirements.

## Feedback Approach

Regarding your question about providing feedback, I recommend creating a new prompt for each iteration rather than giving feedback within the chat. This approach has several advantages:

1. It provides clear context for each iteration.
2. It allows you to maintain a history of changes and improvements.
3. It gives the LLM a fresh start with each iteration, potentially avoiding biases from previous conversations.

## GitHub Project Structure

Here's a suggested project structure for GitHub that captures your workflow:

```
project-name/
├── README.md
├── v1/
│   ├── prompt.md
│   ├── generated_program.py
│   └── feedback.md
├── v2/
│   ├── prompt.md
│   ├── generated_program.py
│   └── feedback.md
├── v3/
│   ├── prompt.md
│   ├── generated_program.py
│   └── feedback.md
└── final/
    ├── prompt.md
    └── final_program.py
```

## Workflow Implementation

To implement this workflow effectively, consider the following steps:

1. **Create a template for prompts**
   - Include sections for requirements, previous code (if applicable), and specific feedback.

2. **Use version control effectively**
   - Commit each version separately to track the evolution of your program.

3. **Implement automated testing**
   - Create a test suite that runs automatically on each new version.

4. **Document the process**
   - Maintain a changelog or development log to track major changes and decisions.

5. **Utilize GitHub features**
   - Use issues to track bugs or feature requests.
   - Create branches for significant changes or experiments.

6. **Consider using a workflow management tool**
   - Tools like GitHub Actions can automate parts of your process, such as running tests on new commits.

By following this structured approach, you can create a more efficient and traceable process for developing software with LLMs. This method allows you to iterate quickly while maintaining a clear history of your development process, making it easier to review, refine, and improve your code over time[1][2][4].

 