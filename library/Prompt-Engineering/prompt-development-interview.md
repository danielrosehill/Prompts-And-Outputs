---
title: "Prompt development interview"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'm trying to create the ultimate prompt for finding the best note taking and knowledge base solution for my needs. Your job is to interview me to understand my requirements and then provide the most detailed prompt possible

# Question 1

**Question:** What do you primarily plan to use this solution for?  
**Answer:** The primary use for this is storing outputs of ChatGPT interactions and other LLMs. By doing so, I'm building up an extensive repository of information that is proving invaluable to both my personal and professional "lives." I'm gathering and storing valuable reference information, desk research about important topics for work, etc. I'm looking for a highly scalable solution for this. But it also has to be easy to use, accessible, and (very importantly) have a good reading interface for when I need to review and read the material that I've gathered.

# Question 2

**Question:** How important is structured data for you? Do you require tagging, folders, backlinks, or a hierarchical system to organize your notes?  
**Answer:** I'm really looking for a database-backed system. I've been using Obsidian for this purpose, and I find the idea of having to add tags in YAML frontmatter to be both annoying to use and not very scalable. The way WordPress or CMSes let you add related data (by "tagging" on the frontend) seems much better to me. So I would say I'm not in favor of the hierarchical/folder-based approach, as I don't think it's a good choice for scalability.

# Question 3

**Question:** Which apps and tools would you want this solution to integrate with (e.g., email, calendars, task managers)?  
**Answer:** Well, given that I'm using it to store ChatGPT outputs, that's the obvious integration that would be helpful. But it's not essential, as I can simply copy and paste the best conversations. But ultimately, for ease of use, it would be ideal to write a prompt in the note-taking app, generate an output right there on the page, and save it. The only other integration I can think of that would be helpful is email because sometimes I like to share useful outputs with my wife, colleagues, or friends.

# Question 4

**Question:** What devices will you primarily use? (e.g., Android, Fedora Linux, web access) Do you need offline access to your notes across all devices?  
**Answer:** My desktop is Fedora Linux, and my phone is Android. I don't think offline access is a priority at all, to be honest. If I'm offline, it's for a reason, and I don't want to be reviewing my notes. A Linux client would definitely be useful, but I think the best approach is to use a web UI.

# Question 5

**Question:** How important is markdown support to you? Should the system support live markdown preview, WYSIWYG editing, or both? Would you also need support for attachments like images, videos, or links?  
**Answer:** Markdown support is critical because when I gather useful outputs, I copy and paste out of ChatGPT. That text (right now) is markdown. A huge value-add in Obsidian is the fact that it automatically recognizes and parses that. I would say that’s an essential requirement—whatever that feature is called.

# Question 6

**Question:** How much data are you planning to store? You’ve mentioned scalability up to 1 million notes—would this include attachments, like images or documents, or just plain text?  
**Answer:** I gave 1 million as an arbitrary number to highlight that I want something very scalable. But it's also not totally out of reach. I've gathered about 2,000 outputs so far and I have about 1,000 prompts stored. As I use GPT and LLMs intensively for both work and personal reasons, it's easy to scale. I'm focused on finding a system that I can commit to and stick with for the long term. So when I see things like "1GB storage limit," those are systems that I quickly exclude.

# Question 7

**Question:** How important are privacy and security features for you? Would you require end-to-end encryption, multi-factor authentication, or other strong privacy measures?  
**Answer:** MFA is essential for any system that has a web UI, although I'd be happy to rely upon Google Workspace authentication. E2E encryption isn't essential for me.

# Question 8

**Question:** Do you need advanced search functionality within the system? For example, the ability to search within notes, tags, or even attachments?  
**Answer:** I definitely need a robust search functionality.

# Question 9

**Question:** Are you looking for any specific pricing tiers or storage limits? What budget constraints, if any, do you have in mind for this solution?  
**Answer:** You could say $100 per month, although $50 would be better. I'm looking for the best tool.

# Question 10

**Question:** Would you prefer a solution that handles interconnected information like a wiki, or is it more important to focus on organizing standalone entries?  
**Answer:** So I've devised my own system in Obsidian for linking outputs and prompts. Or rather, I've built a script that pulls out my prompts and then links them back. I find that helpful, but only because it reflects the rather unique circumstances of AI-generated knowledge. But linkages beyond that aren't key.

# Question 11
**Question:** Are there any specific features or functionalities you consider "must-haves" beyond what we've discussed? For example, collaboration tools, mobile app features, or customization options?  
**Answer:** Yes. Where Obsidian falls down for me is that the mobile app doesn't have simple paginated viewing. I can't just click "next" and go through all my latest outputs; this is a huge drawback for me. Likewise, I need a web UI. That's about it.

# Prompt

**Question:** Are there any specific features or functionalities you consider "must-haves" beyond what we've discussed? For example, collaboration tools, mobile app features, or customization options?  
**Answer:** Yes. Where Obsidian falls down for me is that the mobile app doesn't have simple paginated viewing. I can't just click "next" and go through all my latest outputs; this is a huge drawback for me. Likewise, I need a web UI. That's about it.

---

Now that I have a clear understanding of your requirements, here’s a detailed prompt for finding the best note-taking and knowledge base solution for your needs:

---

**Prompt:**

I am searching for a highly scalable note-taking and knowledge base solution tailored for storing outputs of ChatGPT interactions and other LLMs. The ideal system should meet the following requirements:

1. **Primary Purpose:** 
   - Store and manage extensive outputs from ChatGPT and LLMs, serving both personal and professional needs.
   - Facilitate gathering and referencing valuable information and desk research.

2. **Data Structure:** 
   - A database-backed system with robust support for tagging and linking data, moving away from hierarchical/folder-based organization.
   - Must recognize and parse markdown text efficiently for ease of use.

3. **Integration:**
   - Ideally, it should allow integration with ChatGPT (for generating prompts and outputs directly) and email (for sharing outputs).
   - Though integration is not mandatory, ease of use is a priority.

4. **Platform Compatibility:**
   - Must support web access primarily, with a Linux client desirable.
   - My devices include Fedora Linux for desktop and Android for mobile.

5. **Markdown Support:**
   - Essential markdown support with live preview and automatic recognition and parsing of markdown text.
   - Should handle attachments like images and links effectively.

6. **Storage and Scalability:**
   - The solution must be highly scalable, accommodating thousands of outputs and prompts with no restrictive storage limits (1GB limits are unacceptable).
   - Long-term commitment and usability are key considerations.

7. **Privacy and Security:**
   - Multi-factor authentication (MFA) is essential, ideally integrating with Google Workspace authentication.
   - End-to-end encryption is not necessary.

8. **Search Functionality:**
   - Requires robust search capabilities, allowing searches within notes, tags, and attachments.

9. **Pricing:**
   - Preferred budget is $50 per month, but up to $100 is acceptable for the best tool available.

10. **User Experience:**
    - Needs a mobile app that features simple paginated viewing for easy navigation through outputs.
    - A web UI is essential for overall accessibility.

11. **Must-Haves:**
    - Must provide the features above and facilitate ease of long-term use and accessibility.

---
 