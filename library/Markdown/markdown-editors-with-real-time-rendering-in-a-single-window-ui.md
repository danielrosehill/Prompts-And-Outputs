---
title: "Markdown editors with real time rendering in a single window UI"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I should have clarified that I'm not looking for side by side preview. I don't like those UIs. Any other tools I can integrate into my frontend that would provide the same kind of real time markdown rendering that obsidian offers?

# Output

If you're looking for tools that provide **real-time markdown rendering** in the same document (without side-by-side preview) like Obsidian does, there are a few excellent editor options that support WYSIWYG markdown rendering while hiding the underlying markdown syntax once it's rendered:

### 1. **TipTap Editor (Advanced, Customizable)**
   - **Description**: TipTap is an excellent WYSIWYG editor built on **ProseMirror**, which allows rich customization for markdown handling and instant rendering. It supports markdown input but converts it to rich text on the fly, similar to how Obsidian operates.
   - **How it works**: You can configure TipTap with plugins to handle markdown syntax parsing as you type, displaying it immediately as rich text. It doesn’t show the raw markdown once rendered, providing the clean experience you're looking for.
   - **Customization**: You can modify it to show or hide markdown as needed, and integrate it into your frontend easily.
   - **Integration**: Great for building custom workflows with support for markdown-rich text conversion.
   
   **[TipTap Documentation](https://tiptap.dev)**

### 2. **Slate.js (Customizable WYSIWYG)**
   - **Description**: **Slate.js** is another highly customizable rich-text editor framework. You can extend it to provide real-time markdown rendering as you type, converting markdown into styled text instantly.
   - **How it works**: Slate.js is more of a building block that allows you to control exactly how text is rendered, giving you the power to hide the markdown syntax once it's interpreted into rich text.
   - **Customization**: You'll need to manually handle markdown parsing (with libraries like `remark` or `markdown-it`), but it can be tailored to provide a fully WYSIWYG experience without side-by-side views.
   
   **[Slate.js Documentation](https://docs.slatejs.org)**

### 3. **Milkdown**
   - **Description**: **Milkdown** is a markdown editor that supports real-time WYSIWYG rendering. It hides the underlying markdown as it is parsed and rendered into rich text. It's highly configurable and can be adapted to behave much like Obsidian's markdown handling.
   - **How it works**: Milkdown renders markdown into rich text directly as you write, without showing the markdown syntax, similar to a live preview within the same document. It is built with flexibility and extensibility in mind, making it easy to integrate.
   - **Customization**: Offers deep customization to match your exact editing needs and can be embedded into any frontend.
   
   **[Milkdown Documentation](https://milkdown.dev/)**

### 4. **Remirror**
   - **Description**: **Remirror** is another rich text editor built with ProseMirror under the hood, similar to TipTap. It can handle markdown input and convert it into rich text in real time.
   - **How it works**: You can use Remirror’s markdown extension to handle markdown input and instantly convert it into formatted rich text, mimicking the WYSIWYG behavior of Obsidian.
   - **Integration**: Easy to integrate into modern web applications and customizable for various use cases.
   
   **[Remirror Documentation](https://remirror.io/)**

### 5. **Codemirror 6 (Markdown Mode)**
   - **Description**: While **Codemirror** is often known as a code editor, its new version (**Codemirror 6**) has a markdown mode that can render markdown live without showing raw syntax. It can be configured to behave more like a WYSIWYG editor.
   - **How it works**: Codemirror 6 can be extended with plugins to offer real-time markdown rendering, and with some customization, it can hide the raw markdown syntax from the user.
   
   **[Codemirror 6 Documentation](https://codemirror.net/)**

### Summary:
If you're looking for Obsidian-like real-time markdown rendering with a WYSIWYG experience (where markdown is hidden once rendered), **TipTap**, **Milkdown**, and **Slate.js** are strong candidates. **TipTap** is particularly well-suited for more complex integrations and rich markdown handling. **Milkdown** is simpler to configure for immediate WYSIWYG rendering and is highly intuitive.

These tools offer flexibility, rich text rendering, and markdown support without needing to rely on side-by-side previews.