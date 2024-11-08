---
title: Prompting for simple Python script creation 
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



Please write a Python script

I'd like you to recurse through the following directory and subdirectories, globbing through all markdown files that you find:

`/home/daniel/Git/blogs/danielgoespromptingblog/blog/content`

But avoid this directory:

`/home/daniel/Git/blogs/danielgoespromptingblog/blog/content/Prompt-Library`

Your objective is to identify prompts in the markdown files.

Expect to find a structure like this in the files containing prompts:

```
## Prompt

{prompt text}

## Output

{output text}
```

In this example, I would like you to capture {prompt text}

You should create a copy of the file that you found the prompt in within this path:

`/home/daniel/Git/blogs/danielgoespromptingblog/blog/content/Prompt-Library/Auto-Extracted`

The title of the file should match the title of the file the prompt was extracted from.

This is a script that I will be running repeatedly so set up storage to remember your previous runs and avoid duplicating data.

 