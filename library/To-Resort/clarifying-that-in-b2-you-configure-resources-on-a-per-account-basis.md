---
title: "Clarifying that in B2 you configure resources on a per-account basis"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'd like to clarify something about rclone. when i'm adding a b2 as a remote, the intended workflow is that I add one remote per *account* and that I can then use that account to access all the buckets stored in it. for some reason i assumed that every bucket required a separate configuration!

# Output

Yes, you're correct in clarifying that when adding Backblaze B2 as a remote in **rclone**, you only need to configure one remote per account. This remote will allow you to access all buckets stored under that account. There's no need to configure a separate remote for each bucket. 

Once you've added your B2 account as a remote, you can interact with any bucket in that account by specifying the bucket name in your commands, like so:
```bash
rclone copy ~/Desktop/backup.tar.gz b2:my-bucket-name/
```
This approach makes it more efficient and flexible to manage multiple buckets without the need to configure each one separately.

If you had initially set up separate remotes for each bucket, you can now simplify the configuration by just using a single remote to access all your buckets.