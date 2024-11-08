---
title: "Using old server as a local LLM host"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt
I have a spare computer that I'm currently using as a home server running Proxmox. I'm wondering if this might be a good fit for running a local LLM. Could you help me to spec that out? I'd firstly like to know how to SSH into the server to retrieve the HW specs (I need help with the command, not how to SSH!)

# Output

To retrieve the hardware specifications of your Proxmox server, you can SSH into it and use the following command:

```
lscpu && free -h && lsblk
```

This command combines three useful utilities:

1. `lscpu`: Displays information about the CPU architecture
2. `free -h`: Shows the amount of free and used memory in human-readable format
3. `lsblk`: Lists information about all available block devices

Once you run this command, you'll get detailed information about your server's CPU, memory, and storage devices. This information will be crucial in determining whether your server is suitable for running a local LLM.

After you've obtained this information, we can analyze it to determine if your server meets the requirements for running a local LLM. Generally, for running a local LLM, you'll want to consider:

1. CPU: A modern multi-core processor (preferably 8 cores or more)
2. RAM: At least 16GB, but 32GB or more is recommended for better performance
3. Storage: Fast SSD storage with at least 100GB free space

Once you have the output from the command, please share it, and I can help you interpret the results and determine if your server is suitable for running a local LLM. If it is, we can then discuss which LLM might be appropriate based on your hardware specifications and intended use case.