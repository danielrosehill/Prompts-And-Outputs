---
title: "Creating a form in Obsidian"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt
Here's a post that I wrote on Reddit. Any chance you have some ideas? Anyone able to point me in the right direction? Trying to set up a form for capturing structured notes Hi everyone! I'm working at the moment on developing a kind of knowledge base for storing prompts and outputs that I use for generative AI tools like GPT (and all the rest of them). I have a template in mind that I *feel* should be pretty easy to configure using Obsidian. But I'm struggling to find the plugins and steps to make it come together. My idea is to create a "form" (within Obsidian, if that's possible) for capturing three parameters: Title Prompt Prompt output From that starting point, I'd like to create two "notes" (ie, markdown files): One with just the output (routed to /outputs) One with just the prompt (routed to /prompts) And an automatic link between the two so that the output could be associated with the prompt used to generate it (and vice versa). Anyone scaffolded a similar system? Many thanks for any pointers!

# Output
Your idea sounds like a really cool project, and Obsidian is a great tool for this kind of structured note-taking. Here are a few ideas and steps you can try to set up your system within Obsidian:

### 1. **Templater Plugin**
   - **Overview:** The Templater plugin is extremely powerful and can help you create templates that automatically populate fields based on your inputs.
   - **Steps:**
     1. Install the Templater plugin from Obsidian’s community plugins.
     2. Create a template for your form, including placeholders for Title, Prompt, and Prompt Output.
     3. Use Templater's scripting to automatically generate two separate notes (one for the prompt and one for the output) and save them in their respective folders (/prompts and /outputs).
     4. Link the two notes together by adding a link to the prompt in the output file and vice versa.

### 2. **Dataview Plugin**
   - **Overview:** Dataview can be used to create dynamic views of your data. It won't create the notes for you, but it can link and display related information.
   - **Steps:**
     1. Install the Dataview plugin.
     2. Use Dataview fields to create metadata in your notes, such as `prompt::` and `output::`.
     3. Write a Dataview query to automatically link prompts to their outputs and display them in a summary view.

### 3. **QuickAdd Plugin**
   - **Overview:** QuickAdd can automate the creation of notes based on a template and user input, similar to Templater.
   - **Steps:**
     1. Install the QuickAdd plugin.
     2. Configure a QuickAdd capture to create two notes from your template.
     3. Add a script within QuickAdd to insert links between the notes.

### 4. **Creating the Workflow**
   - **Create a Note Template:**
     - Create a template that includes placeholders for the Title, Prompt, and Output.
     - Save this template in your templates folder.

   - **Automating Note Creation:**
     - Use Templater or QuickAdd to create the notes based on this template. Set up your folder paths within the plugin so that the prompts and outputs are saved in their respective folders.

   - **Linking Notes:**
     - Use internal links within Obsidian to link the prompt and output notes. You can do this by referencing the note names directly.

### 5. **Advanced Scripting (Optional)**
   - If you’re comfortable with a bit of scripting, you can write custom JavaScript within Templater or QuickAdd to automate more complex tasks, such as auto-generating unique filenames, adding timestamps, or creating backlinks automatically.

### 6. **Alternative: Use a Database Plugin**
   - If Obsidian's native capabilities don't meet your needs, consider using a plugin like `Obsidian DB Folder`. This plugin allows you to work with data in a more structured, database-like manner, which might be closer to the "form" experience you're looking for.

### Example Templater Script:
```markdown
---
title: <% tp.file.title %>
prompt: <% tp.prompt("Enter your prompt:") %>
output: <% tp.prompt("Enter the output:") %>
---
# Prompt
<% tp.prompt %>

# Output
<% tp.output %>

[[<% tp.file.title %> Output]]

```

This script will prompt you for the input when creating the note, and you can tweak it to generate and link separate notes.

These steps should help you get started with setting up your system in Obsidian. If you hit any roadblocks or need more specific guidance, feel free to ask!

# Prompt 2
I get the feeling that I'm really hacking around the system, though! Can you think of any knowledge management or note taking tool that might provide a more intuitive pathway and workflow for achieving this?

# Output 2


If you’re looking for a more intuitive tool that might better align with your needs, here are a few alternatives that could offer a more straightforward approach:

### 1. **Notion**
   - **Overview:** Notion is a very flexible tool for note-taking and knowledge management. It allows you to create databases, which could easily accommodate your need for structured input fields (like Title, Prompt, and Output).
   - **Features:**
     - **Databases:** Create a database where each entry has fields for Title, Prompt, and Output. You can then create different views (like table, gallery, or list) to separate prompts and outputs.
     - **Linked Databases:** Easily link related entries, like connecting prompts to their respective outputs.
     - **Templates:** Notion allows you to create templates for new entries, making it easy to standardize your notes.

### 2. **Roam Research**
   - **Overview:** Roam Research is designed for non-linear note-taking and knowledge management, making it ideal for linking ideas and content together.
   - **Features:**
     - **Bidirectional Links:** Roam automatically links related content, which could simplify linking prompts and outputs.
     - **Block References:** You can reference specific blocks of text (like a prompt) from other notes, providing a powerful way to interconnect your knowledge base.
     - **Databases with Tables:** Roam also supports creating tables for structured data entry.

