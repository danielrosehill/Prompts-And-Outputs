---
title: "Prompt for Output Hub guidance"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Could you generate an optimised prompt for Anthropic to use. It should define all the requirements for my Output Hub project and ask the LLM to begin providing the user with detailed and sequential steps to action the idea.

# Output

Certainly! Here's an optimized prompt for Anthropic's Claude to use for your Output Hub project:

```
You are an expert software architect and developer. I need your help to create a detailed, step-by-step plan for developing the Output Hub project. Here are the key requirements and features of Output Hub:

1. Purpose: A web-based application for managing and organizing LLM (Language Model) prompts, outputs, and custom agents.

2. Core Components:
   - Agents: Store and manage custom LLM agent configurations
   - Prompts: Create, edit, and organize prompts
   - Outputs: Store and manage LLM-generated outputs
   - Context: Store contextual information for prompts

3. Key Features:
   - CRUD operations for agents, prompts, and outputs
   - Ability to send prompts to LLM APIs and save returned outputs
   - Automatic linking between prompts and their corresponding outputs
   - Tagging system for easy categorization and retrieval
   - Search functionality across all components
   - User authentication and authorization

4. Technical Stack:
   - Backend: Node.js with Express.js
   - Database: MongoDB with Mongoose ODM
   - Frontend: React.js
   - API Integration: OpenAI or Anthropic API for LLM interactions

5. Additional Requirements:
   - Implement version control for prompts and outputs
   - Periodic backups to cloud storage (B2 or similar)
   - Ability to add metadata and follow-up notes to outputs

Please provide a detailed, sequential list of steps to develop this project, including setup, implementation of core features, testing, and deployment. For each step, include specific technical details and best practices to follow.






## Extracted Prompts
[[Prompts/Prompt for Output Hub guidance.md#Prompt 1|Prompt 1]]
