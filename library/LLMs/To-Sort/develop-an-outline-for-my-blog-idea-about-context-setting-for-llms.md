---
title: "Develop an outline for my blog idea about context setting for LLMs"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Please help me to create an organised outline for this blog idea.

Here are my notes:

Could you help me to write a blog explaining a workflow I've developed for improving LLM outputs? Here's my approach. I've been using GPT extensively for the past few months in both personal and professional domains. As is well known, context is really important to getting better outputs from GPT and shallow context can be a problem due to tokenisation limits. Systems like RAG are wonderful but not simple for your average GPT user to implement. I've created my own little system that has proven very effective which I'd like to share. I use an Obsidian vault to capture my prompts and outputs because it's markdown-first and a great way to organise outputs. Within my vault, I've created a "context" folder. This folder houses what I'm calling "context snippets" until I find a better name for them. Context snippets are discrete pieces of contextual data that can be used to quickly bring an LLM "Up to speed". In this way, you can try out using a new model which has no existing context of you and provide essential information. A more advanced approach I'm trying involves creating self-standing contextual repositories. I would suggest that this is a more scalable approach for business users and represents a middle ground solution between more casual context libraries and full RAG implementations. 
There are a few approaches that can be used to create these context repos however you choose to implement the idea. One of them is what we can call the manual method: it involves simply creating markdown documents with basic details about you. I can give a few examples: you may wish to create a context document with your professional responsibilities. Another about where you live. A third about your computer hardware. A simple example: I use my computer hardware context document to quickly spec out upgrades and run compatibility checks to find compatible hardware. In this way, I can run endless prompts without ever having to repeat my hardware details. And if I upgrade my hardware, I can just update the context document and reuse it for future prompts. But this is just one example. 
You can add that a work in progress for me is figuring out ways to combine multiple context snippets into aggregated context documents. Say that this might be a little beyond what this system  is capable of and a job for RAG ... or there might be imaginative approaches I haven't figure out yet ... like dynamically concatenating multiple context docs into temporary doc used for detailed context setting for a specific prompt or series of prompts.

Say that the quality of LLM outputs is highly dependent upon the quality of the intputs and that developing these contextual documents is probably the most effective strategy I've developed to date for greatly enhancing not only the utility of the outputs but also their consistency and reliability

# Output

**Title:** Optimizing LLM Outputs with Context Snippets: My Approach to Improving AI Interactions

**Introduction:**
I've been extensively using GPT for several months now, both personally and professionally, and I've learned that the quality of outputs is strongly linked to the context you provide. However, managing context effectively can be tricky due to tokenization limits. While systems like Retrieval-Augmented Generation (RAG) are powerful, they're often complex for casual users. In this blog, I want to share a simpler yet effective workflow I've developed that anyone can use to significantly improve their LLM outputs.

**1. The Challenge of Shallow Context in LLMs**
- **Importance of Context:** Start by emphasizing why context is crucial for getting quality outputs from language models like GPT.
- **Limits of Tokenization:** Discuss how tokenization limits can hinder the depth of context, making it challenging to maintain continuity.
- **The Complexity of Existing Solutions:** Acknowledge that advanced tools like RAG exist but are not practical for every user.

**2. My Simple but Effective Solution: The Obsidian Vault Approach**
- **Using Obsidian for Organization:** Introduce the tool of choice, Obsidian, and its markdown-first approach, which makes it perfect for organizing prompts and responses.
- **The "Context" Folder:** Describe how you created a specific "context" folder within the vault.
- **Context Snippets Explained:** Explain what "context snippets" are — small, discrete pieces of data that provide background information to quickly "catch up" the LLM.

**3. Setting Up Context Snippets**
- **Manual Method:** Detail the manual creation of context snippets as markdown files in Obsidian.
  - **Examples of Context Documents:**
    - Professional responsibilities.
    - Location and living situation.
    - Computer hardware specifications.
  - **Utility in Repeated Prompts:** Explain how these snippets help when interacting with LLMs by avoiding redundant explanations.
    - For instance, using a "hardware" context snippet allows you to discuss upgrades without repeating details.
- **Benefits for Consistency and Reliability:** Highlight how this approach boosts the consistency and utility of LLM outputs, improving the quality and reliability of responses.

**4. Advanced Approach: Context Repositories**
- **Context Repositories as a Scalable Solution:** Introduce the idea of self-standing contextual repositories as an advanced, more scalable alternative, especially for business use cases.
  - **Comparison with RAG Systems:** Explain how this solution serves as a middle ground between simple context libraries and more complex RAG implementations.

**5. Potential for Aggregating Context Snippets**
- **Work in Progress:** Acknowledge that combining multiple context snippets into aggregated documents is a work in progress.
- **Possible Approaches:** Discuss potential imaginative methods for achieving this:
  - Dynamic concatenation of multiple snippets.
  - Temporary aggregation for a specific prompt or sequence of prompts.
  - Acknowledge that these methods might edge closer to RAG-style complexity.

**6. Conclusion: The Importance of Quality Inputs**
- **Inputs Determine Outputs:** Reiterate that the quality of LLM outputs is directly dependent on the quality of inputs.
- **Why Context Matters:** Encourage readers to experiment with developing their own context documents, emphasizing that this strategy has significantly enhanced the utility, consistency, and reliability of your outputs.

**Call to Action:**
Are you using context effectively with your LLM workflows? I'd love to hear about your approaches and whether these methods inspire new ideas for organizing your interactions with AI.