### 3. **Logseq**
   - **Overview:** Logseq is an open-source outliner and knowledge management tool similar to Roam but with a more straightforward interface and local-first data storage.
   - **Features:**
     - **Structured Data:** Like Roam, Logseq supports bidirectional links and block referencing.
     - **Hierarchy and Tags:** You can easily organize your prompts and outputs with tags and hierarchical structures.
     - **Databases:** Logseq can handle databases where you can define specific fields for each entry, similar to how you would in Notion.

### 4. **Coda**
   - **Overview:** Coda combines the flexibility of documents with the power of spreadsheets and databases. It’s highly customizable and allows for structured data entry and automation.
   - **Features:**
     - **Custom Forms:** You can create forms to capture inputs like Title, Prompt, and Output.
     - **Linked Tables:** Easily create relationships between different tables, such as linking prompts to their outputs.
     - **Automation:** Coda’s automation capabilities can handle repetitive tasks, like generating links between notes.

### 5. **Evernote**
   - **Overview:** Evernote is a classic note-taking app that has evolved to include more robust organizational features.
   - **Features:**
     - **Templates:** Evernote allows you to create custom templates for new notes, which could simplify the process of capturing prompts and outputs.
     - **Note Links:** You can link notes together to associate prompts with their outputs.
     - **Tagging:** Use tags to organize and filter your notes efficiently.

### 6. **Airtable**
   - **Overview:** Airtable is a hybrid of a spreadsheet and a database, making it a great tool for structured data management.
   - **Features:**
     - **Custom Fields:** You can create custom fields for each entry, such as Title, Prompt, and Output.
     - **Views and Filtering:** Create different views to separate your prompts and outputs.
     - **Linked Records:** Easily link records (e.g., link a prompt to its output) and automate relationships.

### 7. **Craft**
   - **Overview:** Craft is a note-taking and document creation app that is visually appealing and highly functional.
   - **Features:**
     - **Document Linking:** Craft makes it easy to link documents together, which could be useful for associating prompts with outputs.
     - **Templates:** Create and reuse templates to maintain consistency in your notes.
     - **Tagging and Organizing:** Craft offers powerful organizing features to manage your knowledge base effectively.

### 8. **TiddlyWiki**
   - **Overview:** TiddlyWiki is a highly customizable, non-linear note-taking tool that you can host locally or online.
   - **Features:**
     - **Custom Fields:** You can define custom fields and templates to capture structured data.
     - **Linked Notes:** Like Obsidian, TiddlyWiki allows for easy linking between notes.
     - **Plugins:** There are many community plugins available that can enhance its functionality, making it more intuitive for specific use cases.

Each of these tools offers a more guided or intuitive experience for setting up the kind of structured notes system you’re looking to create. If you prefer a more database-like approach with forms and relational data, **Notion**, **Coda**, or **Airtable** might be the best fit. If you prefer an outliner with strong linking capabilities, **Roam Research** or **Logseq** could be more suitable.

# Prompt 3
Those all sound like interesting ideas. However, to be clear, I'm looking for a note taking tool (or app or whatever) that can achieve what I described with little extra configuration required on my part. Do any of those tools meet that requirement?

# Output 3

For a note-taking tool that requires minimal configuration to achieve what you're aiming for, **Notion** and **Craft** are the two options that best meet that requirement:

### 1. **Notion**
   - **Why It Fits:**
     - **Minimal Setup:** Notion allows you to quickly set up databases with predefined fields. You can easily create templates for your "Prompt" and "Output" entries, and link them with just a few clicks.
     - **Ready-Made Templates:** Notion has many community templates you can use to get started quickly. For example, you can find templates for knowledge bases or content tracking that you can easily adapt for your needs.
     - **Ease of Use:** The drag-and-drop interface and built-in relations between databases make it straightforward to create and link notes without extensive configuration.

### 2. **Craft**
   - **Why It Fits:**
     - **Simple and Intuitive:** Craft is designed for ease of use with a focus on beautiful, structured documents. You can create notes and link them with minimal effort.
     - **Linking Documents:** Craft’s linking feature is intuitive, allowing you to easily associate prompts with outputs without the need for complex setup.
     - **Ready-to-Use Templates:** Craft offers pre-made templates for various use cases, which can be quickly adapted to your structured note-taking requirements.

### 3. **Evernote**
   - **Why It Fits:**
     - **Simple Linking:** Evernote's note-linking feature is very straightforward, allowing you to connect notes (like prompts and outputs) easily.
     - **Pre-Built Templates:** Evernote offers a variety of templates that can be quickly adapted to your needs with minimal customization.
     - **Minimal Configuration:** It’s designed to be used out of the box, with only slight adjustments needed to fit your specific workflow.

Among these, **Notion** likely offers the best balance of flexibility and ease of setup for your specific use case, with the added benefit of a large community offering templates and tips to get started quickly. **Craft** would be the next best option if you're looking for a more streamlined, visually focused experience with minimal configuration.




## Extracted Prompts
[[Prompts/Creating a form in Obsidian.md#Prompt 1|Prompt 1]]
[[Prompts/Creating a form in Obsidian.md#Prompt 2|Prompt 2]]
[[Prompts/Creating a form in Obsidian.md#Prompt 3|Prompt 3]]
[[Prompts/Creating a form in Obsidian.md#Prompt 4|Prompt 4]]
