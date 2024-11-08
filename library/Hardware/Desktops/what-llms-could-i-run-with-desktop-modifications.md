---
title: "What LLMs could I run with desktop modifications"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Let's say I was determined to optimise this hardware as much as possible for the sole purpose of running local LLMs. Where would I start? And what's the biggest and most advanced model that I could run after making all these changes? And what would that cost?

# Output

To optimize your **hardware** for running local **LLMs** and push the system to its limits, here’s a step-by-step guide on how to maximize performance and efficiency. After the upgrades and optimizations, I’ll suggest the biggest and most advanced models you could potentially run.

### **1. Maximize RAM**:
Your system currently has **32GB of DDR5 RAM**. To handle larger LLMs, upgrading to the **motherboard's capacity** of **128GB** will allow you to work with significantly bigger models. More RAM reduces the need for excessive paging (using the hard drive as temporary RAM), improving performance during inference.

- **Cost**: DDR5 RAM (128GB, 4x32GB) costs around **$400-$500** depending on the brand and speed.
- **Benefit**: Increases the ability to run models with more parameters and handle larger batch sizes.

### **2. Utilize Your GPU**:
You have an **AMD Radeon RX 7700 XT GPU** with **12GB VRAM**, which is crucial for running LLMs efficiently. While **NVIDIA** cards are more popular for LLM acceleration due to their **CUDA** support, AMD GPUs can still run models using **ROCm** (Radeon Open Compute) and **PyTorch**. Optimizing for **GPU inference** is critical to speed up the processing of LLMs.

- **Steps**:
  - **Install ROCm**: Ensure **ROCm** is installed and configured properly for AMD GPU acceleration.
  - **Use float16 (FP16)** precision models to reduce memory requirements without a large performance penalty.
  
### **3. CPU Optimization**:
Your **Intel Core i7-12700F (12 cores / 20 threads)** provides excellent multi-threading capabilities. However, when running larger models, ensure **hyper-threading** is enabled, and use CPU cores efficiently when working with multi-threaded workloads. You may not need CPU optimizations for GPU-based inference, but it can still help if you fall back to CPU-only runs for certain models.

- **Cost**: No additional cost, but you could consider better cooling if overclocking is on the table.

### **4. Storage Optimization**:
Your **BTRFS + RAID1** setup provides redundancy and speed, but it might not be necessary for performance-critical workloads like LLMs. You could switch to a **single SSD** configuration or consider an **NVMe drive** for extremely fast read/write speeds to reduce any potential bottlenecks when loading large models.

- **Cost**: High-performance **NVMe SSDs** with capacities like **2TB** typically cost **$200-$300**.
- **Benefit**: Faster loading of models, especially when working with large language models that require high disk I/O.

### **5. Optimize Software and Dependencies**:
- **PyTorch + ROCm**: Since you’re using an AMD GPU, **PyTorch with ROCm support** is essential. This allows you to use GPU resources efficiently.
- **Quantization**: Use **model quantization** (e.g., 8-bit or 4-bit precision) to reduce the memory and compute requirements of models, allowing you to run larger models within your available resources.
- **Offload to RAM**: Some frameworks allow you to offload parts of the model to CPU RAM when VRAM runs out (although this can slow down performance).

### **6. Advanced Cooling**:
If you plan to push the CPU and GPU to their limits, you may need improved cooling solutions to handle potential heat buildup from running LLMs at full capacity for extended periods.

- **Cost**: A **high-end cooling system** could range from **$100-$200**.
- **Benefit**: Prevents throttling and improves overall system stability during heavy computations.

---

### **Biggest and Most Advanced Models You Can Run After Optimization**

After optimizing your hardware (especially by upgrading the RAM to 128GB and optimizing GPU use), here are the largest models you could run efficiently:

#### **1. GPT-NeoX-20B (EleutherAI)**
- **Size**: 20 billion parameters.
- **VRAM Requirements**: You would likely need to use **CPU RAM offloading** with 20B models since 12GB VRAM is tight. However, with 128GB of RAM, you can balance between RAM and VRAM to run this model.
- **Why It Works**: NeoX-20B is one of the most advanced open-source LLMs, capable of high-quality generation. It will push the limits of your system, but with optimizations like quantization and memory offloading, it should be feasible.

#### **2. BLOOM-7B (BigScience)**
- **Size**: 7 billion parameters.
- **VRAM Requirements**: With 12GB of VRAM, **BLOOM-7B** should fit comfortably. If optimized with **FP16**, it can run on GPU without memory issues.
- **Why It Works**: BLOOM-7B is a multilingual model designed for large-scale performance and can handle complex tasks. It’s well-suited for systems with limited VRAM but strong CPU-RAM combinations.

#### **3. LLaMA-13B (Meta)**
- **Size**: 13 billion parameters.
- **VRAM Requirements**: You’ll need to rely on memory offloading to **RAM** since 12GB VRAM will not be enough to run the entire model in GPU memory.
- **Why It Works**: LLaMA is known for being highly efficient, so the 13B variant is an excellent choice for advanced tasks on your hardware, especially after memory upgrades.

#### **4. GPT-J-6B (EleutherAI)**
- **Size**: 6 billion parameters.
- **VRAM Requirements**: This model will comfortably fit in **12GB VRAM**, making it a good candidate for smooth GPU inference.
- **Why It Works**: GPT-J is a powerful and efficient model that strikes a balance between quality and resource demand, ideal for your hardware without needing significant optimizations.

---

### **Estimated Costs for Full Optimization**
1. **128GB DDR5 RAM**: $400-$500
2. **High-Performance NVMe SSD**: $200-$300 (optional)
3. **Advanced Cooling System**: $100-$200 (optional)

### **Total Estimated Cost**: **$400-$1000** depending on whether you add an NVMe drive and enhanced cooling.

---

### **Summary**
After optimizing your hardware (especially by upgrading RAM), you’ll be able to run models up to **20 billion parameters**, like **GPT-NeoX-20B**, with some compromises in performance via offloading. Models around **6-13 billion parameters** (e.g., **LLaMA-13B**, **BLOOM-7B**) will run efficiently and provide high-quality outputs.

Let me know if you'd like help setting up these optimizations!