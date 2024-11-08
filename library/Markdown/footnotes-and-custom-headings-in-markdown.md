---
title: "Footnotes and custom headings in markdown"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Prompt Summary:** You asked how to add footnotes in Markdown documents in Obsidian, and whether it's possible to add headers for inclusion during PDF export.

---

### 1. **Adding Footnotes in Obsidian:**
   Obsidian supports footnotes via the standard Markdown syntax. Here's how you can add them:

   - **Footnote Syntax:**
     ```markdown
     Here's some text with a footnote.[^1]

     [^1]: This is the content of the footnote.
     ```

   When exporting to PDF, the footnotes will be automatically formatted at the bottom of the page or section, depending on how you're exporting the document.

---

### 2. **Adding Headers for PDF Export:**
   To include headers and footers during a PDF export in Obsidian, you can make use of the CSS `@media print` rules to customize the look of your documents. However, this requires custom CSS setup:

   - **Steps for Adding a Header in PDF Export:**
     1. **Enable Custom CSS**: First, ensure you have the **Custom CSS** feature enabled in Obsidian.
     2. **Create a CSS Snippet**: Create a file named `header-print.css` in the Obsidian vault's `.obsidian/snippets` directory. If the directory doesn't exist, you can create it manually.

     - Sample CSS to include headers in PDF:
       ```css
       @media print {
           @page {
               margin: 20mm;
           }
           header {
               position: fixed;
               top: 0;
               left: 0;
               right: 0;
               height: 20mm;
               text-align: center;
               font-size: 12pt;
               font-weight: bold;
           }
           body {
               padding-top: 30mm;
           }
       }
       ```

     3. **Activate the Snippet**: Go to **Settings** → **Appearance** → **CSS Snippets** and enable the `header-print.css` snippet.

Now, your exported PDFs will have a header section.

Let me know if you need further details on any step!