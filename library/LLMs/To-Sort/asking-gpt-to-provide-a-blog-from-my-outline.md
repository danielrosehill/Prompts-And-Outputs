---
title: "Asking GPT to provide a blog from my outline"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*



# Prompt

Please generate a blog that explains how i use ChatGPT to spec out hardware upgrades. This methodology works wodnerfully to quickly run compatibility checks on your hardware. I've used this to spec out upgrades, check component compatibility, and I've even used this to convert dry technical spec sheets into much richer narrative style descriptions allowing me to better understand my hardware.

The process is like this. 

Firstly, I gather a detailed spec of my system. I use Fedora Linux so it requires a few commands. But if you're using Windows, you can drop in screenshots of your system config.

Next, I ask ChatGPT to generate a JSON out of that config. While not strictly necessary, standardising a repository of contextual snippets on JSON is a good way to keep this data machine-readable and not specific to any particular LLM.

Add a note that I have created Github repositories just to hold contextual snippets like this (which you might say is a primitive form of RAG!). This allows me to pass these context snippets through version control and means that they're accessible to me from whatever computer I'm prompting with.

That's all the prep work. 

Now, whenever you want to check for a compoatible hardware upgrade, you can drop the JSON into a chat with your favorite LLM.

Here are some example prompts:

Can you evaluate the capability of my hardware for running local LLMs? What's the most powerful local LLM I could run on this current build?

Please evaluate the capability of my hardware for running image generation LLMs? Can you suggest some GPU upgrades and provide a price point for each?

Non-LLM specific:

I'd like to upgrade to a better motherboard. What are some options?

Please generate a document that lists all the constraints posed by current hardware. An example of a constraint: the maximum RAM that my motherboard will allow.

Please provide with me some approxixate costs for updating my RAM. Please provide a cost estimate for adding an additional 32GB of RAM and another one for maximising the RAM to its capacity in this system.


# Output

