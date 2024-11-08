---
title: "Parsing article into email"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


 

Great! Here’s the same structure without the image:

---

**Source Name**: The Jerusalem Post  
**Author**: BY REUTERS  
**Title**: US backs Israel's operations in Lebanon despite risk of expanding conflict  
**Description**: The United States has continued to provide Israel with arms despite tensions during the past year over the conduct of its war in Gaza.  
**Published At**: 2024-10-03T20:37:45Z  
**URL**: [Read Full Article](https://www.jpost.com/middle-east/article-823142)

---

**Source Name**: Breitbart News  
**Author**: John Hayward, John Hayward  
**Title**: Saudis Grant Iranian President an Audience as Israel Escalates anti-Hezbollah Campaign  
**Description**: Iranian President Masoud Pezeshkian was welcomed in Doha, Qatar, on Wednesday for a meeting with Saudi Foreign Minister Prince Faisal bin Farhan, where they reportedly...  
**Published At**: [Add the date if available]  
**URL**: [Read Full Article] [Insert URL]

---

To implement this in Zapier, you can use a **Formatter by Zapier** action with a **Text** event. Use the **Append Text** function, and concatenate the necessary fields like this:

1. **Source Name**: `[Source Name]`  
2. **Author**: `[Author]`  
3. **Title**: `[Title]`  
4. **Description**: `[Description]`  
5. **Published At**: `[Published At]`  
6. **URL**: `[URL]`

Each section would be separated by line breaks, and you can pass this formatted text into the next step of your workflow.