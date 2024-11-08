---
title: "Self hosted LLM with on-server storage"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Is it possible to self host an LLM that can store the outputs of your prompts in local database storage that you can host on your server? If so what kind of hardware spec would be needed and are there any "ready to go" packages?

# Outputs

Yes, it is possible to self-host a large language model (LLM) that can store the outputs of your prompts in a local database, which you can host on your server. However, the exact hardware specifications and setup will depend on the size of the model you want to run and the volume of data you plan to store. There are "ready-to-go" packages for self-hosting LLMs, some of which are open-source, but they may require varying levels of technical expertise to set up.

### Steps to Self-Host an LLM with Local Storage
1. **Choose the LLM**: Depending on your needs, you can opt for smaller models or large, more resource-intensive models. Some of the most common open-source models include:
   - **GPT-2, GPT-3** (via GPT-Neo or GPT-J models by EleutherAI)
   - **LLaMA (Meta)**
   - **Bloom** (by BigScience)
   - **Falcon** (by TII)

2. **Select a Framework/Package**: Some frameworks that allow for self-hosting LLMs include:
   - **Hugging Face Transformers**: One of the most popular libraries for serving LLMs. You can load models from Hugging Face’s Model Hub and serve them locally.
   - **FastAPI**: Combined with Hugging Face or other Python-based libraries, this allows you to build a web API around your LLM.
   - **Text Generation Web UI**: A user-friendly package that allows you to host models like GPT-J or GPT-NeoX with minimal configuration.
   - **AutoGPTQ / GPTQ-for-LLaMA**: These are designed for quantized versions of models, significantly reducing the computational burden.

3. **Hardware Requirements**:
   - **Smaller Models (1-3 billion parameters)**: These can typically run on consumer-grade GPUs (NVIDIA 3060, 3080) or CPUs, though with slower performance on CPUs. You would need at least 16GB of RAM and preferably a high-core-count CPU (8-16 cores).
   - **Larger Models (6-20+ billion parameters)**: For these, you would need powerful GPUs like the NVIDIA A100 or RTX 3090/4090, with at least 24GB of VRAM. For efficient inference, it’s recommended to have 128GB of system RAM and fast storage (NVMe SSDs).
   - **Quantized Models**: GPTQ allows you to run models with fewer resources, making models like LLaMA 7B or Falcon 7B usable on a single consumer GPU with 12GB or more VRAM.

4. **Database Storage**:
   - You can easily integrate a local database to store your LLM outputs. Common database options for this include:
     - **SQLite** (for small-scale use and quick setups).
     - **PostgreSQL** (more scalable for large-scale setups).
   - You can set up a basic Python script to connect the model to a database, saving the input prompts and output responses into the storage as you interact with the model.

### Example "Ready-to-Go" Packages:
1. **Text Generation Web UI**: A web-based interface that can be set up easily to load models such as GPT-J or GPT-NeoX. It includes prompt saving and other useful features.
2. **Hugging Face Inference API (Local)**: You can use Hugging Face models locally with their Python API, which is easily configurable to store prompt/response data to a database.
3. **LMDeploy**: A deployment toolchain for serving models like LLaMA efficiently on local hardware. It allows the integration of databases for output storage.

### Hardware Example for Medium-Sized Models (6B-13B Parameters):
- **GPU**: NVIDIA RTX 3090 (24GB VRAM) or RTX 4090.
- **CPU**: AMD Ryzen 5950X or Intel i9 (16 cores or more recommended for general use).
- **RAM**: 64-128GB for handling large inference tasks and dataset storage.
- **Storage**: NVMe SSD with at least 1TB for faster read/write operations during model inference and for storing model weights.
- **Operating System**: Linux (Ubuntu or Fedora) for better GPU and Python compatibility.

### Conclusion
It is entirely possible to self-host an LLM with output storage in a local database, and there are frameworks like Hugging Face Transformers and Text Generation Web UI to make this easier. The hardware specs depend on the size of the model and the performance you require.