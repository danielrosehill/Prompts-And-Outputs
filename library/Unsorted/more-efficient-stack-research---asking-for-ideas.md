---
title: "More efficient stack research - asking for ideas"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Hi Claude! 

One of my favorite uses for LLMs is doing "stack research". Sometimes I do very in depth stack research like the prompting I did earlier (in which I might compare two potential database architectures for a project and asked you for thoughts on how I could model my Postgres schema in MongoDB). In other instances, I'm looking for guidance towards finding the best tool for a project from existing software. 

This AI use case has been pretty transformative for me. I recently built a CRM and event management solution for a corporate event almost from scratch. Time was of the essence and your guidance was invaluable in helping me identify the perfect integrations. I find that with the right prompting strategies I can often unearth interesting projects, especially in the world of open source, that previously evaded me. 

As much as I love discovering good technology, it can also be vastly time consuming and tool-finding can become a distraction from the world that needs to get done. 

I'm trying to think of ways I could leverage LLMs' usefulness in this respect to make the project less tedious. When I'm looking for a solution, I tend to set out very detailed and specific requirements. My optimal outcome from AI-assisted ressearch is getting my tech evaluation list down to 5 very strong options. That's a manageable amount of options for me to go through one by one. 

What are your thoughts on how I might go about doing this? Is fine-tuning an LLM for this purpose overkill? Would that be hard? Perhaps simply creating a custom agent is a better approach? Can I do this in Anthropic? Prompting templates? A program that integrates with an LLM by API and is interactive? Let me know your thoughts!

# Output

Your approach to leveraging LLMs for "stack research" is indeed innovative and can be highly effective for quickly identifying suitable technologies and tools for projects. To streamline this process further and make it less time-consuming, here are some suggestions:

1. Custom AI Agent:
Creating a custom AI agent could be an excellent approach. This agent could be designed to:
- Understand your specific requirements
- Search through databases of software and tools
- Apply filters based on your criteria
- Rank options based on relevance and suitability
- Provide a concise list of top 5 recommendations

This approach is less complex than fine-tuning an entire LLM and can be more flexible for your specific needs.

2. Prompting Templates:
Developing a set of structured prompting templates could significantly improve consistency and efficiency. These templates could include:
- Project type and scope
- Specific technical requirements
- Budget constraints
- Integration needs
- Scalability requirements
- Open-source vs. proprietary preferences

By using consistent templates, you can train yourself (and potentially an AI system) to provide more targeted and efficient responses.

3. Interactive Program with LLM Integration:
Creating a program that integrates with an LLM via API could be a powerful solution. This program could:
- Guide you through a series of questions to define your project requirements
- Use these inputs to formulate optimal prompts for the LLM
- Process the LLM's responses to extract and rank the most relevant options
- Present you with a curated list of top recommendations

This approach combines the flexibility of custom software with the power of LLMs.

4. Fine-tuning:
While fine-tuning an LLM for this specific purpose might be overkill, it could be considered if you're dealing with a very niche area or have access to a large, specialized dataset of software recommendations. However, the other approaches mentioned are likely more practical and cost-effective for most scenarios.

5. Anthropic's Claude:
Currently, Anthropic doesn't offer direct fine-tuning or custom agent creation for Claude. However, you can use Claude effectively with well-crafted prompts and potentially integrate it into a custom solution via API.

Recommended Approach:
Given your needs, I would suggest starting with a combination of prompting templates and an interactive program that integrates with an LLM via API. This approach would allow you to:

1. Standardize your input process
2. Leverage the power of LLMs for broad knowledge
3. Customize the output processing to your specific needs
4. Iteratively improve the system based on your experiences

You could begin by creating a set of comprehensive prompting templates. Then, develop a program that uses these templates to interact with an LLM API, process the responses, and present you with a curated list of top 5 recommendations. This system could be refined over time based on its performance and your evolving needs.

This approach strikes a balance between leveraging existing LLM capabilities and customizing the process to your specific workflow, potentially saving you significant time in your technology selection process.
 




## Extracted Prompts
[[Prompts/More efficient stack research - asking for ideas.md#Prompt 1|Prompt 1]]
