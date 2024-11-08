---
title: "Extrapolating file storage predictions for Obsidian"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I have setup my Obsidian vault for managing prompt outputs now and it seems to be syncing fairly well to its cloud storage in B2. 

As my vault is growing, I've also been able to calculate some file size data that may help in assessing the scalability of this system. 

Here's what I have so far:

603 outputs = 3.2MB
385 prompts = 183 Kb

Could you extrapolate some numbers from these

Firstly assume that the number of outputs and prompts is equal as it should be. 

Next, provide the total estimated combined storage size for the system if it were to hold 100,000 prompts and outputs

Then 1 million of each 
then 10 million of each

# Output

Thank you for providing those details about your Obsidian vault and the file size data. Let's analyze and extrapolate based on the information you've given.

First, let's calculate the average size per prompt and output:

1. Average size per output: 3.2MB / 603 ≈ 0.0053MB (5.3KB)
2. Average size per prompt: 183KB / 385 ≈ 0.475KB

Now, let's assume the number of outputs and prompts is equal, and use the sum of these averages (0.0053MB + 0.475KB ≈ 0.4803MB) as the combined size for one prompt-output pair.

Extrapolating for different scales:

1. **For 100,000 prompts and outputs:**
   100,000 * 0.4803MB = 48,030MB ≈ 48.03GB

2. For 1 million prompts and outputs:
   1,000,000 * 0.4803MB = 480,300MB ≈ 480.3GB

3. For 10 million prompts and outputs:
   10,000,000 * 0.4803MB = 4,803,000MB ≈ 4.803TB

These calculations show that:
- **A system with 100,000 prompts and outputs would require about 48GB of storage.**
- Scaling to 1 million would need around 480GB.
- At 10 million, you'd be looking at approximately 4.8TB of storage.

These estimates assume that the average sizes remain consistent as you scale up, which may not always be the case in real-world scenarios. Factors like data compression, metadata overhead, and varying content lengths could affect the actual storage requirements.

For your Obsidian vault syncing to B2 cloud storage, these numbers suggest that:
1. The current 100,000 scale should be manageable with most cloud storage plans.
2. At 1 million, you'd need to consider more robust storage solutions.
3. At 10 million, you'd definitely need to look into enterprise-level storage options or consider data archiving strategies.

Remember to factor in additional space for system growth, backups, and any other files you might store alongside the prompts and outputs.

 




## Extracted Prompts
[[Prompts/Extrapolating file storage predictions for Obsidian.md#Prompt 1|Prompt 1]]
