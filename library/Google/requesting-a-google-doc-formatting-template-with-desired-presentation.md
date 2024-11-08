---
title: "Requesting a Google Doc formatting template with desired presentation"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To insert your desired footer format programmatically in **Google Docs**, you would need to use **Google Apps Script**. Here’s how you can automate adding this specific footer content:

### Footer Format:
```
Page: [Page Number] of [Total Pages]
Document: [Document Title]
Date: [Today's Date]
Author: Daniel Rosehill
```

### Step-by-Step Guide Using Google Apps Script

1. **Open Google Docs**:
   - Start with a Google Doc where you want to insert the footer.

2. **Open Google Apps Script**:
   - In the Google Doc, click on `Extensions` -> `Apps Script`.

3. **Script for Adding Footer**:
   - Copy and paste the following script in the Google Apps Script editor:

```javascript
function insertFooter() {
  var doc = DocumentApp.getActiveDocument();
  var body = doc.getBody();
  var footer = doc.addFooter();

  // Define the footer variables
  var pageNum = 'Page: ';
  var totalPages = ' of ' + doc.getHeader().getFootnotes().length;
  var documentName = 'Document: Request for Non-Commercial Use of the Global Value Factors Database';
  var date = 'Date: ' + new Date().toLocaleDateString();
  var author = 'Author: Daniel Rosehill';

  // Insert the footer content
  footer.appendParagraph(pageNum + "{{pageNumber}}" + totalPages);
  footer.appendParagraph(documentName);
  footer.appendParagraph(date);
  footer.appendParagraph(author);
}
```

4. **Modify the Script**:
   - If you want to insert variables like the **total page number** programmatically, modify the placeholder `{{pageNumber}}` in the script. Unfortunately, Google Apps Script doesn’t have direct access to dynamically place page numbers, but you can manually handle page count logic or export the document to PDF format using specific Apps Script APIs.

5. **Run the Script**:
   - After pasting the script, click the **Save** button.
   - Then, click the **Run** button to execute the script and insert the footer.

6. **Authorize**:
   - The first time you run the script, you’ll need to authorize the script to access your Google Docs.

### Future Use:
- This script can be modified or automated to run for multiple documents. You could add more functionality, such as different titles or dates, if needed.

With this setup, you can easily insert a custom footer with all the necessary information, and it will be added automatically to your Google Docs file.