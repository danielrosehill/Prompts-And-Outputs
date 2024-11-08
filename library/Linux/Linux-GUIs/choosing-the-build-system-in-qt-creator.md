---
title: "Choosing the build system in Qt Creator"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

![[Choosing the build system in Qt Creator.png]]

# Output

In your image, you have the options of **CMake**, **qmake**, and **Qbs** as build systems in Qt Creator.

Here’s a quick guide to help you decide:

### 1. **CMake (Recommended)**
   - **Why Choose CMake**: 
     - **Modern and Flexible**: CMake is widely adopted and considered more modern and flexible than qmake. It's also better supported by newer versions of Qt, and many open-source projects are transitioning to CMake for this reason.
     - **Cross-Platform**: CMake is cross-platform, making it easier to port your application to different operating systems if needed.
     - **Better Tooling**: Many tools (IDEs, CI/CD pipelines, etc.) have better integration with CMake.

   - **When to Use**: If you’re planning on long-term maintenance or contributing your project to a larger community, CMake is a good choice. It also gives more control over complex build configurations and is more future-proof as Qt continues to evolve.

### 2. **qmake**
   - **Why Choose qmake**: 
     - **Simplicity**: If you're looking for something quick and simple, qmake is a good choice. It's the traditional build system for Qt projects and may be easier for basic applications.
     - **Qt Focused**: While less flexible than CMake, qmake is tightly integrated with Qt, which can simplify some workflows for smaller projects.
     
   - **When to Use**: Choose this if you are focusing on a simpler, quick-to-setup project, or if you are already familiar with qmake from previous Qt projects.

### 3. **Qbs**
   - **Why Choose Qbs**: 
     - **Experimental**: Qbs was introduced by Qt for certain specific use cases but was eventually deprecated by Qt in 2020.
     - **Discontinued**: Qt no longer maintains or promotes Qbs, so it's not recommended for new projects.
     
   - **When to Use**: It's generally not recommended for new projects, as it’s deprecated and lacks long-term support.

### **Recommendation**:
Go with **CMake**, as it’s modern, flexible, and better integrated with future Qt developments. It will also give you more flexibility and scalability for your project as it grows.