---
title: "Closest things to AutoCAD that run on Linux"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

My wife uses AutoCAD, Revit, and Rhino (she is an architect). I think she uses mostly AutoCAD and Rhino and wants to start using Revit more. What do each of these do? And what are the closest things that exist in the Linux universe and which could run on Fedora?

# Output

Here’s a breakdown of the tools your wife uses and their closest alternatives in the Linux universe, especially ones that could run on Fedora.

### **1. AutoCAD**
   - **What It Does**: AutoCAD is a widely used tool for 2D and 3D computer-aided design (CAD) and drafting. Architects use it to create detailed floor plans, blueprints, technical drawings, and architectural renderings. It's highly versatile and supports precise design work.
   - **Linux Alternatives**:
     - **BricsCAD**: A commercial alternative to AutoCAD, BricsCAD has a native Linux version and is fully compatible with AutoCAD’s .dwg file format. It’s a good solution if AutoCAD-like features are needed.
       - **Installation**: Available for Fedora via `.rpm` packages.
     - **LibreCAD**: An open-source 2D CAD tool that provides basic drafting functionalities similar to AutoCAD, but it lacks the robust 3D modeling features AutoCAD has.
     - **FreeCAD**: A more complex, open-source 3D CAD tool. FreeCAD is used for parametric modeling and engineering designs but may require some time to adapt to its workflow compared to AutoCAD.
       - **Installation**: Available via Fedora repositories.

### **2. Rhino**
   - **What It Does**: Rhino is a powerful tool primarily used for freeform 3D modeling. Architects and designers use it for creating complex, organic shapes and detailed surface modeling. It’s particularly popular for architectural design, industrial design, and 3D printing.
   - **Linux Alternatives**:
     - **Blender**: A powerful open-source 3D modeling and rendering tool. While Blender is mainly known for animation and visual effects, it’s also highly capable for 3D modeling tasks, including architectural work. With some tweaks, it can work as an alternative to Rhino.
       - **Installation**: Available via Fedora repositories.
     - **FreeCAD**: While not as robust for freeform modeling as Rhino, FreeCAD does have some features that make it a viable alternative for certain 3D modeling tasks.
     - **Modo (via Wine)**: Modo is a 3D modeling software used for similar tasks as Rhino. While it doesn’t have a Linux version, you could potentially run it via Wine (though with limitations).

### **3. Revit**
   - **What It Does**: Revit is a Building Information Modeling (BIM) software used by architects for designing buildings, structures, and infrastructure in 3D. Revit focuses on architectural workflows, allowing users to create and manage building models, plans, and schedules.
   - **Linux Alternatives**:
     - **FreeCAD (with BIM Workbench)**: FreeCAD has a dedicated **BIM Workbench** for architectural design and building modeling. While it’s not as advanced as Revit, it offers many BIM features that could work as an open-source alternative.
     - **BIMserver**: A server-side BIM application that allows for collaborative building model work. It’s more of a backend service but could be combined with FreeCAD or other tools to create a Revit-like workflow.
     - **ArchiCAD (via Wine or Virtualization)**: ArchiCAD is another BIM tool comparable to Revit, but it doesn’t natively support Linux. You could try running it through **Wine** or using a virtual machine.

### **Best Solutions for Running These on Fedora**:
- **Virtualization**: If your wife needs to use the exact versions of AutoCAD, Rhino, or Revit, you could consider running them on a virtual machine (e.g., using **QEMU/KVM** or **VirtualBox**) with Windows as the guest OS. This will allow her to run the software while still using Fedora as her base system.
- **Wine/Proton**: Some Windows-based CAD applications may work through **Wine** or **Proton** (from Steam), but performance might vary. **Rhino** and **AutoCAD** have varying degrees of compatibility in Wine, though they are not officially supported.
- **Dual-Boot**: If high performance and full features are necessary, dual-booting with Windows and Linux is another solution. She could use Linux for general work and Windows for architecture design when needed.

Let me know if you'd like more detailed guides for installation or tips for using these alternatives on Fedora!