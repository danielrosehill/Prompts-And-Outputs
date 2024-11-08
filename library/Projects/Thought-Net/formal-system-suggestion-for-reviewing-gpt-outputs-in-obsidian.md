---
title: "Formal system suggestion for reviewing GPT outputs in Obsidian"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Here’s a structured system for reviewing ChatGPT outputs in Obsidian with a formalized review queue, bookmarking, and tracking methods. This workflow combines tags, custom frontmatter, and Obsidian’s Dataview plugin for a systematic process.

### 1. **Organize Outputs with Frontmatter**
   Use YAML frontmatter at the top of each output note to organize metadata and manage your review queue. Here’s a sample template:
   ```yaml
   ---
   title: <Title of Output>
   date_captured: YYYY-MM-DD
   status: "unreviewed"  # or "reviewed", "important"
   tags: [output, ChatGPT]
   notes: ""  # Personal notes or key takeaways
   ---
   ```

### 2. **Bookmarking System for Important Outputs**
   - Mark important outputs with a frontmatter field, like `status: "important"`.
   - Alternatively, add a `#important` tag within the note.
   - This tagging approach allows you to retrieve important outputs later using a Dataview query.

### 3. **Set Up a Review Queue with Dataview**
   Using the Dataview plugin, you can create a dynamic review queue that organizes notes by their review status. For instance:
   - **Unreviewed Outputs**: 
     ```dataview
     table date_captured, notes
     from #output
     where status = "unreviewed"
     sort date_captured asc
     ```
   - **Important Outputs**: 
     ```dataview
     table date_captured, notes
     from #important
     sort date_captured asc
     ```

   - **Reviewed Outputs**: 
     ```dataview
     table date_captured, notes
     from #output
     where status = "reviewed"
     sort date_captured desc
     ```

4. **Formal Review Process and Queue Management**
   - **Daily or Weekly Review Session**: Dedicate time each day or week to review notes in the “unreviewed” table.
   - **Update Review Status**: After reviewing, update the note’s frontmatter `status` from `"unreviewed"` to `"reviewed"` or `"important"`, depending on the significance.
   - **Optional Notes**: Add notes to the `notes` field for future reference or context.

5. **Periodic Review of Important Outputs**
   - Regularly review the outputs tagged as important. You might dedicate a monthly or quarterly session to revisit and reflect on these entries to consolidate insights and identify recurring themes.

### 6. **Automate Reminders for Follow-Up Reviews**
   To automate reminders, you can use a “next_review_date” field in the frontmatter and a Dataview query to track notes up for review:
   ```yaml
   ---
   next_review_date: YYYY-MM-DD
   ---
   ```

   ```dataview
   table date_captured, notes
   from #important
   where next_review_date <= date(today)
   sort next_review_date asc
   ```

This system lets you quickly add, review, and organize outputs within Obsidian in a way that is trackable and adaptable as you gather more notes.