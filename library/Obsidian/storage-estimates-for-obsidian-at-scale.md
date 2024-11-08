---
title: "Storage estimates for Obsidian at scale"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt
I'm currently capturing prompts and outputs into Obsidian which is then syncing to B2. B2 provides vast storage capabilities but a sync client relies upon syncing to local devices. Give me some estimates for how much space I could expect the vault to take up as it scales. Let's say there are 10,000 saved files each with a fairly average prompt and output capture of about 1,000 words. How much space would that take up?

# Output
To estimate the storage space required for your Obsidian vault with 10,000 files containing prompts and outputs, let's break down the calculation:





# Obsidian Vault Storage Estimate

## Assumptions:
1. Average file contains 1,000 words
2. Average word length in English is about 5 characters
3. Each character typically requires 1 byte of storage
4. Markdown formatting adds approximately 10% overhead
5. Obsidian metadata and additional formatting add another 10% overhead

## Calculation:

1. Basic text content per file:
   1,000 words * 5 characters/word * 1 byte/character = 5,000 bytes

2. With Markdown formatting (10% increase):
   5,000 bytes * 1.1 = 5,500 bytes

3. With Obsidian overhead (additional 10%):
   5,500 bytes * 1.1 = 6,050 bytes per file

4. Total for 10,000 files:
   6,050 bytes * 10,000 = 60,500,000 bytes

## Conversion to more readable units:
- 60,500,000 bytes
- ≈ 60.5 MB (Megabytes)
- ≈ 0.0605 GB (Gigabytes)

## Additional considerations:
- Attachments (images, PDFs) would significantly increase storage needs
- Obsidian's internal linking and indexing may add a small amount of overhead
- Actual file sizes may vary based on content complexity and formatting



Based on these calculations, a vault with 10,000 files, each containing an average of 1,000 words of prompt and output content, would take up approximately 60.5 MB of storage space.

Key points to consider:

1. **Scalability**: This estimate scales linearly. If you were to have 100,000 files, it would be around 605 MB, and 1,000,000 files would be about 6.05 GB.

2. **Variance**: Actual file sizes will vary. Some prompts and outputs may be much shorter, while others could be significantly longer.

3. **Attachments**: If you include images, diagrams, or other file attachments in your notes, the storage requirements could increase dramatically. A single high-resolution image could easily be larger than several text-only notes.

4. **Metadata**: If you use extensive tagging or create many internal links, this could slightly increase the storage needs, but not significantly for text-based content.

5. **Compression**: When syncing to B2 or other cloud storage, files are typically compressed, which could reduce the actual storage space needed in the cloud.

6. **Local vs. Cloud Storage**: While 60.5 MB is quite manageable for local storage, it's also very modest for cloud storage. B2's vast storage capabilities mean you have room for significant growth.

7. **Performance**: Even with 100,000 or 1,000,000 files, modern systems should handle this amount of data without significant performance issues, especially since Obsidian is designed to work with large vaults.

8. **Backup Considerations**: When planning backups, you might want to account for 2-3 times the estimated size to allow for version history and potential growth.

Given these estimates, your current setup with Obsidian syncing to B2 seems very sustainable. Even if you were to increase your vault size by 100 times, you'd still only be using about 6 GB of storage, which is very manageable both locally and in cloud storage.

For perspective, if you were capturing 10 new prompt-output pairs every day, it would take you about 3 years to reach 10,000 files, and even then, the storage requirements would be quite modest.

Would you like to explore strategies for optimizing storage as your vault grows, or discuss how to manage performance with larger vaults?## Extracted Prompts
[[Prompts/Autocapture/Storage estimates for Obsidian at scale.md#Prompt 1|Prompt 1]]





## Extracted Prompts
[[Prompts/Storage estimates for Obsidian at scale.md#Prompt 1|Prompt 1]]
