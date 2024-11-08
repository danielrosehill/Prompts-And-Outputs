---
title: "VS Code extensions for converting markdown"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Summary of the prompt:** You are asking if there is a VS Code extension that can convert markdown to PDF with nice formatting.

Yes, there are several **VS Code extensions** and tools that can convert markdown to PDF with enhanced formatting. Here are some of the best options:

### **1. Markdown PDF**

The **Markdown PDF** extension allows you to easily convert markdown files to PDF, with options to customize formatting.

#### **Features**:
- Converts markdown to PDF, HTML, PNG, and JPEG.
- Supports **custom stylesheets** for more control over formatting (e.g., fonts, margins, page breaks).
- Table of contents generation and support for images, links, and tables.

#### **How to Use**:
1. **Install the Extension**: Search for **Markdown PDF** in the VS Code extensions marketplace and install it.
   - [Markdown PDF Extension](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf)

2. **Convert Markdown to PDF**:
   - Open your markdown file in VS Code.
   - Right-click on the editor and choose **Markdown PDF: Export (pdf)** from the context menu.

3. **Custom CSS**: You can customize the look of the generated PDF by adding a custom stylesheet. Add a CSS file and reference it in the extension’s settings.

#### **Formatting Customization**:
- You can apply custom CSS styles for more advanced formatting by editing the `markdown-pdf.styles` setting in the VS Code configuration.
- Example: Add custom CSS in your settings JSON.
   ```json
   "markdown-pdf.styles": [
       "file:///path/to/custom.css"
   ]
   ```

### **2. Markdown Preview Enhanced**

**Markdown Preview Enhanced** is another powerful extension that provides advanced markdown rendering and exporting capabilities.

#### **Features**:
- Export to **PDF**, **HTML**, **Pandoc**, and **LaTeX**.
- Advanced markdown features like **diagrams**, **LaTeX equations**, and **charts**.
- **Customizable styling** using a stylesheet (CSS).
- Supports **mermaid diagrams**, **flowcharts**, **math rendering**, and more.

#### **How to Use**:
1. **Install the Extension**: Search for **Markdown Preview Enhanced** in the marketplace and install it.
   - [Markdown Preview Enhanced Extension](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced)

2. **Preview and Export**:
   - Open your markdown file.
   - Press `Ctrl+Shift+V` to open the **preview**.
   - In the preview window, click the **export icon** and select **PDF**.

3. **Custom CSS**: Like Markdown PDF, this extension allows you to use custom CSS for your PDF export.

#### **Extra Features**:
- Supports **exporting code snippets with syntax highlighting**.
- Allows customization through **Pandoc** for even more advanced conversions (e.g., footnotes, bibliography).

### **3. Pandoc with VS Code**

**Pandoc** is an external tool that can be integrated with VS Code to convert markdown to PDF with extensive formatting options, including LaTeX support for high-quality PDF outputs.

#### **How to Use**:
1. **Install Pandoc**: Download and install **Pandoc** from [pandoc.org](https://pandoc.org/installing.html).

2. **Run Pandoc Command**:
   - From the VS Code terminal, use Pandoc to convert your markdown file to PDF:
     ```bash
     pandoc input.md -o output.pdf
     ```

3. **Customization**:
   - You can use **custom CSS** or **LaTeX** templates to style the PDF.
   - Example with a custom LaTeX template:
     ```bash
     pandoc input.md -o output.pdf --pdf-engine=xelatex --template=mytemplate.tex
     ```

#### **Features**:
- **Highly customizable**: You can control nearly every aspect of the PDF output, including fonts, margins, and sections.
- **LaTeX support**: For high-quality typesetting and precise control over the output.

---

### **Conclusion**:
For easy markdown-to-PDF conversion with nice formatting:
- **Markdown PDF** is simple to use and allows basic styling via custom CSS.
- **Markdown Preview Enhanced** provides more advanced features like diagrams, LaTeX, and customizable PDF exports.
- For the most control, **Pandoc** combined with LaTeX or custom CSS gives professional-grade PDF outputs but requires more setup.

Each of these options provides excellent ways to create well-formatted PDFs directly from VS Code.