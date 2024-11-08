---
title: "Hotkey for entering text into Obsidian"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I spend a lot of time prompting LLMs and working with them professionally. Frequently I need to enter the same text strings whether in prompts or in feedback messages - things like "please return the full codeblock in one go". I'd love to be able to speed this up a bit. 

It would be useful to have something like a text snippet manager. Ideally I would press on a hotkey which would trigger this to open. Then I can search through my snippets and select one to quickly paste it into whatever context window I had active. 

The context I would require the snippets in would be an open Chrome window.

I use Fedora Linux

Any tool(s) like this that could run on my desktop?

# Output

Based on your requirements, there are a few options that could work well for managing text snippets on Fedora Linux. Here are some recommendations:

## Espanso

Espanso is an open-source, cross-platform text expander that would suit your needs well[3]. It offers several key features:

- Works across different applications, including Chrome
- Allows you to create custom snippets and expand them with keywords
- Provides a search bar (activated with ALT+Space) to quickly find snippets
- Supports advanced features like shell commands and custom scripts

To use Espanso on Fedora:

1. Install it using the instructions on their website
2. Create snippets for your common LLM prompts and feedback messages
3. Use the ALT+Space shortcut to quickly search and insert snippets

## Nap

Nap is a command-line code snippet manager that could be adapted for your use case[1]. While primarily designed for code, it can store any text snippets. Key features include:

- Text-based user interface for managing snippets
- Command-line interface for quick access
- Fuzzy search functionality

To use Nap effectively:

1. Install it using Go: `go install github.com/maaslalani/nap@main`
2. Create snippets for your common prompts and messages
3. Use the command-line interface to quickly find and copy snippets

## SnippetPixie

SnippetPixie is another option available as a Snap package for Fedora[5]. It's designed specifically for text expansion and could work well for your needs.

To use SnippetPixie:

1. Install it from the Snap Store
2. Set up your snippets with custom abbreviations
3. Type the abbreviations to expand your snippets in any application

## Custom Solution with IBus

For a more integrated approach, you could set up a custom solution using IBus and the Compose key[4]. This method allows you to create text substitutions that work across the system, including in Chrome:

1. Enable multiple IBus engines in Settings > Region & Language
2. Set up a Compose key in Settings > Keyboard Shortcuts
3. Create a `~/.XCompose` file with your custom substitutions

While this method requires more setup, it provides a system-wide solution that works seamlessly in Wayland.

Each of these options offers different strengths. Espanso provides a comprehensive, cross-platform solution with a search interface. Nap offers a lightweight, terminal-based approach. SnippetPixie provides a dedicated text expansion tool. The IBus method offers deep system integration. Choose the one that best fits your workflow and preferences.

 