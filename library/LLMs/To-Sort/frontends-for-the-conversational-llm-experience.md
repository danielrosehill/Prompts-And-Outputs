---
title: "Frontends for the conversational LLM experience"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Very interesting. It sounds like options are actually very limited. Using things like APIs and Lang Hub seems like one way of doing this (being able to automatically capture outputs into your database or business systems). Or building custom solutions. But if you want to still take advantage of the ease of a conversational interface with the LLM .... I'm not sure what you'd do.

Are there any frameworks or tools which specifically focus on providing the conversational frontends to existing LLMs and do that via API integration. It seems to me that this would be one approach to get the kind of system I'm looking for developed.

# Output

You're absolutely right—there seems to be a **gap** between platforms offering conversational frontends and those that support **automatic capture** of outputs into user-controlled systems like databases and object storage. However, there are **frameworks and tools** that focus on providing conversational frontends to existing LLMs **via API integration**. These can act as a bridge to create the kind of system you're looking for. Here's a breakdown of relevant options:

### 1. **Rasa**
   - **Focus**: Conversational AI Framework
   - **How It Works**: Rasa is an open-source framework designed for building custom conversational interfaces (chatbots) with deep integration options via APIs. It supports connections to multiple LLMs and allows you to build fully customizable chatbots with the ability to route responses through different models.
   - **API Integration**: You can directly connect LLM APIs (e.g., OpenAI, Hugging Face) and program Rasa to export or log conversation outputs to databases, including SQL/NoSQL systems.
   - **Suitability**: **Excellent** for users who want to build a **custom solution** with full control over data storage. It provides flexibility in routing conversations, logging data, and exporting outputs automatically to business systems.

### 2. **Botpress**
   - **Focus**: Conversational AI Platform
   - **How It Works**: Botpress is an enterprise-grade chatbot framework that can integrate with LLMs via APIs. It offers a user-friendly web interface while allowing developers to automate prompt handling and export outputs to external databases or cloud storage through workflows.
   - **API Integration**: Supports API integration with external LLMs and can be connected to databases for logging all user interactions and responses in real-time. It also offers a conversational frontend that can be used as the interaction point.
   - **Suitability**: **Very Good**. If you want an **easy-to-use conversational interface** but still need strong backend API capabilities for exporting data, Botpress is a solid option.

### 3. **ChatterBot (Python Library)**
   - **Focus**: Conversational Framework
   - **How It Works**: ChatterBot is a Python library designed for building conversational agents. While it’s typically used for simple chatbot applications, it can be connected to LLM APIs (like GPT-3) and can be extended to store conversations and outputs in databases via Python code.
   - **API Integration**: Easily integrates with LLM APIs through Python, and all outputs can be logged directly into SQL databases or exported to cloud storage systems using additional Python libraries.
   - **Suitability**: **Good** for users comfortable with coding and looking for a lightweight solution to capture LLM outputs. **Less suited** for non-developers, as it requires more setup than pre-built platforms.

### 4. **Dialogflow CX (Google Cloud)**
   - **Focus**: Conversational AI Platform
   - **How It Works**: Dialogflow CX is a cloud-based conversational platform with a focus on managing complex dialogues. It integrates with LLMs via Google Cloud's ecosystem and offers APIs for integrating external services and storing conversational data.
   - **API Integration**: Can integrate with external LLMs (via API) and export data directly into Google Cloud databases (BigQuery, Firestore, etc.), allowing full logging and automated storage of conversations and outputs.
   - **Suitability**: **Very Good** for power users who are already in the **Google Cloud ecosystem** and need seamless API integrations to manage and export data.

### 5. **Microsoft Bot Framework**
   - **Focus**: Conversational AI for Enterprises
   - **How It Works**: Microsoft Bot Framework allows developers to build bots that can be connected to LLMs via APIs (e.g., Azure’s OpenAI service). It also supports data export, allowing you to capture conversational outputs in your own business systems, whether that's a SQL database or Azure Storage.
   - **API Integration**: Integrates well with LLMs through APIs and allows storing outputs into Azure databases or external systems via custom logic. It’s also integrated with Azure’s AI services for more advanced use cases.
   - **Suitability**: **Very Good** if you're working within the **Microsoft Azure ecosystem** and need deep integration into existing business systems with full data capture capabilities.

### 6. **Gradio**
   - **Focus**: UI for Machine Learning Models
   - **How It Works**: Gradio is a web-based interface for machine learning models, including LLMs. It allows you to create conversational UIs for LLMs that can be easily integrated with APIs. While it is primarily a front-end, it can be connected to backends that store the outputs into databases or object storage.
   - **API Integration**: Supports API-based interactions, allowing LLM outputs to be logged via custom backends. You can use Gradio as the front-end for user interactions and build a pipeline to send outputs to databases like PostgreSQL or object storage solutions.
   - **Suitability**: **Good** for users who need **minimal setup** for the UI part but are comfortable building the integration layer for capturing and storing outputs.

### 7. **Streamlit**
   - **Focus**: Data App Framework
   - **How It Works**: Streamlit is an open-source framework for building custom web apps. Although not explicitly designed for conversational AI, you can build a conversational UI for LLMs using APIs, and integrate it with storage solutions for prompt/response logging.
   - **API Integration**: With Streamlit, you can integrate LLM APIs and use its ability to export and store data into databases or cloud storage solutions. It's suitable for those who want to build customized conversational workflows while managing the data pipeline themselves.
   - **Suitability**: **Very Good** for developers comfortable with coding and building custom pipelines for data storage. You get full flexibility to capture all prompt data into any storage solution of your choice.

### 8. **Kore.ai**
   - **Focus**: Conversational AI Platform for Enterprises
   - **How It Works**: Kore.ai offers a no-code platform with API integration capabilities for LLMs. It focuses on providing enterprise-grade bots with robust analytics and logging, allowing for prompt and response capture.
   - **API Integration**: Supports integration with external LLMs and provides native export options to external databases or object storage solutions. You can automatically capture and log every interaction and store it for later use.
   - **Suitability**: **Very Good**. Especially strong for users looking for a **no-code interface** combined with powerful export and data logging capabilities.

---

### Best Options for Conversational Frontends + API Integration:

1. **Rasa**: Excellent for users who want to **build custom conversational UIs** with full control over logging data into databases or cloud storage.
2. **Botpress**: **Enterprise-grade** with a good balance of **ease of use** and backend integration options for exporting LLM outputs.
3. **Dialogflow CX**: Strong for those in the **Google Cloud ecosystem** who want to leverage Google’s AI tools and easily export data.
4. **Gradio** and **Streamlit**: Both are good if you’re comfortable building the conversational frontend **with flexibility** in backend integration.
5. **Microsoft Bot Framework**: Excellent for Azure users who want seamless LLM integration and automatic logging into business systems.
6. **Kore.ai**: Best for those who need a **no-code solution** with strong data logging capabilities and API integrations.

These tools and frameworks allow you to build **conversational frontends** for interacting with LLMs, while also enabling integration with your existing **business systems or databases** for **automatic data capture**. By using these, you can have both a smooth conversational interface and robust control over your data storage.