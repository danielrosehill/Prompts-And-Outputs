---
title: "Cross tool highlighting in markdown"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Does markdown have any native support for highlighting so that one can highlight in one program without the concern that it will render text unreadable in another

# Output

Based on the information provided in the search results, here's a summary of the situation regarding native highlighting support in Markdown:

1. Standard Markdown does not have native support for highlighting. Highlighting is not part of the core Markdown specification.

2. Some Markdown flavors and editors have introduced custom syntax for highlighting, but it's not universally supported:

   - Some use double equals (==highlight==) for highlighting. This is supported by editors like Typora, iA Writer, and Quilt.
   - However, this syntax is not part of CommonMark, which attempts to specify Markdown syntax unambiguously.

3. The most widely compatible method for highlighting in Markdown is to use HTML:
   
   - The <mark> HTML tag is recommended for highlighting: <mark>highlighted text</mark>
   - This works in most Markdown processors and is more semantically correct than other HTML alternatives.

4. For Obsidian specifically:
   
   - Obsidian's built-in highlighting uses ==double equals==
   - However, this is limited to a single color and doesn't support annotations
   - Some users use plugins like "Highlightr" for more advanced highlighting, but this adds HTML to the Markdown files

5. Given the lack of standardization, using highlighting syntax from one program may indeed render text unreadable or lose formatting in another.

In conclusion, while some Markdown flavors support highlighting with ==double equals==, there is no universally supported native Markdown syntax for highlighting that works across all programs. The most compatible approach is to use HTML <mark> tags, but this comes at the cost of reduced readability in plain text.

Citations:
[1] https://pplx-res.cloudinary.com/image/upload/v1727559334/user_uploads/nzpyeupul/image.jpg
[2] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/19554357/c86fc347-7314-4156-9224-89f921ac9236/program.py
[3] https://israelmitolu.hashnode.dev/markdown-for-technical-writers-tips-tricks-and-best-practices
[4] https://stackoverflow.com/questions/25104738/text-highlight-in-markdown/36039773
[5] https://www.reddit.com/r/Markdown/comments/jykg3b/why_doesnt_highlighting_work_in_my_markdown_apps/
[6] https://forum.obsidian.md/t/better-text-marking-functionality/45510
[7] https://www.codecademy.com/resources/docs/markdown/highlight




## Extracted Prompts
[[Prompts/Cross tool highlighting in markdown.md#Prompt 1|Prompt 1]]
