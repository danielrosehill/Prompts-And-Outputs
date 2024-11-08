---
title: "Creating galleries in Github repos"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I would like to add a gallery of screenshots to a readme page on Github. Is there any way to emulate something like a "gallery view"? I am trying to find a smarter way of adding them in VS Code than dragging and dropping them one by one into a markdown doc

# Prompt Image

![[Creating galleries in Github repos.png]]

# Output

To create a gallery-like view of screenshots in your GitHub README, you can use a combination of HTML and Markdown. This approach allows for more flexibility in layout and presentation compared to standard Markdown. Here's a method to achieve this:

## Creating a Gallery View in GitHub README

1. First, upload your screenshots to your repository. Based on the image provided, it seems you have a "Screenshots" folder with numbered PNG files.

2. In your README.md file, you can use HTML tables to create a grid-like structure for your images. Here's an example of how you can structure it:

```html
<table>
  <tr>
    <td><img src="Screenshots/1.png" width="200"/></td>
    <td><img src="Screenshots/2.png" width="200"/></td>
    <td><img src="Screenshots/3.png" width="200"/></td>
  </tr>
  <tr>
    <td><img src="Screenshots/4.png" width="200"/></td>
    <td><img src="Screenshots/5.png" width="200"/></td>
    <td><img src="Screenshots/6.png" width="200"/></td>
  </tr>
</table>
```

This will create a 2x3 grid of images. Adjust the number of `<tr>` (table rows) and `<td>` (table cells) as needed for your gallery layout[3].

3. To make this process more efficient in VS Code, you can use some tricks:

   - Use VS Code's multi-cursor editing: Hold Alt (Option on Mac) and click to add multiple cursors, then type the repetitive parts of the HTML structure.
   - Use snippets: Create a custom snippet in VS Code for your gallery structure, which you can quickly insert and modify.
   - Use the "Markdown: Insert Image from Workspace" command in VS Code to quickly insert image paths[2].

4. For a more dynamic approach, you could write a simple script to generate the HTML for your gallery based on the files in your Screenshots folder. This script could be run locally to generate the HTML, which you then paste into your README.md.

5. If you want to make the images clickable to view larger versions, you can wrap each `<img>` tag in an anchor tag:

```html
<td><a href="Screenshots/1.png"><img src="Screenshots/1.png" width="200"/></a></td>
```

This approach allows you to create a visually appealing gallery-like view in your README while maintaining flexibility in layout and presentation. It's more efficient than dragging and dropping images one by one, especially when combined with VS Code's editing features[1][2].

Remember that while this method uses HTML within your Markdown file, GitHub's Markdown renderer supports this mixed approach, allowing you to create more complex layouts when needed[4].

 




## Extracted Prompts
[[Prompts/Creating galleries in Github repos.md#Prompt 1|Prompt 1]]
