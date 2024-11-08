---
title: "Header and footer text on exported PDFs from Obsidian"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

In Obsidian, I would love to be able to add some boilerplate header and footer text whenever I export a note to PDF. Any extensions that can do this?

# Output
To add boilerplate **header and footer** text when exporting a note to PDF in **Obsidian**, there are a few options, though there's no direct plugin designed exclusively for this. However, with **CSS** and **Markdown Export Customization**, you can achieve this functionality.

### Option 1: **Use Custom CSS**
You can customize the export using **custom CSS** to add headers and footers to your PDFs. This approach uses Obsidian’s ability to apply custom styles when exporting notes.

#### Steps:
1. **Enable Custom CSS in Obsidian**:
   - Go to **Settings** > **Appearance** and ensure **CSS Snippets** are enabled.

2. **Create a CSS Snippet**:
   - Create a file in your Obsidian vault’s `.obsidian/snippets/` folder (create the folder if it doesn’t exist), for example: `pdf-header-footer.css`.

3. **Add CSS for Header and Footer**:
   - Add the following CSS to control the header and footer when exporting to PDF:
     ```css
     /* Custom header for PDF export */
     @page {
         margin-top: 4cm; /* Adjust margin to leave space for the header */
     }
     @page::before {
         content: "Your Header Text Here";
         display: block;
         position: running(header);
         font-size: 12px;
         text-align: center;
         margin-bottom: 10px;
     }

     /* Custom footer for PDF export */
     @page::after {
         content: "Your Footer Text Here - Page " counter(page);
         display: block;
         position: running(footer);
         font-size: 12px;
         text-align: center;
         margin-top: 10px;
     }
     ```

4. **Activate the Snippet**:
   - Go to **Settings** > **Appearance** > **CSS Snippets**, and activate your new snippet (`pdf-header-footer.css`).
   
5. **Export the Note to PDF**:
   - When you export a note to PDF, the header and footer text will be added automatically.

#### Pros:
- Full control over styling, headers, and footers.
- Can be adjusted to fit your specific needs.

#### Cons:
- Requires some understanding of CSS.
- Limited to static content (i.e., no dynamic note titles or metadata).

### Option 2: **Pandoc + Custom Template for PDF Export**
If you want more advanced customization, including dynamic headers and footers, you can use **Pandoc** for exporting your notes. Pandoc allows the use of LaTeX templates, which can include headers, footers, and other custom formatting.

#### Steps:
1. **Install Pandoc**:
   - On Fedora, install Pandoc:
     ```bash
     sudo dnf install pandoc
     ```

2. **Create a Pandoc Template**:
   - Create a custom LaTeX template with the desired header and footer content. For example:
     ```latex
     \documentclass{article}
     \usepackage{fancyhdr}
     \pagestyle{fancy}
     \fancyhead[L]{Your Header Text}
     \fancyfoot[C]{Your Footer Text - Page \thepage}

     \begin{document}
     $body$
     \end{document}
     ```

3. **Export the Note Using Pandoc**:
   - In Obsidian, export your note to Markdown, and then run Pandoc to convert it to a PDF with your custom template:
     ```bash
     pandoc note.md -o note.pdf --template=your-template.tex
     ```

#### Pros:
- Allows for dynamic content (e.g., note titles, page numbers, etc.).
- Full customization of headers, footers, and layout.

#### Cons:
- Requires external tools and manual processing.
- Involves more setup.

### Option 3: **Templater Plugin for Custom Export**
You can use **Templater** in conjunction with Obsidian’s PDF export to insert custom header and footer text dynamically into your Markdown before exporting.

#### Steps:
1. **Install Templater Plugin**:
   - Go to **Settings** > **Community Plugins** > Search for **Templater** and install it.

2. **Create a Template**:
   - Create a template that inserts a header and footer at the top and bottom of each note, which will be included in the PDF export. For example:
     ```markdown
     ---
     Title: <% tp.file.title %>
     Date: <% tp.date.now("YYYY-MM-DD") %>
     ---

     # Header
     This document was exported on <% tp.date.now("YYYY-MM-DD") %>.

     %% Your note content will go here %%

     ---
     # Footer
     Confidential - For internal use only.
     ```
   
3. **Apply the Template**:
   - Apply the template to the note you want to export, and then export the note as PDF.

#### Pros:
- Works directly within Obsidian.
- Allows for dynamic content insertion (e.g., note titles, dates, etc.).

#### Cons:
- Headers and footers are part of the note content, not true page-level headers/footers.
  
### Conclusion:
- **Custom CSS** is the easiest solution if you're comfortable with styling, as it integrates seamlessly into Obsidian's PDF export.
- **Pandoc** offers the most flexibility, especially if you want dynamic headers and footers based on the content of the note.
- **Templater** provides a quick solution for inserting headers and footers within the note itself.

Let me know if you'd like more help with any of these approaches!