---
title: "Prompt templates for generating tech specs for resting projects"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Here are some prompt templates you can use to generate a comprehensive technical specification document like the one I just provided. These prompts can help you efficiently structure different sections of a **Tech Spec** document by focusing on the key aspects of the project.

---

### **1. Project Overview Template**
*Prompt:*
> "Create a detailed project overview for a system that [describe the system’s goal and purpose]. The system will be used for [describe the target audience] and will include features such as [briefly list key features]. Ensure that the overview summarizes the primary goal, target users, and the major functionality."

*Example:*
> "Create a detailed project overview for a knowledge management system that organizes and stores LLM-generated outputs. The system is designed for professionals looking to curate and search through large amounts of LLM responses. Key features include full-text search, markdown editing, and user authentication."

---

### **2. Tech Stack Description Template**
*Prompt:*
> "List and describe the technology stack for a project involving [describe the project]. Include a description of the frontend framework, backend framework, database, search engine, and any other relevant technologies. Explain why each technology is suitable for the project."

*Example:*
> "List and describe the technology stack for a knowledge base that stores LLM outputs and allows users to search and edit them. Include the following: React for the frontend, FastAPI for the backend, MongoDB for the database, and ElasticSearch for search capabilities. Explain the advantages of each in this context."

---

### **3. Feature Set Template**
*Prompt:*
> "Generate a list of core features for a system designed to [describe the system]. Each feature should include a short description of what it does and how users will interact with it. Focus on the primary functionality that will be included in the first release or MVP."

*Example:*
> "Generate a list of core features for a knowledge base system that stores and organizes LLM outputs. Include note creation, editing with markdown, a list view of notes organized by tags, full-text search across notes, and basic user authentication."

---

### **4. System Architecture Template**
*Prompt:*
> "Provide a high-level system architecture for a project that includes [describe the components]. The architecture should explain how the frontend communicates with the backend, how data is stored in the database, and how search functionality is integrated. Include details on API communication, data flow, and how each component interacts."

*Example:*
> "Provide a high-level system architecture for a knowledge base that uses React as the frontend, FastAPI for the backend, MongoDB for data storage, and ElasticSearch for search. Include how the frontend communicates with the backend, and how search queries and data storage work."

---

### **5. Database Schema Template**
*Prompt:*
> "Design a sample database schema for storing [describe the data]. Include key fields and relationships between entities. Be sure to explain how different components of the data relate to one another and how they will be queried."

*Example:*
> "Design a sample database schema for storing conversations with LLMs, including fields for the conversation ID, prompts, outputs, tags, and timestamps. Explain how prompts and outputs are related and how the schema will be queried for search purposes."

---

### **6. Feature Prioritization and MVP Template**
*Prompt:*
> "Create a prioritized list of features for an MVP of a [describe the system]. Explain which features are essential for the first release, which are medium priority, and which can be added later as enhancements."

*Example:*
> "Create a prioritized list of features for an MVP of a knowledge base system. Prioritize backend CRUD functionality, frontend note creation and editing, and search features for the first release. Consider tagging and versioning as medium priority, and advanced authentication and mobile optimization as low priority."

---

### **7. Development Workflow Template**
*Prompt:*
> "Outline the development workflow for building a project that involves [describe the components]. Describe what should be developed first, the key milestones, and how the frontend and backend teams (or a single developer) should work together. Mention deployment and testing considerations."

*Example:*
> "Outline the development workflow for building a knowledge base project using React, FastAPI, MongoDB, and ElasticSearch. Focus on setting up the backend first with API routes, then build the frontend with TipTap integration for markdown editing. Finally, integrate the search functionality and set up Docker for local and cloud deployment."

---

### **8. Future Enhancements Template**
*Prompt:*
> "Provide a list of potential future enhancements for a system that [describe the current features]. Include features that could improve the user experience, performance, or security. Indicate which enhancements might require significant changes to the system architecture."

*Example:*
> "Provide a list of potential future enhancements for a knowledge base system that stores LLM outputs. Include features like two-factor authentication, advanced analytics, collaborative note editing, and automated summarization of LLM responses. Indicate that collaborative editing may require significant changes to data synchronization."

---

### **9. Reference and Resources Template**
*Prompt:*
> "List key resources, documentation, and tools that developers working on a [describe the project] will need. Include official documentation, relevant libraries, and any tutorials or resources that will help with setup and integration."

*Example:*
> "List key resources, documentation, and tools for developers working on a knowledge base project. Include MongoDB documentation, ElasticSearch setup guides, React and FastAPI tutorials, and TipTap editor integration resources."

---

These templates should help you capture different parts of your project effectively and ensure that anyone reviewing your spec document can clearly understand and execute your project in the future.