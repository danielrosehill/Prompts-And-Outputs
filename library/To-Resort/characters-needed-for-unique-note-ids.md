---
title: "Characters needed for unique note IDs"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To calculate the number of characters needed for a unique ID string, let's assume you are using base-62 encoding, which consists of uppercase letters (A-Z), lowercase letters (a-z), and digits (0-9), giving 62 unique characters.

1. 100 million notes:

The number of possible IDs with n characters is . To find n for 100 million notes, we solve .

, which is greater than 100 million.

So, 5 characters are enough to support up to 100 million unique IDs.



2. 10 million notes:

To support 10 million unique IDs, solve .

, which is also more than enough for 10 million.

5 characters would still suffice for this as well.



3. 1 million notes:

For 1 million unique IDs, solve .

, which exceeds 1 million.

So, 4 characters are enough for 1 million notes.




Summary:

1 million notes: 4 characters

10 million notes: 5 characters

100 million notes: 5 characters


Let me know if you'd like more details on other encodings or options!

