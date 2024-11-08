---
title: "Seeking better custom OS creation tools"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Getting closer to what I'm looking for. But no tools like these that I can download and run myself?

# Output

You're right, we're getting closer to what you're looking for. There are indeed tools you can download and run yourself to create custom OS images. One particularly relevant option for your Fedora-based system is Fedora's own Image Builder tool. Here's some information about it:

## Fedora Image Builder

Fedora Image Builder is a set of modern tools designed specifically for building operating system images, including custom Fedora Workstation live ISOs[1]. This tool aligns perfectly with your goal of creating a customized Fedora-based OS image.

Key features and benefits:

1. Designed for reliability and reproducibility
2. Provides a simple workflow for end users to build custom images
3. Uses TOML blueprint files for configuration, which are more user-friendly than traditional kickstart files
4. Offers both CLI and graphical interfaces for defining blueprints

To use Fedora Image Builder:

1. Install the necessary packages (likely `osbuild-composer` and related tools)
2. Create a blueprint file defining your customizations
3. Use the CLI or GUI to build your custom image based on the blueprint

This tool is actively being developed and integrated into Fedora's build process, making it an excellent choice for your needs.

## Other Options

If you want to explore alternatives, here are a couple more options you can download and run yourself:

1. Diskimage-builder: This is an automated disk image creation tool that supports Fedora and other distributions[2]. You can install it and run it locally to create custom images.

2. Packer: While not specific to Fedora, Packer is a versatile tool for creating machine images across multiple platforms. It can be used to create custom Fedora images as well.

These tools allow you to create custom OS images on your local machine, giving you full control over the process and the ability to fine-tune your customizations. They're more aligned with your goal of creating a replicable custom OS image than the disaster recovery or cloning tools mentioned earlier.

 