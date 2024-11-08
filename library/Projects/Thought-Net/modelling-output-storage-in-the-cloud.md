---
title: "Modelling output storage in the cloud"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'm thinking about adapting my prompt output storage system so that it runs natively in the cloud and sends prompts to an API and then collects them back in an outputs folder. 

I have a couple of questions about this architecture:

1) Will it significantly increase the required file storage if the outputs are gathered as documents rather than stored as rows in a database?

2) My idea is to create a highly scaleable system capable of storing perhaps hundreds of thousands of these outputs.It would be ideally something like a knowledge base that humans could edit and carry forward (ie improve upon).

Google Drive provides great cloud-native document editing capabilities but I dont' think it's the right tool. Can you think of any other programs I could implement? It would be great if they were self hostable as I think it's vital that users would be able to backup their own output "vault"

# Output

Based on your requirements for a cloud-native, scalable system to store and edit large numbers of prompt outputs, here are my thoughts on your questions:

1. File storage vs database storage:

Storing outputs as individual documents rather than database rows will likely increase the total storage required, but not significantly for text-based outputs[3]. The overhead for individual files is generally small. However, file systems can be less efficient for searching and indexing large numbers of small files compared to databases[4].

2. Alternative systems for scalable, editable knowledge base:

While Google Drive offers good collaborative editing, you're right that it may not be ideal for your specific needs. Here are some self-hostable alternatives to consider:

- Outline: A wiki and knowledge base for teams. It's self-hostable, supports collaborative editing, and can scale to large numbers of documents[2].

- BookStack: An open-source, self-hosted knowledge base platform. It organizes content into books, chapters, and pages, which could work well for your output structure[2].

- MediaWiki: The platform that powers Wikipedia. It's designed for high-traffic websites and large amounts of content, though it may be overkill for smaller setups[2].

- Obsidian: While primarily designed for personal use, Obsidian can be adapted for team use. It stores data as local markdown files, making backups and version control easy[2].

- Custom solution using a document-oriented database: You could build a custom system using something like MongoDB or CouchDB, which are designed to store and query large numbers of documents efficiently.

For your specific requirements of scalability, editability, and self-hosting capability, I would recommend considering Outline or a custom solution built on a document database. These options would allow you to:

1. Store hundreds of thousands of outputs efficiently
2. Provide human-editable interfaces
3. Implement version control and collaboration features
4. Allow users to easily backup their "vault" of outputs

Remember that whichever system you choose, you'll need to carefully design the architecture to handle the expected volume of data and concurrent users. You may also want to implement a caching layer and efficient search indexing to maintain good performance as the system scales.






## Extracted Prompts
[[Prompts/Modelling output storage in the cloud.md#Prompt 1|Prompt 1]]
