---
title: "Custom UIs for LLMs"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Can you suggest any customisable UIs / frontends for LLMs? Perhaps you provide API keys and you get to the use the frontend just for chatting. But you get a more customisable experience and can do things like save the chats to your own storage?
# Output

There are several customizable **UIs/frontends** for **Large Language Models (LLMs)** that allow users to integrate their own **API keys** (e.g., OpenAI or other LLM services) and use a tailored frontend for a more flexible experience, including saving chats to custom storage. Below, I’ve listed some solutions that provide **customizable chat experiences** along with the ability to integrate with **external APIs**.

### 1. **Flowise**
- **Overview**: **Flowise** is an open-source **chatbot builder** with a visual interface. It allows users to create custom chatbots using **API keys** for LLMs, such as OpenAI.
- **Customizable Features**:
  - Drag-and-drop visual designer to create workflows.
  - Allows integration with **custom databases** for data storage, which makes saving chat history possible.
  - Supports external plugins and modules to enhance chatbot functionality.
- **Backend Storage**: You can integrate your **own storage solutions** (such as a local database or cloud storage) for saving chat history.
- **Website**: [Flowise](https://github.com/FlowiseAI/Flowise)

### 2. **Chatbot UI (by mckaywrigley)**
- **Overview**: **Chatbot UI** is an open-source project designed as an alternative frontend for interacting with **OpenAI’s GPT models**.
- **Customizable Features**:
  - Provides a simple, clean interface for interacting with LLMs.
  - Users can **provide their own OpenAI API key** and use the chatbot for personal purposes.
  - Chats can be exported manually, and users can modify the code to connect to a **custom storage backend** (like a database).
- **Installation**: It’s a web-based tool that you can host yourself, providing complete control over chat handling.
- **GitHub**: [Chatbot UI Repository](https://github.com/mckaywrigley/chatbot-ui)

### 3. **Hugging Face Spaces**
- **Overview**: **Hugging Face Spaces** are web applications that can be customized to run LLMs using their **Inference API**.
- **Customizable Features**:
  - Use tools like **Gradio** or **Streamlit** to build an interactive chat UI.
  - You can customize the entire interface and **connect to your own API keys** from services like OpenAI.
  - Offers the ability to **save conversations** to custom databases or export chat data.
- **Benefits**: If you deploy on **Hugging Face**, you have a cloud-based solution, but you can also run it locally if you want full control.
- **Website**: [Hugging Face Spaces](https://huggingface.co/spaces)

### 4. **Open Assistant**
- **Overview**: **Open Assistant** is an open-source implementation similar to ChatGPT, providing a customizable interface to interact with LLMs.
- **Customizable Features**:
  - Users can use their **API keys** for various LLM services.
  - Customizable frontend interface to suit individual preferences.
  - You can modify the source code to add features such as **automatic chat history saving** to a custom backend like a **Postgres** or **SQLite** database.
- **GitHub**: [Open Assistant Repository](https://github.com/LAION-AI/Open-Assistant)

### 5. **Langchain with Custom Frontend**
- **Overview**: **Langchain** is a framework designed for building applications powered by language models. By combining Langchain with a **custom frontend** like **Streamlit**, you can create a highly personalized UI for interacting with LLMs.
- **Customizable Features**:
  - Use Langchain to connect to multiple LLMs (OpenAI, GPT-Neo, Cohere, etc.).
  - Fully customizable with **Streamlit** or **Gradio** for building a user-friendly interface.
  - You can store chat histories using **custom storage backends** or integrate with **vector databases** like Pinecone or Weaviate.
- **Use Case**: Langchain is particularly powerful if you want to add functionalities like **retrieval-augmented generation (RAG)** or integration with various APIs.

### 6. **Jarvis (Self-Hosted Chatbot)**
- **Overview**: **Jarvis** is an open-source chatbot that can be hosted locally or on a server. It allows integration with multiple LLMs via their API keys.
- **Customizable Features**:
  - Users can provide their **API key** for various LLM providers.
  - The interface is designed to be simple, but fully customizable if you want to adapt it to your use case.
  - Offers options to **log and save chat history** to local files or custom databases.
- **GitHub**: [Jarvis](https://github.com/mrskrt/jarvis)

### 7. **Chatr**
- **Overview**: **Chatr** is another **open-source customizable chatbot UI** that allows users to interact with LLMs by providing an API key.
- **Customizable Features**:
  - Offers a straightforward way to set up a chat interface with **API keys** for OpenAI or other LLM services.
  - Chats can be **saved locally** or integrated with other custom storage solutions.
  - Users can adjust the frontend to change appearance, add buttons, or automate saving.
- **GitHub**: [Chatr](https://github.com/tom-doerr/chatr)

### Summary of Features

| Tool                  | Customizability | API Integration | Chat History Storage | Technology Stack  |
|-----------------------|-----------------|-----------------|----------------------|-------------------|
| **Flowise**           | Visual builder  | Yes             | Custom storage       | Node.js           |
| **Chatbot UI**        | Web frontend    | Yes             | Custom backend       | React             |
| **Hugging Face Spaces** | High          | Yes             | Customizable         | Streamlit/Gradio  |
| **Open Assistant**    | Web-based       | Yes             | Custom backend       | Python            |
| **Langchain + UI**    | Fully customizable | Yes          | Full customization   | Langchain + Streamlit/Gradio |
| **Jarvis**            | Simple UI       | Yes             | Local or custom DB   | Python            |
| **Chatr**             | Web-based       | Yes             | Local/custom storage | Python            |

### Recommendations
- If you’re looking for a **plug-and-play customizable UI**, **Chatbot UI** or **Open Assistant** could be great options since they offer a ready-made interface that is also easy to modify.
- For **visual customization** and flexibility in workflows, **Flowise** would be an ideal choice since you can build complex flows with ease.
- If you want to integrate with **custom storage solutions** and need full control, building a chatbot with **Langchain** and using **Gradio** or **Streamlit** as a frontend provides complete flexibility.

These solutions can provide a **customizable chat experience** while allowing you to integrate your **API keys** and save conversations to your own storage, giving you more control over both the frontend and backend of the application.