---
title: "Automatically adding tracking data to Google Docs"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Please suggest some conventions that are used to provide tracking data in the footer of documents. I would like to note the following particulars: Document name: Drafted by: Type/Privacy (Internal/External) Date: I would ideally like a way to be able to automatically insert these using Google Docs

# Output

To provide **tracking data in the footer** of your Google Docs with information like the document name, drafted by, type/privacy, and date, you can follow these best practices:

### Suggested Footer Structure:
```
Document Name: [Document Name]
Drafted by: [Author's Name]
Type/Privacy: [Internal/External]
Date: [Date]
```

### Steps to Automatically Insert These Fields in Google Docs:

1. **Document Name**:
   - You can create a custom footer and manually type in the document name or link the title to the footer using the **Header & Footer** feature.
   - Alternatively, using **Add-ons** like **AutoLaTeX** or a custom Google Apps Script could help auto-fill the document title.

2. **Drafted by**:
   - This can be manually added in the footer or inserted using **custom templates** for documents. If you're frequently adding the same details, you can create a template for consistency.

3. **Type/Privacy (Internal/External)**:
   - Create a custom **dropdown** or an easily selectable **note** in your template, so you can mark this field each time you start a document.

4. **Date**:
   - You can automatically insert the current date into the footer using **Insert > Date** in Google Docs.
   - For dynamic updating, Google Apps Script can be used to automatically refresh the date each time the document is opened or edited.

### How to Insert a Footer in Google Docs:
1. Go to **Insert > Headers & Footers > Footer**.
2. In the footer area, manually input the desired fields such as document name, author, and date.
3. To insert the **current date**, use **Insert > Date**.

### Automating with Google Apps Script (Optional):
To fully automate the insertion of some of these fields, you can use **Google Apps Script**:
- For example, to automatically insert the **document name** and **current date** dynamically into the footer:

```javascript
function addFooterInfo() {
  var doc = DocumentApp.getActiveDocument();
  var footer = doc.addFooter();
  var title = doc.getName(); // Gets the document name
  var today = new Date(); // Gets the current date

  footer.appendParagraph("Document Name: " + title);
  footer.appendParagraph("Drafted by: Your Name");
  footer.appendParagraph("Type/Privacy: Internal");
  footer.appendParagraph("Date: " + today.toLocaleDateString());
}
```
To use this:
1. Go to **Extensions > Apps Script**.
2. Copy and paste the above script and click **Run**.

### Conclusion:
This structure allows for a clear, organized footer that tracks key document details. While you can manually add these fields for most documents, using **Google Apps Script** can automate the process, particularly for fields like the document name and date. This approach will help streamline your document management and ensure consistent tracking across all your Google Docs files.