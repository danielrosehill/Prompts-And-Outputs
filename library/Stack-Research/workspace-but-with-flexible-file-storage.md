---
title: Google Workspace but with storage you cans control?
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Perhaps there's something like google workspace that provides a bit more flexibility.

I would like:

- To store data in my own Postgres database
- To store other file data in a B2 bucket

Are there any similar tools - cloud business workspaces - that would allow me to do this?

# Output

Based on your specific requirements for a flexible cloud business workspace that allows you to store data in your own Postgres database and file data in a B2 bucket, there are a few options that could potentially meet your needs:

1. Nextcloud

Nextcloud is an open-source, self-hosted productivity platform that offers similar functionality to Google Workspace but with more flexibility.

**Key Features:**
- File storage and synchronization
- Collaborative document editing
- Calendar and contact management
- Project management tools
- Customizable and extensible with apps

**Pros:**
- Can be configured to use Postgres as the backend database
- Supports external storage, including Backblaze B2
- Highly customizable and self-hosted, giving you full control over your data
- Active development and community support

**Cons:**
- Requires technical expertise to set up and maintain
- May need additional configuration for some advanced features

Nextcloud can be set up to use Postgres as its database, and you can configure it to use Backblaze B2 as external storage for file data.

2. ownCloud

ownCloud is another open-source cloud collaboration platform similar to Nextcloud (they actually share a common ancestry).

**Key Features:**
- File sync and share
- Collaborative editing
- Calendar and contact sync
- Extensible with apps

**Pros:**
- Supports Postgres as the backend database
- Can be configured to use Backblaze B2 for file storage
- Self-hosted, providing control over your data
- Enterprise version available with additional features

**Cons:**
- Setup and maintenance require technical knowledge
- Some advanced features may require the enterprise version

Like Nextcloud, ownCloud can be configured to use Postgres and Backblaze B2, meeting your specific requirements.

3. Seafile

Seafile is an open-source file sync and share solution that can be self-hosted.

**Key Features:**
- File synchronization and sharing
- Team collaboration
- Online file editing
- Version control

**Pros:**
- Supports Postgres as the database backend
- Can be configured to use S3-compatible storage like Backblaze B2
- Known for its performance with large files and many small files
- Offers both community and professional editions

**Cons:**
- Less comprehensive than Nextcloud or ownCloud in terms of built-in productivity tools
- May require additional integrations for a full workspace solution

While Seafile focuses more on file management than full workspace functionality, it meets your database and storage requirements and could be combined with other tools for a complete solution.

Conclusion:

Among these options, Nextcloud stands out as the most comprehensive solution that closely matches your requirements. It provides a full suite of productivity tools similar to Google Workspace, while allowing you to use your own Postgres database and Backblaze B2 for storage.

All of these solutions require some level of technical expertise to set up and maintain, as they are self-hosted. However, this approach gives you the flexibility and control over your data that you're looking for.

Remember to consider factors like your team's technical capabilities, specific feature requirements, and long-term maintenance when making your decision. It might be beneficial to set up test instances of these platforms to evaluate which best fits your needs.

# Prompt

Is Nextcloud or Owncloud the bigger and better maintained project these days?

# Output

Based on the search results and the information provided, it appears that Nextcloud has become the bigger and better maintained project compared to ownCloud in recent years. Here are the key points supporting this conclusion:

1. Community and Development:
   - Nextcloud has a more active and diverse developer community, with over 2,000 contributors and 300 apps in its app store[1].
   - ownCloud has a smaller developer community, with around 1,000 contributors and 200 apps in its app store[1].
   - Nextcloud has a more vibrant and supportive community, both for users and developers[1].

2. Innovation and Updates:
   - Nextcloud has a faster development cycle, with major releases every six months and minor releases every month[1].
   - ownCloud has a slower development cycle, with major releases every year and minor releases every three months[1].
   - Nextcloud is described as more innovative and agile, releasing new features and updates more frequently and consistently[1].

3. Features and Collaboration:
   - Nextcloud offers more collaboration features, such as video chat, online office, and project management[1].
   - Nextcloud aims to be a complete collaboration platform, similar to Microsoft Office 365 and Google Workspace[1].
   - Nextcloud has more integrations with popular services like Zoom, Slack, Jitsi, and Moodle[1].

4. Open-Source Commitment:
   - Nextcloud is fully open-source, with all components available under the AGPLv3 license[3].
   - ownCloud restricts certain functionalities to its Enterprise edition, which requires a commercial license[3].

5. Security:
   - Nextcloud is described as having a slight edge in security due to its commitment to remaining 100% open-source, allowing for more community scrutiny[4].

6. Customizability and Extensibility:
   - Nextcloud is noted to have a more extensive app ecosystem and a more active developer community, leading to greater customizability[4].

While both projects continue to evolve, the information suggests that Nextcloud has gained more momentum and community support since its fork from ownCloud in 2016. It appears to be the more actively developed and feature-rich project of the two at present.

 




## Extracted Prompts
[[Prompts/Workspace but with flexible file storage.md#Prompt 1|Prompt 1]]
[[Prompts/Workspace but with flexible file storage.md#Prompt 2|Prompt 2]]
