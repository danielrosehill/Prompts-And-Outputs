---
title: "Probing the scalability of Obsidian for this purpose"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

For context, I'm attaching a rough outline of a project I'm working on currently for saving the outputs from LLM interactions at scale. As a temporary solution, I'm using Obsidian, while I'm quite enjoying. However, I wonder how scalable this approach is. Can Obsidian be used to amass large knowledge repositories without significant slowdown? I'm thinking about scaling into the tens of thousands of notes. If not, can you suggest an alternative platform which might be more appropriate?

# Output

Based on the information provided in your query and the attached project outline, I can offer insights on Obsidian's scalability and suggest potential alternatives for large-scale knowledge management.

## Obsidian's Scalability

Obsidian has been tested with large vaults and generally performs well, but there are some limitations to consider:

1. Performance with Large Vaults:
   - Obsidian has been stress-tested with vaults containing up to 20,000 notes[1][8].
   - Users report acceptable performance with 10,000-18,000 notes, though some lag may occur when using the file explorer[3].

2. Factors Affecting Performance:
   - Hardware: Solid-state drives (SSDs) perform better than mechanical hard drives for large vaults[3].
   - Plugins: The number and type of plugins used can impact performance[4].
   - File Size: While the size of non-Markdown files doesn't significantly affect Obsidian's performance, large amounts of text content can slow down indexing and searching[2].

3. Limitations:
   - Search Performance: Initial search times may increase with very large vaults[4].
   - Graph View: The graph view can become laggy with a high number of notes[4].

## Alternatives for Large-Scale Knowledge Management

If you find Obsidian's performance insufficient for your needs, consider these alternatives:

1. Document360:
   - Offers robust search capabilities and supports large-scale knowledge bases[5][6].
   - Provides both internal and external knowledge base options.

2. Guru:
   - Designed for centralized knowledge management in large organizations[5][6].
   - Features intelligent search and verification workflows.

3. TiddlyWiki:
   - Highly customizable, open-source tool for creating personal wikis[7].
   - Suitable for tech-savvy users who want complete control over their knowledge base.

4. Custom Solution:
   - For your specific use case of managing LLM interaction outputs at scale, you might consider developing a custom solution using a combination of:
     - A database system (e.g., PostgreSQL) for efficient data storage and retrieval.
     - A search engine (e.g., Elasticsearch) for fast full-text search capabilities.
     - A web-based frontend for user interaction and visualization.

## Conclusion

While Obsidian can handle repositories with tens of thousands of notes, its performance may degrade with extremely large vaults, especially when using resource-intensive features like the graph view. For your project focusing on saving LLM interaction outputs at scale, you might want to consider a more specialized solution or develop a custom platform that can efficiently handle the volume and type of data you're working with.

If you decide to continue with Obsidian, consider strategies like splitting your vault into multiple smaller vaults or using a combination of Obsidian for front-end interaction and a more robust backend storage solution for the bulk of your data.

Citations:





## Extracted Prompts
[[Prompts/Probing the scalability of Obsidian for this purpose.md#Prompt 1|Prompt 1]]
