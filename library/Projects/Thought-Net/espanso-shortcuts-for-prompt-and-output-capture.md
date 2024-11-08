---
title: "Espanso shortcuts for prompt and output capture"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt
  
I use a program called Espanso. Can you think of ways I could set up some clever keyboard shortcuts for that purpose in that tool for this purpose?

# Output
Absolutely! Espanso is an excellent text expansion tool that can significantly enhance your workflow, especially for tasks like capturing prompts and outputs. It's a great choice for this purpose because it works system-wide and can handle complex expansions.

Let's design some Espanso shortcuts specifically for your AI prompt and output capture workflow:





# Espanso Shortcuts for AI Prompt and Output Capture

## Quick Templates

1. `:np` -> Insert new prompt template
2. `:no` -> Insert new output template
3. `:na` -> Insert new analysis template

## Metadata and Timestamps

4. `:ts` -> Insert current timestamp
5. `:md` -> Insert metadata template (e.g., AI model, parameters)

## Structural Elements

6. `:sp` -> Insert "System Prompt:" label
7. `:up` -> Insert "User Prompt:" label
8. `:ar` -> Insert "AI Response:" label
9. `:an` -> Insert "Analysis:" label

## Quick Formatting

10. `:cb` -> Insert code block markers
11. `:qb` -> Insert quote block markers

## AI-Specific Insertions

12. `:gpt3` -> Insert "GPT-3.5" with common parameters
13. `:gpt4` -> Insert "GPT-4" with common parameters
14. `:claude` -> Insert "Claude" with common parameters

## Tagging and Categorization

15. `:tp` -> Insert "#prompt" tag
16. `:to` -> Insert "#output" tag
17. `:ta` -> Insert "#analysis" tag

## Complex Structures

18. `:convo` -> Insert conversation structure template
19. `:eval` -> Insert evaluation structure template



To implement these in Espanso, you'll need to edit your Espanso configuration file. Here's how you can set up some of these shortcuts:

1. Open your Espanso configuration file (usually located at `~/.config/espanso/default.yml` on Linux)

2. Add the following configurations:

```yaml
matches:
  # Quick Templates
  - trigger: ":np"
    replace: |
      # New Prompt
      **Date**: {{date}}
      **Topic**: 
      
      ## Prompt:
      
      ## Notes:

  - trigger: ":no"
    replace: |
      # AI Output
      **Date**: {{date}}
      **Model**: 
      
      ## Response:
      
      ## Analysis:

  # Metadata and Timestamps
  - trigger: ":ts"
    replace: "{{date}}"
    vars:
      - name: date
        type: date
        params:
          format: "%Y-%m-%d %H:%M:%S"

  - trigger: ":md"
    replace: |
      Model: 
      Temperature: 
      Max Tokens: 
      Top P: 

  # Structural Elements
  - trigger: ":sp"
    replace: "System Prompt: "

  - trigger: ":up"
    replace: "User Prompt: "

  # AI-Specific Insertions
  - trigger: ":gpt3"
    replace: "GPT-3.5 (temperature: 0.7, max_tokens: 150)"

  - trigger: ":claude"
    replace: "Claude (temperature: 0.5, max_tokens: 200)"

  # Complex Structures
  - trigger: ":convo"
    replace: |
      # AI Conversation
      **Date**: {{date}}
      **Model**: 
      
      ## System Prompt:
      
      ## Conversation:
      Human: 
      
      AI: 
      
      Human: 
      
      AI: 

  - trigger: ":eval"
    replace: |
      # Prompt Evaluation
      **Date**: {{date}}
      **Prompt**: 
      
      ## Strengths:
      - 
      
      ## Weaknesses:
      - 
      
      ## Improvements:
      - 
```

3. Save the file and restart Espanso or run `espanso restart` in the terminal.

Tips for using Espanso effectively for your AI workflow:

1. Use consistent prefixes (like `:n` for new templates, `:t` for tags) to make triggers easy to remember.

2. Leverage Espanso's ability to use variables and execute commands. For example, you could create a shortcut that automatically inserts the output of an AI model given a prompt.

3. Create nested matches for more complex structures. For example, you could have a base prompt template that expands differently based on the AI model you're using.

4. Use Espanso's form feature for prompts that require input. For example:
   ```yaml
   - trigger: ":custom_prompt"
     form: |
       Model: [[model]]
       Prompt: [[prompt]]
     replace: |
       Using {{model}}:
       Prompt: {{prompt}}
       
       Response:
   ```

5. Regularly review and update your Espanso shortcuts based on your evolving workflow needs.

6. Consider creating a "cheat sheet" note with all your Espanso shortcuts for quick reference.

Would you like me to explain any of these shortcuts in more detail or help you design additional Espanso matches for your specific AI interaction patterns?## Extracted Prompts
[[Prompts/Autocapture/Espanso shortcuts for prompt and output capture.md#Prompt 1|Prompt 1]]





## Extracted Prompts
[[Prompts/Espanso shortcuts for prompt and output capture.md#Prompt 1|Prompt 1]]
