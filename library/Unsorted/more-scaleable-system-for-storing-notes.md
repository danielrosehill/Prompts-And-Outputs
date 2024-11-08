---
title: "More scaleable system for storing notes"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt
Hmm, that's a bit concerning. 20,000 isn't a huge note repository. I'm very eager to self host. Can you recommend some alternative platforms I could self host and which might achieve much better levels of scale? Why do you think the stress testing has been at such a low level?
# Output

Based on your concerns about Obsidian's scalability and your preference for self-hosting, I can recommend some alternative platforms that may better suit your needs for managing a large-scale knowledge repository:

## Self-Hosted Alternatives for Large-Scale Knowledge Management

1. BookStack:
   - Open-source, self-hosted platform designed for organizing and storing information[2].
   - Uses a book-like organizational structure (books, chapters, pages) that can handle large amounts of content efficiently[2].
   - Supports full-text search, which is crucial for navigating extensive knowledge bases[2].

2. Wiki.js:
   - Modern, open-source wiki software built with Node.js[3].
   - Designed for performance and scalability, making it suitable for large repositories[3].
   - Supports various databases (PostgreSQL, MySQL, MariaDB, MS SQL Server, SQLite) for flexible data storage options[3].

3. XWiki:
   - Enterprise-grade, open-source wiki platform[5].
   - Offers structured data capabilities, making it easier to organize and retrieve large amounts of information[5].
   - Supports scalability across various platforms and is used by major organizations like Amazon[5].

4. MediaWiki:
   - The software that powers Wikipedia, designed to handle large-scale wikis[3].
   - Proven track record of managing millions of articles and high traffic loads[3].
   - Offers robust search capabilities and version control, essential for large repositories[3].

## Why Obsidian's Stress Testing May Be Limited

The relatively low level of stress testing for Obsidian (around 20,000 notes) could be due to several factors:

1. Target Audience: Obsidian is primarily designed for personal knowledge management, where most users typically have fewer notes.

2. Local-First Approach: Obsidian's focus on local storage and processing may introduce performance challenges with very large datasets on average consumer hardware.

3. Development Focus: The developers may have prioritized features and user experience for typical use cases over extreme scalability scenarios.

4. Community Testing: Much of the stress testing might come from the user community rather than extensive internal testing for edge cases.

## Conclusion

For your needs, a self-hosted wiki or knowledge base solution like BookStack, Wiki.js, XWiki, or MediaWiki might be more appropriate. These platforms are designed to handle larger scales of data and offer more robust search and organization features for extensive knowledge repositories. They also provide the benefit of self-hosting, giving you full control over your data and the ability to optimize the system for your specific hardware and requirements.

When choosing a platform, consider factors like the expected size of your repository, the types of content you'll be storing, your technical expertise for maintenance, and the specific features you need for your workflow. It may be worthwhile to set up test instances of these platforms to evaluate their performance with a dataset similar in size and structure to what you anticipate using.
 




## Extracted Prompts
[[Prompts/More scaleable system for storing notes.md#Prompt 1|Prompt 1]]
