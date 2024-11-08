---
title: "Image generation GUIs for AI programs"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Summary of the prompt:** You are asking for recommendations of image generation programs with **GUIs** that are compatible with **Fedora**.

Here are some of the best **GUI-based image generation programs** for **Fedora Linux**:

### **1. InvokeAI**
**InvokeAI** is one of the most popular GUI-based tools for **Stable Diffusion** and other AI image generation models. It provides a simple interface for text-to-image generation and image manipulation.

#### **Features**:
- User-friendly **web-based GUI** and **command-line interface** (CLI).
- Supports **inpainting**, **outpainting**, and **image editing**.
- Local installation ensures you don’t need to rely on cloud-based services.
- **Stable Diffusion** support for generating high-quality images.

#### **Installation on Fedora**:
InvokeAI is a Python-based tool that runs on Fedora.
1. Install Python 3 and dependencies:
   ```bash
   sudo dnf install python3 python3-pip git
   ```

2. Clone the InvokeAI repository and set it up:
   ```bash
   git clone https://github.com/invoke-ai/InvokeAI.git
   cd InvokeAI
   pip install -r requirements.txt
   ```

3. Run the application and access the GUI via your browser:
   ```bash
   python3 scripts/invoke.py --web
   ```

#### **Use Case**:
InvokeAI is perfect if you are looking for a **fully local image generation tool** that allows you to experiment with different models and do image editing as well.

#### **Link**:
- [InvokeAI GitHub](https://github.com/invoke-ai/InvokeAI)

---

### **2. **Automatic1111 Stable Diffusion Web UI**

The **Stable Diffusion Web UI** by Automatic1111 is a powerful **local GUI-based interface** for working with **Stable Diffusion**. It offers a wide range of features, including text-to-image generation, inpainting, outpainting, and image editing.

#### **Features**:
- Fully customizable **local GUI** for generating images.
- Supports **inpainting**, **outpainting**, and **upscaling**.
- Highly configurable with many different models and settings.
- Works entirely offline after installation.

#### **Installation on Fedora**:
1. Install necessary dependencies:
   ```bash
   sudo dnf install python3 python3-pip git
   ```

2. Clone the repository and install the required packages:
   ```bash
   git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
   cd stable-diffusion-webui
   pip install -r requirements.txt
   ```

3. Run the UI:
   ```bash
   python launch.py
   ```

4. Access the GUI in your browser at `http://localhost:7860`.

#### **Use Case**:
This tool is ideal if you want a **fully featured, highly customizable GUI** for Stable Diffusion and AI image generation on Fedora, offering both casual use and deep customization.

#### **Link**:
- [Stable Diffusion Web UI GitHub](https://github.com/AUTOMATIC1111/stable-diffusion-webui)

---

### **3. DiffusionBee (Linux Alternative: InvokeAI)**

**DiffusionBee** is popular on macOS, but for Fedora Linux, the best alternative would be **InvokeAI**, which provides similar functionality for **Stable Diffusion** with a GUI. Since InvokeAI has been mentioned earlier, DiffusionBee doesn’t directly support Linux.

---

### **4. GIMP with Plugins (For Image Editing and Generation)**

While **GIMP** itself is a general-purpose image editing tool, you can use it in combination with **AI-based plugins** to add **image generation capabilities**.

#### **Features**:
- Extensive plugin support for AI-based tools, including **deep learning-based super-resolution** and **style transfer**.
- Useful for both manual image editing and AI-assisted image generation.

#### **Installation on Fedora**:
1. Install GIMP:
   ```bash
   sudo dnf install gimp
   ```

2. Add AI plugins like **G’MIC** (General Image Manipulation Collection):
   - Install G'MIC:
     ```bash
     sudo dnf install gmic gimp-gmic
     ```

3. Use the **G'MIC** plugin for AI-based image processing.

#### **Use Case**:
GIMP is a great choice if you want a versatile image editor with some **AI-powered enhancements** for generating artistic images or improving the quality of images.

#### **Link**:
- [GIMP](https://www.gimp.org/)

---

### **5. **Artbreeder (Web-based AI Art Generator)**

**Artbreeder** is a web-based AI image generation tool that lets users create images by combining or "breeding" images. While it is not a local application, it runs smoothly on Linux through any browser and offers a fun, visual interface for creating AI-generated art.

#### **Features**:
- Browser-based, so no need for installation.
- Allows mixing and evolving images using **AI models**.
- Supports fine-tuning parameters like face generation, landscapes, and abstract art.

#### **Use Case**:
Artbreeder is ideal if you are looking for a **lightweight and creative** tool that runs directly in your browser on Fedora, without needing any heavy installations.

#### **Link**:
- [Artbreeder](https://www.artbreeder.com/)

---

### **Conclusion**:

For **GUI-based AI image generation** on Fedora, here are your best options:

- **InvokeAI** and **Stable Diffusion Web UI** are the top choices for **locally running GUIs** with powerful image generation capabilities.
- **GIMP** with plugins like **G'MIC** offers a more general image editor with AI enhancements.
- For quick and lightweight image generation, **Artbreeder** is a web-based tool that runs perfectly in a Fedora browser.

Each of these options provides different features, so you can choose the one that best suits your needs for AI-powered image creation on Fedora.