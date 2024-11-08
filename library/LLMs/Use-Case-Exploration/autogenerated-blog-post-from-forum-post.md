---
title: Autogenerate a blog post from a forum post on Reddit
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Title:** How I Use ChatGPT to Create Comparison Matrices for Stack Research

**Introduction:**
In today's fast-paced tech environment, finding the right tools for your projects can be a daunting task. Whether it's accounting software, CRMs, or any other tech stack component, making informed decisions requires effective research and comparison. To simplify this process, I’ve developed a workflow using ChatGPT to create comparison matrices for tools I'm researching. In this blog post, I'll show you how I leverage ChatGPT to streamline my software selection process by generating easy-to-understand comparison matrices, and how you can apply this method to your own stack research.

**1. Using ChatGPT for Stack Research**
I use ChatGPT intensively to help me research software options for different projects. Recently, I needed to find an accounting solution for my small business, and this is where GPT was very helpful. My prompts for this kind of research are typically detailed, specifying my exact requirements.

For instance, when searching for accounting software, my prompt might look like this:

```
Please provide a list of accounting software that meets all of the following criteria:

- SaaS / cloud hosted
- Supports expense capture
- Supports invoicing and receipt generation
- Has a subscription for less than $100 per month
- Leverages some AI features
```

By specifying the requirements, ChatGPT can narrow down the list and provide software suggestions that fit my criteria.

**2. Fine-Tuning with Follow-Up Prompts**
Once ChatGPT gives me some initial suggestions, my workflow typically involves a bit of back and forth. I often give more context or refine the search by prompting something like:

*"Nice job, but try to find tools that are more suited to a digital consultancy like mine. I don't require inventory management, but a native integration with Google Workspace for client management would be very helpful."*

This interaction helps in tailoring the results more specifically to my needs. After some iterations, I usually have a good shortlist of tools that match what I'm looking for. I often store these lists in Obsidian for easy future reference.

**3. Creating a Comparison Matrix for the Shortlist**
While having a shortlist is helpful, reading through a long list of features can get overwhelming. This is where my latest "hack" comes in: using ChatGPT to generate a comparison matrix for the final shortlist.

Here's how I prompt for it:

```
Please generate a comparison matrix comparing the 5 products on our final shortlist. Please output this matrix to raw markdown.
```

This way, GPT generates a clear comparison matrix, formatted in markdown, which I can directly capture in Obsidian. The matrix is an easy way to see which products meet specific requirements at a glance.

Without further instruction, ChatGPT will decide which columns to include in the matrix, but I often prefer specifying what I want to compare.

**4. Customizing the Matrix**
For a more specific comparison, I might add details like this:

```
Please generate a comparison matrix for the shortlist we have identified. Include the following: price, free tier limits, Fedora Linux support.
```

This way, I can make sure that all the relevant features I'm considering are present, and it helps me compare tools more effectively.

**5. Using Symbols for Clarity**
One variation I often use involves including tick symbols to make the comparison table even more readable. When the goal is to avoid another long block of text, using symbols can make things much clearer.

For that, I might prompt:

```
Please generate a comparison matrix for the shortlist we have identified. Include price and free tier limits. Also include whether the platform has a native Linux GUI. If it does, indicate that with a tick symbol. If it doesn't, use an x symbol.
```

This type of presentation helps me quickly scan the information, especially when I'm looking at multiple criteria.

**6. Example: Creating a Comparison Matrix for CRMs**
To give a concrete example, let's say I am researching small business CRMs. After using ChatGPT to generate a shortlist of suitable options, I prompt for a comparison matrix to simplify the decision-making process.

Here's an example prompt and the resulting comparison matrix:

```
Please generate a comparison matrix for the following CRMs: HubSpot, Zoho CRM, Freshsales, Pipedrive, Insightly. Include features such as price, free tier availability, native integration with Google Workspace, and support for custom workflows.
```

### Example Comparison Matrix:

| CRM          | Price (per month) | Free Tier Available | Google Workspace Integration | Custom Workflow Support |
|--------------|-------------------|---------------------|------------------------------|-------------------------|
| HubSpot      | $50               | ✓                   | ✓                            | ✓                       |
| Zoho CRM     | $20               | ✓                   | ✓                            | ✓                       |
| Freshsales   | $29               | x                   | ✓                            | ✓                       |
| Pipedrive    | $18               | x                   | ✓                            | ✓                       |
| Insightly    | $35               | x                   | ✓                            | ✓                       |

This table provides a concise overview, making it easier to compare and determine which CRM best fits my requirements.

**Conclusion:**
This workflow—using detailed prompts, refining suggestions, and generating comparison matrices—has made my stack research much more effective and efficient. Whether you're looking for accounting software, project management tools, or anything else, creating a clear comparison matrix can help you make informed decisions faster. I hope this helps others in their own software research endeavors!
