---
title: "Pixel offsets for 3 screen display"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I have 3 displays on my computer. Each display is 1920 x 1080.
Could you calculate a couple of pixels for me so that I don't need to remember them?
Firstly to align a program in full screen on the 2nd display, what offset do I need?
Likewise for the right screen

# Output

Given that each of your displays is 1920x1080, we can calculate the X offsets for positioning windows on the second and third displays.

- **Left display (Primary)**: Starts at X = 0.
- **Second display (Middle)**: Starts at X = 1920 (since the first display is 1920 pixels wide).
- **Right display (Third)**: Starts at X = 3840 (since it comes after two 1920 pixel wide displays).

### Summary of Offsets:
- **Left (Primary) Display**: X = 0
- **Second (Middle) Display**: X = 1920
- **Right (Third) Display**: X = 3840

### Full-Screen Window Placement:
- To position a window on the **second (middle) display** in full screen: use the offset X = 1920.
- To position a window on the **third (right) display** in full screen: use the offset X = 3840.

You can now use these offsets when adjusting window placement in your script. For example:

- For the second display: `wmctrl -ir <window_id> -e 0,1920,0,1920,1080`
- For the right display: `wmctrl -ir <window_id> -e 0,3840,0,1920,1080`

Let me know if you need further assistance with this!

# Input

Great. And if I wanted to put two programs on the third (right) screen, dividing that display equally, what would the offsets for those two programs be?

# Output

If you want to divide the **third (right) display** equally between two programs, you'll be splitting its width of 1920 pixels in half, so each program will have a width of 960 pixels.

Here are the offsets for placing two programs side by side on the third screen:

### Program 1 (Left half of the third screen):
- **X offset**: 3840 (the start of the third screen).
- **Width**: 960 pixels.
- **Command**:
  ```bash
  wmctrl -ir <window_id> -e 0,3840,0,960,1080
  ```

### Program 2 (Right half of the third screen):
- **X offset**: 3840 + 960 = 4800.
- **Width**: 960 pixels.
- **Command**:
  ```bash
  wmctrl -ir <window_id> -e 0,4800,0,960,1080
  ```

### Summary of Offsets:
- **Left half of the third screen**: X = 3840, Width = 960.
- **Right half of the third screen**: X = 4800, Width = 960.

You can use these values to place two windows on the right screen in a 50:50 split. Let me know if you need further adjustments!