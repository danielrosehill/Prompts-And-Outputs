---
title: "Modifying Bookstack to support the Output Hub design"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt
Let's consider BookStack. 

I would like to add the functionality we've discussed:

The knowledge base has three sections for agents, prompts, and outputs.

The user can "action" (run) a prompt from within the web UI. When that happens, the prompt is sent to an LLM API (let's say Anthropic). The output that the API sends back is saved as a file in the outputs folder. And ideally some link is recorded between the two.

Do you think that this functionality could be added to a tool like BookStack (or Outline)?
And if so how would I go about doing that?

# Output

Based on your requirements and the information provided about BookStack, I believe it's possible to add the functionality you're looking for to a tool like BookStack or Outline. However, it would require some custom development and integration. Here's how you might approach this:

1. Extending BookStack:

BookStack doesn't have a traditional plugin system, but it does offer several ways to extend its functionality:

- Custom HTML Head Content: This allows you to add custom JavaScript and CSS.
- Visual Theme System: For customizing the look and feel.
- Logical Theme System: This allows PHP code-based extensions by hooking into specific events.
- REST API: For external interaction and consumption of BookStack data.

To implement your desired functionality, you'd likely need to use a combination of these approaches:

1. Use the Logical Theme System to add new routes and controllers for your agent, prompt, and output sections.
2. Modify the database schema to include new tables for agents, prompts, and outputs.
3. Create new views for these sections using the Visual Theme System.
4. Use the Custom HTML Head Content to add JavaScript for handling the "action" button and API calls.
5. Use the REST API to handle data storage and retrieval for your custom sections.

2. Implementation steps:

a) Create new database tables for agents, prompts, and outputs.
b) Use the Logical Theme System to add new routes and controllers for these sections.
c) Create new views for displaying and managing agents, prompts, and outputs.
d) Add a button to "action" prompts in the prompt view.
e) Implement JavaScript to handle the "action" button click, send the prompt to the Anthropic API, and save the response.
f) Create a link between prompts and outputs in your database schema.
g) Update the views to display the relationships between prompts and outputs.

3. Challenges:

- This approach requires a deep understanding of BookStack's architecture and Laravel (the framework BookStack is built on).
- You'll need to maintain your custom code across BookStack updates.
- There's a risk of conflicts with future BookStack updates.

4. Alternative approach:

Instead of deeply integrating with BookStack, you could:

a) Build a separate application that handles the agent, prompt, and output functionality.
b) Use BookStack's API to create pages or sections that link to your custom application.
c) This approach would be more maintainable and less likely to break with BookStack updates.

In conclusion, while it's technically possible to add this functionality to BookStack, it would require significant custom development. Given BookStack's structure and the project's stance on plugins, it might be more practical to build a separate application that integrates with BookStack via its API. This would allow you to leverage BookStack's documentation capabilities while maintaining a separate, purpose-built system for managing your LLM interactions.
 




## Extracted Prompts
[[Prompts/Modifying Bookstack to support the Output Hub design.md#Prompt 1|Prompt 1]]
