---
title: "What is Obsidian running that makes it so great at handling markdown"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


You mentioned that Obsidian offers excellent markdown support with instant rendering and WYSIWYG-like interaction. Here's a breakdown of what’s happening under the hood in tools like Obsidian and which text entry tools can offer similar functionality.

### How Obsidian Handles Markdown:
1. **Dual-Mode Rendering**: Obsidian allows you to write in markdown while simultaneously rendering it in a rich text (WYSIWYG) format. This is done using **HTML and CSS** to interpret the markdown and style it appropriately in real time.
   
   - **Markdown Parsing**: When you write in markdown, Obsidian's underlying system uses a **markdown parser** (like `markdown-it` or similar libraries) that converts markdown syntax (e.g., `**bold**`, `# header`, etc.) into HTML as soon as it is written.
   
   - **WYSIWYG-Like Editor**: The HTML generated from markdown is displayed in a way that looks and behaves like a traditional text editor, thanks to a combination of CSS and JavaScript. For example:
     - `# Heading 1` becomes a large heading.
     - `**Bold**` text is immediately rendered as bold text.
   
   - **Instant Rendering**: Every time you modify the content, the editor refreshes the rendered view in real time, which provides the "instant" WYSIWYG effect. This doesn’t alter the underlying markdown but shows it in a human-friendly format.

2. **Rich Text + Markdown Editing**: While working in Obsidian, you can seamlessly switch between writing raw markdown and interacting with the rendered content (clicking links, toggling checkboxes, etc.). This is achieved by keeping the rendered and raw markdown synced in real-time.

### Which Tools Can Offer Similar Functionality?

Here are the text entry tools I mentioned earlier, with a focus on their markdown support and potential for WYSIWYG-like functionality similar to Obsidian:

#### 1. **TipTap Editor**
   - **Why it's similar**: TipTap is built on **ProseMirror**, which is a robust framework for rich text editing that can handle markdown. It offers extensive customization and can support real-time markdown rendering through plugins and extensions.
   - **How to configure**: You can configure it to handle markdown input and display it as rich text instantly. This would involve setting up a markdown parser (like `markdown-it`) and linking it with TipTap’s editor state to provide WYSIWYG-like rendering.
   - **Flexibility**: It’s highly flexible and designed to be integrated into modern web apps, making it ideal for projects where you need full control over how markdown is processed and rendered.

#### 2. **SimpleMDE (Simple Markdown Editor)**
   - **Why it's similar**: SimpleMDE is a **markdown editor with built-in preview** capabilities. While less powerful than Obsidian, it offers a side-by-side markdown writing and preview mode.
   - **How to configure**: SimpleMDE renders markdown in real-time as you write, allowing for immediate feedback, similar to Obsidian’s real-time rendering, though not with full WYSIWYG interaction.
   - **Limitations**: It’s more basic and might require custom development if you want deeper WYSIWYG functionality like Obsidian offers.

#### 3. **StackEdit**
   - **Why it's similar**: StackEdit is a **browser-based markdown editor** with live preview capabilities. It allows for instant markdown rendering as you type, much like Obsidian.
   - **How to configure**: It provides an automatic markdown-to-rich-text conversion out of the box. You can use it directly or customize it for integration with your backend.
   - **Limitations**: It’s a standalone tool that might not be as customizable for integration into custom workflows as TipTap.

#### 4. **Editor.js**
   - **Why it's similar**: Editor.js is a block-based editor that allows customization through plugins, including markdown support. With plugins, you can add markdown input and rich text rendering.
   - **How to configure**: You would need to write or integrate a markdown parser to handle instant rendering of markdown input into rich text. While it can handle markdown blocks, the WYSIWYG experience may require additional customization.
   - **Limitations**: Its focus on block editing makes it different from traditional markdown editors like Obsidian, though it can be configured to offer some markdown-to-rich-text conversion.

### Summary
If you're looking to replicate Obsidian’s markdown functionality with real-time rendering, **TipTap Editor** offers the closest flexibility and customization to build an editor with WYSIWYG markdown support. It’s highly configurable, allows for markdown rendering, and can be extended with plugins to achieve a similar experience. **SimpleMDE** and **StackEdit** are also good lightweight alternatives, but they offer less customization compared to TipTap.

**Under the hood**, tools like Obsidian work by parsing markdown to HTML instantly and using CSS and JavaScript to manage real-time rich text rendering. The key to replicating this lies in using a solid markdown parser and a flexible editor framework like TipTap.