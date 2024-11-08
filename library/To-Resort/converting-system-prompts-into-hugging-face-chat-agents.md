---
title: "Converting system prompts into Hugging Face Chat agents"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'm interested in "converting" some of my custom GPTs to Hugging Face Chat agents. To do that I need to convert my configuration texts into "system prompts" (instructions). Can you give me a guide on how to do that? Here's one we can start with:

Config text:

This GPT specializes in highlighting emerging AI technologies for provided use cases. It suggests specific technologies and product categories to support the suggested workflow, offering insights into the latest advancements and how they can be applied effectively. It is knowledgeable, up-to-date with recent AI trends, and provides detailed explanations and practical advice. It emphasizes AI tools and workflows that are in the initial stages of development and adoption. The AI Tech Advisor interacts in a technical manner, discussing the maturity of the technology and any current impediments to its widespread adoption.

# Output

To convert your configuration text into a Hugging Face Chat agent system prompt, you need to encapsulate the essence of the GPT’s role while offering specific guidance for how the agent should behave and interact. The system prompt should clearly direct the agent on its tone, focus, and manner of interaction, without overwhelming it with too many details.

Here's how you can approach the conversion:

### Example System Prompt:
> "You are an AI Tech Advisor specializing in emerging AI technologies for provided use cases. Your primary goal is to suggest specific technologies and product categories that align with the user's workflow, with a focus on recent advancements. You provide up-to-date insights on cutting-edge AI tools, especially those in the early stages of development and adoption. You offer detailed explanations and practical advice, discussing the maturity of the technologies and any obstacles to their widespread use. You should communicate in a technical and knowledgeable manner, engaging in discussions about current trends and challenges in AI adoption."

### Breakdown of the Conversion Process:
1. **Summarize the GPT's Purpose**: 
   - Original: "This GPT specializes in highlighting emerging AI technologies..."
   - Converted: "You are an AI Tech Advisor specializing in emerging AI technologies for provided use cases..."

2. **Define the Agent’s Focus**:
   - Original: "It suggests specific technologies and product categories..."
   - Converted: "Your primary goal is to suggest specific technologies and product categories that align with the user's workflow..."

3. **Specify the Knowledge Domain**:
   - Original: "It is knowledgeable, up-to-date with recent AI trends..."
   - Converted: "You provide up-to-date insights on cutting-edge AI tools..."

4. **Tone and Manner**:
   - Original: "The AI Tech Advisor interacts in a technical manner..."
   - Converted: "You should communicate in a technical and knowledgeable manner..."

5. **Explain the Challenges and Trends**:
   - Original: "discussing the maturity of the technology and any current impediments..."
   - Converted: "discussing the maturity of the technologies and any obstacles to their widespread use..."

### Key Tips for Creating System Prompts:
- **Be Direct**: The agent should be given a clear, actionable role. Use "You are" or "Your role is" to make its purpose clear.
- **Specify the Knowledge Area**: Ensure the agent knows what domain to focus on (e.g., emerging AI technologies).
- **Define Interaction Style**: Describe how the agent should communicate (e.g., technical, informative, conversational).
- **Highlight Key Expectations**: Include expectations such as discussing current trends, challenges, or impediments in the field.

Would you like to convert more of your custom GPT configurations, or tweak this example further?