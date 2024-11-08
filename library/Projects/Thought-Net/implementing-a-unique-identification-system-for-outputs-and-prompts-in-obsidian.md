---
title: "Implementing a unique identification system for outputs and prompts in Obsidian"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt
I'm beginning to run into a problem in Obsidian. I store a lot of outputs in an initial capture folder and it's very easy for them to have the same file name which means that I have to manually edit the titles. I had an ID that it might be smart to begin assigning unique identifiers for both the prompts and outputs that I'm capturing. Could you think of a system that would give me enough unique values to scale to 1 million permutations with the minimum amount of letters and numbers?

After doing that, suggest a unique prefix for the IDs that I can use to visually distinguish between prompts, outputs, and whatever else I might assign IDs to.

Finally give me some ideas on how I can automatically populate these ideas into titles as soon as I create new notes in Obsidian. Ideally the ID would match the folder in which the note was being created. So if I created a new note in Obsidian it might begin with O2324 ... if O was the prefix being used for outputs

# Output

Based on the code execution results and your requirements, I can provide you with a system for unique identifiers and suggestions for implementation in Obsidian.

## Unique Identifier System

The code demonstrates that using a base36 system (digits 0-9 and letters a-z) with 4 characters is sufficient to generate over 1 million unique permutations. This system provides:

- Minimum length: 4 characters
- Character set: 0-9 and a-z (case-insensitive)
- Total permutations: 36^4 = 1,679,616 (exceeding your 1 million requirement)

Example IDs: 0000, 0001, ..., zzzz

This system is compact and easily readable, making it ideal for your Obsidian notes.

## Prefix System

To distinguish between different types of notes, you can use a single letter prefix:

- P: Prompts
- O: Outputs
- R: Research notes
- I: Ideas
- S: Summaries

For example:
- P0000: First prompt
- O0001: Second output
- R0002: Third research note

## Automatic ID Population in Obsidian

To automatically populate these IDs in Obsidian titles, you can use a combination of Obsidian plugins and features:

1. **Templater Plugin**: This powerful plugin allows you to create custom templates with dynamic content.

2. **Folder-specific templates**: Set up different templates for each folder in Obsidian.

3. **JavaScript Date functions**: Use these to generate sequential numbers based on the current date and time.

Implementation ideas:

1. Create a template for each type of note (prompts, outputs, etc.) using the Templater plugin.

2. In each template, use JavaScript to generate the ID:

   ```javascript
   <%*
   const prefix = 'O'; // Change this based on the folder
   const date = new Date();
   const timestamp = date.getTime().toString(36).slice(-4);
   const title = `${prefix}${timestamp} `;
   tR += title;
   %>
   ```

   This script generates a unique ID using the current timestamp, converts it to base36, and adds the appropriate prefix.

3. Set up folder templates in Obsidian settings, associating each folder with its corresponding template.

4. When creating a new note in a specific folder, Obsidian will automatically use the associated template, generating a unique ID in the title.

5. For even more precision, you could maintain a counter in a separate file and read/increment it each time you create a new note, ensuring absolute uniqueness.

By implementing this system, when you create a new note in the "Outputs" folder, it might automatically start with a title like "O2324" (where 2324 is a unique base36 number generated from the timestamp or a counter).

This approach provides a scalable, visually distinct, and automatically implementable system for organizing your Obsidian notes with unique identifiers.