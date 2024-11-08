---
title: "How to make an Obsidian doc into a Google Doc"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To convert an **Obsidian document** to a **Google Doc**, you can follow a few straightforward steps. Here are some effective approaches to accomplish this conversion while preserving your formatting:

### **1. Export as Markdown and Use Google Docs Add-Ons**
1. **Export or Copy Markdown from Obsidian**:
   - Open your note in **Obsidian** and copy the **Markdown** content or save the file directly as a `.md` file.
   
2. **Convert to Google Docs via Google Docs Markdown Import Add-On**:
   - **Google Docs** doesn’t natively support Markdown, but you can use an add-on like **Docs to Markdown**:
     1. Open **Google Docs**.
     2. Install the **Docs to Markdown** add-on from the **Google Workspace Marketplace**.
     3. Create a new **Google Doc** and paste your Markdown content.
     4. Run the **Docs to Markdown** add-on, which will correctly format the pasted Markdown content, ensuring the formatting is preserved.

**Advantages**: This approach retains much of your Markdown formatting, including headings, bullet points, and links.

### **2. Use Markdown to HTML and Import to Google Docs**
1. **Convert Markdown to HTML**:
   - Open your Markdown file using a text editor or Markdown editor (such as **Typora**, **Dillinger**, or **MarkText**).
   - Export the document as **HTML**.

2. **Paste HTML into Google Docs**:
   - Open the exported **HTML** file in a browser.
   - **Select All** (`Ctrl + A` or `Cmd + A`) and then **Copy** the content (`Ctrl + C` or `Cmd + C`).
   - Go to **Google Docs**, open a new document, and paste (`Ctrl + V` or `Cmd + V`).
   
**Advantages**: HTML retains much of the formatting, such as **headings**, **links**, and **styles**.

### **3. Convert Markdown to Word, then Upload to Google Docs**
1. **Export Markdown to Word**:
   - Open your Markdown file in an editor like **Typora** or **MarkText**.
   - Choose to **export** as **.docx** (Microsoft Word format).

2. **Upload to Google Docs**:
   - Go to **Google Drive** and click **New > File Upload**.
   - Upload your `.docx` file.
   - Once uploaded, right-click and choose **Open with > Google Docs**.
   - Google Docs will convert the Word document to its native format.

**Advantages**: This process ensures a good level of fidelity for formatting, including lists, images, and headings.

### **4. Use Pandoc to Convert Markdown to Google Docs Format**
1. **Install Pandoc**:
   - Install **Pandoc** on your computer (available for Windows, Mac, and Linux).
   - Make sure you also have **Google Docs API access** (you'll need OAuth credentials).

2. **Use Pandoc to Convert**:
   - Open the terminal and run the following command:
     ```bash
     pandoc your_document.md -o your_document.docx
     ```
   - Once converted to a **.docx**, follow the previous step to upload to **Google Docs**.

**Advantages**: Pandoc is a very powerful tool that can handle a lot of formatting nuances, making it ideal for complex documents.

### **5. Manual Copy-Paste (With a Markdown Preview Plugin)**
1. **Use Markdown Preview Plugin in Obsidian**:
   - In **Obsidian**, switch to **Preview mode** (`Ctrl + E` or `Cmd + E`) to see the formatted document.

2. **Copy and Paste**:
   - Copy the content from the preview mode.
   - Open a new **Google Doc** and paste the content directly.
   
**Advantages**: This is a simple and direct method. However, it may not retain all formatting perfectly, especially for complex elements like tables.

### **Best Practices for Conversion**
- **Check Formatting After Import**: Google Docs may not always perfectly interpret Markdown elements, so after importing, **check headings, links, lists, and tables** to ensure everything appears as intended.
- **Avoid Reformatting Issues**: If tables or lists appear incorrectly, it’s sometimes easiest to **fix them manually** within Google Docs to match your preferences.
- **Use an External Markdown Editor**: Tools like **StackEdit** or **Dillinger** can be used to view and convert Markdown content, which can then be exported to **Google Docs**.

### **Summary Recommendation**
- For the **most seamless experience** and to keep your formatting intact, I recommend using the **export to .docx and upload to Google Docs** approach, as it maintains the best formatting quality overall.
- If you want a **quick approach** and don’t mind minor formatting adjustments, **copying the formatted preview** from Obsidian directly to Google Docs works well too.

These methods will help ensure you get a well-formatted Google Doc that closely matches your original Obsidian note. Let me know if you need further guidance on any of these steps!