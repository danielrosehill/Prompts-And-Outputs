---
title: "Characters to avoid in file names on Obsidian"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

can you give me a list of characters that i should avoid using when saving files in obsidian. it's very easy to forget that the titles are filenames and if I include things like question marks it will cause sync issues on android

# Output
When saving files in Obsidian, especially to avoid sync issues on Android, you should avoid using the following characters in your filenames:

1. **Backslash (\)**
2. **Forward slash (/)**
3. **Colon (:)**
4. **Asterisk (*)**
5. **Question mark (?)**
6. **Quotation mark (")**
7. **Less than (<)**
8. **Greater than (>)**
9. **Vertical bar (|)**

These characters are either reserved by the operating system or can cause issues in file paths and syncing. To avoid problems, it's best to stick to alphanumeric characters, underscores (_), hyphens (-), and spaces.

# Question

Any idea why it doesn't seem to cause problems on my Fedora Linux computer but does on Android?

# Answer
The difference in behavior between your Fedora Linux computer and Android likely stems from how the operating systems handle file systems and file naming conventions.

### Fedora Linux:
- **File System**: Fedora typically uses the **EXT4** file system, which is quite permissive with filenames. It allows most characters, including those reserved on other systems, except for the null character and forward slash.
- **Character Handling**: On Linux, special characters in filenames are generally treated as part of the string and don’t have any special meaning unless explicitly escaped or used in commands.

### Android:
- **File System**: Android devices often use the **FAT32** or **exFAT** file system for their internal storage or SD cards. These file systems are more restrictive because they originated from older Windows systems, where certain characters are reserved or disallowed.
- **Sync Mechanism**: When syncing, if the underlying file system on Android doesn’t support certain characters, it can lead to issues, as the system might fail to create or access the file with those characters. This could cause sync errors, especially when trying to access files saved with such characters from a Linux system.

### Why It Works on Fedora But Not on Android:
- **File System Compatibility**: Fedora's EXT4 system can handle a wider range of characters in filenames, but when these files are synced to Android, the FAT32/exFAT file system might not support them, leading to sync issues.
- **Sync Tools**: The software used for syncing might not correctly translate or handle these characters between the two systems, causing the sync process to fail or skip problematic files.

To avoid these issues, it's best to stick to universally accepted characters across all operating systems when naming files, especially if they will be synced between different devices.## Extracted Prompts
[[Prompts/Autocapture/Characters to avoid in file names on Obsidian.md#Prompt 1|Prompt 1]]





## Extracted Prompts
[[Prompts/Characters to avoid in file names on Obsidian.md#Prompt 1|Prompt 1]]
