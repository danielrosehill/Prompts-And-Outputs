---
title: "Combining saved purchasing preferences with LLMs - ideation"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I think YAML is the way to go.
Here's a bigger and better idea. 
I would like to be able to use these with an LLM in the future.

Imagine I prompted "could we look at macro keyboards again? You can use [file] for my preferences"

Think about how I could implement that preferably using an LLM via API. Any ideas?

# Output

Your idea to use YAML for storing preferences and integrating it with an LLM via API is excellent. Here's a concept for implementing this system:

1. **YAML Preference Files**:
   Store your preferences in YAML files, each named descriptively (e.g., `macro_keyboard_prefs.yaml`).

2. **File Storage**:
   Keep these YAML files in a cloud storage service (like Dropbox, Google Drive, or GitHub) for easy access.

3. **LLM Integration**:
   Use an LLM API (like OpenAI's GPT or Anthropic's Claude) to process your requests and the YAML data.

4. **Custom Middleware**:
   Create a middleware application that:
   - Handles your prompts
   - Retrieves the relevant YAML file
   - Sends both to the LLM API
   - Processes and returns the response

Here's a conceptual workflow:

1. You prompt: "Could we look at macro keyboards again? You can use [macro_keyboard_prefs.yaml] for my preferences"

2. The middleware:
   - Identifies the file request
   - Retrieves `macro_keyboard_prefs.yaml` from cloud storage
   - Reads and parses the YAML content

3. The middleware constructs an API call to the LLM, including:
   - Your original prompt
   - The parsed YAML data
   - Instructions for the LLM on how to use the preference data

4. The LLM processes the request, using the preference data to tailor its response

5. The middleware receives the LLM's response and presents it to you

Implementation steps:

1. **YAML Structure**:
   ```yaml
   category: macro_keyboards
   last_updated: 2024-10-01
   preferences:
     type: full_with_macro
     macro_keys: 6+
     connectivity: 
       - wireless
       - bluetooth
       - 2.4GHz
     lighting: no_rgb_preferred
     price_range: 
       min: 70
       max: 250
     features: 
       - customizable_keys
       - durable_build
     software: easy_macro_programming
   ```

2. **Middleware Development**:
   - Create a Python application using libraries like `pyyaml` for YAML parsing and `openai` or `anthropic` for API interactions
   - Implement file retrieval from your chosen cloud storage
   - Develop prompt parsing to identify file requests

3. **LLM Prompt Engineering**:
   Design a prompt template that instructs the LLM how to use the YAML data, e.g.:
   ```
   User preferences for {category} are provided in YAML format below. 
   Use these preferences to guide your recommendations:

   {yaml_content}

   User query: {user_prompt}

   Provide recommendations based on these preferences and the current market offerings.
   ```

4. **User Interface**:
   Create a simple interface (CLI, web app, or chat interface) where users can input their prompts

This system would allow you to easily reference and update your preferences over time, while leveraging the power of LLMs to provide up-to-date recommendations based on your stored preferences.