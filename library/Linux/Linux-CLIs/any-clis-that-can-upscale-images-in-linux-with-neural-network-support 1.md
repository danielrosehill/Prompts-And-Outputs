---
title: "Any CLIs that can upscale images in Linux with neural network support?"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


You asked if there is a CLI for Linux that can both rescale an image to match a target paper size and intelligently upscale without losing quality.

Yes, there are several command-line tools on Linux that can help you achieve both tasks:

1. **ImageMagick**:
   - **Rescale to match a target paper size**: ImageMagick can rescale images to specific dimensions that correspond to common paper sizes (like A4, Letter, etc.).
   - **Intelligent upscaling**: ImageMagick supports several resampling filters (such as `Lanczos` and `Mitchell`) which help upscale images with minimal quality loss.

   To rescale and upscale:
   ```
   convert input_image.jpg -resize 2480x3508 -filter Lanczos output_image.jpg
   ```
   This example resizes to A4 size at 300 DPI (2480x3508 pixels).

2. **waifu2x (waifu2x-converter-cpp)**:
   - This tool specializes in intelligent upscaling, particularly using neural networks. While primarily designed for anime-style images, it works well on other image types too.
   - You can combine it with ImageMagick: first use ImageMagick to rescale, and then waifu2x to upscale the image.

   Example usage:
   ```
   waifu2x-converter-cpp --scale 2 -i input_image.jpg -o output_image_upscaled.jpg
   ```
   This upscales the image by 2x with intelligent noise reduction.

You can combine the two tools in a workflow to meet your needs, ensuring both the right paper size and intelligent upscaling for high-quality output.