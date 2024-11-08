---
title: "Text Generator adhere to template"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


I'm using an Obsidian plugin called Text Generator which allows users to run prompts through the Open AI API. It's great. 

I'm trying to think of a way to get it to follow a template I've created. 

My template is basically this:

```
# Prompt 

The prompt goes here

# Output 

The output goes here
```

I'd like to be able to run the plugin on the prompt, but have it return the output only after the output heading. 

Can you think of a way to set this up (or with a different plugin or with a combination of them)

Certainly! To achieve the behavior where the Obsidian Text Generator plugin adheres to your specific template, you can follow a structured approach. While I don't have direct access to the Text Generator plugin's internal workings, I can suggest a generalized method that you could adapt:

### Step-by-Step Guide:

1. **Initial Template Setup in Obsidian:**
    - Create a new note or template file in Obsidian with the following structure:
      ```markdown
      # Prompt

      The prompt goes here

      # Output

      ```

2. **Define a Placeholder for Prompt:**
    - Use a unique placeholder text within the `# Prompt` section to easily identify and replace it later. For example:
      ```markdown
      # Prompt

      [PROMPT_PLACEHOLDER]

      # Output

      ```

3. **Automated Replacement Script/Plugin:**
    - Write a small script (e.g., using Python) or use an existing automation tool/plugin within Obsidian (like Templater) to replace `[PROMPT_PLACEHOLDER]` with your actual prompt text.

4. **Generating Output Using OpenAI API:**
    - After replacing the placeholder, use the Text Generator plugin to run the prompt through OpenAI's API.
    - Ensure that only the content after `# Output` gets replaced with OpenAI’s generated response.

### Example Using Templater Plugin (Hypothetical Approach):

1. **Install Templater Plugin:**
    - If not already installed, add Templater from Obsidian’s community plugins list.

2. **Create a Template File:**
    - Save this template file in your designated templates folder:
      ```markdown
      # Prompt

      <% tp.user.replace_placeholder() %>

      # Output

      <% tp.user.insert_generated_output() %>
      ```

3. **Templater User Scripts:**
    - Define two user scripts within Templater settings:
    
    ```javascript
    // replace_placeholder.js
    module.exports = async (tp) => {
        return "Your actual prompt text here";
    }
    
    // insert_generated_output.js
    module.exports = async (tp) => {
        const openaiResponse = await callOpenAI(tp);  // Assume callOpenAI is your function to fetch response from OpenAI API.
        return openaiResponse;
    }
    
    async function callOpenAI(tp) {
        // Implement your logic to call OpenAI API and get response.
        const apiKey = "your_openai_api_key";
        const promptText = "Your actual prompt text here";  // You may also fetch this dynamically.
        
        // Example fetch request (adjust as necessary):
        const response = await fetch("https://api.openai.com/v1/engines/davinci-codex/completions", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${apiKey}`
            },
            body: JSON.stringify({
                prompt: promptText,
                max_tokens: 150,
            })
        });

        const data = await response.json();
        
        return data.choices[0].text.trim();
   }
   ```

4. **Run Your Template in Obsidian:**
   - Use Templater’s command palette options or hotkeys to insert your prepared template into any note.
   - The placeholders will be dynamically replaced by defined user scripts, and you should see the output generated after `# Output`.

### Summary:

By using tools like Templater along with custom user scripts, you can set up an automated workflow where prompts are dynamically inserted and processed by OpenAI, ensuring that outputs are placed correctly under the specified heading in your template.

Always ensure that any script accessing APIs handles sensitive information securely and adheres to rate limits imposed by those APIs.
 