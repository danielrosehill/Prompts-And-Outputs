---
title: "Using only DP ports on GPU for DDCUTIL support"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Summary of your prompt:** You are asking if it is possible to drive **3 x 1080p** displays from the **2 DisplayPort** outputs on your AMD Radeon RX 7700 XT and how this can be achieved.

### Yes, it is possible to drive **3 x 1080p** displays from the 2 DisplayPort outputs on your card. Here’s how you can achieve that:

### 1. **Use DisplayPort Daisy-Chaining (Multi-Stream Transport - MST):**
   - **DisplayPort 1.2 and higher** (your RX 7700 XT has DisplayPort 2.1) supports **MST (Multi-Stream Transport)**, which allows multiple displays to be connected in a daisy-chain configuration from a single DisplayPort output.
   - **How to Set It Up**:
     - Ensure your monitors support **DisplayPort Daisy-Chaining** (MST).
     - Connect the first monitor to the GPU's DisplayPort output.
     - Then, connect the second monitor to the **DisplayPort output** of the first monitor.
     - You can then connect the third monitor either to the second DisplayPort on the GPU or via MST if the monitors and cables support it.
   - **Limitations**:
     - MST typically supports up to **4 monitors** in a daisy-chain, but each monitor must be compatible with MST, and the total bandwidth must be sufficient for the resolution and refresh rate you are using (e.g., 1080p at 60Hz is easily supported by DP 2.1).

### 2. **Use a DisplayPort MST Hub:**
   - If your monitors do not support daisy-chaining, you can use an **MST hub**. This device splits one DisplayPort output into multiple outputs.
   - **How to Set It Up**:
     - Connect an **MST hub** to one of the DisplayPort outputs on your GPU.
     - The MST hub will provide multiple DisplayPort outputs (usually 3 or more).
     - Connect each of your 1080p monitors to the hub.
   - **MST Hub Example**:
     - You could use something like the **Club 3D DisplayPort 1.4 MST Hub**, which supports multiple 1080p displays via a single DP connection.

### Conclusion:
To drive **3 x 1080p** displays using only the **2 DisplayPort outputs**:
1. **Daisy-chain** your displays if they support **MST**.
2. Use a **DisplayPort MST hub** if the monitors do not support daisy-chaining.

Either solution will allow you to drive three 1080p displays from the two DP ports on your AMD Radeon RX 7700 XT.