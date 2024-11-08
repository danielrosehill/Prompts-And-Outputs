---
title: "Prompting tips for working with large inputs past the token limit"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Great. Could you give me some prompting tips on how to prompt GPTs and LLMs when asking them to parse a long document that is likely to exceed the token limit? Some strategies that can be used to get the model to chunk the input and generate based on that?

# Output

When working with long documents that exceed the token limit, chunking and structuring your approach can help ensure the model processes the most important information. Here are some strategies you can use to prompt effectively when parsing long documents:

### 1. **Break the Document into Chunks**:
   Divide the long document into smaller sections that fall within the token limit. Each chunk can be processed separately, and you can stitch together the responses. You might do this manually or ask GPT to generate a summary for each chunk. Here’s how you can approach it:

   **Prompt Example**:
   - *“I’m going to provide this document in sections. Please summarize each section for me. Here’s the first section: [input]. I’ll give you the next section after this.”*

   This allows you to process long texts step-by-step, ensuring nothing gets lost.

### 2. **Use Indexing**:
   If the document has logical sections (e.g., chapters, sections, or headings), start by asking the model to create an index of the document. Then, you can refer back to this index to target specific sections.

   **Prompt Example**:
   - *“Here is a long document. Can you create an index with the titles or main topics for each section? I’ll ask you to summarize specific sections from this index.”*

   This is especially useful for narrowing down specific parts of the document for further inquiry.

### 3. **Extract Key Sections First**:
   Instead of feeding the entire document, extract the most critical sections based on your goals. You can either do this manually or ask GPT to identify and summarize key portions.

   **Prompt Example**:
   - *“I’m providing a large document. Can you identify and summarize the sections that deal with [specific topic or keyword]?”*

   This way, you only focus on what’s important without needing the whole document processed.

### 4. **Generate Summaries Overviews**:
   After each chunk, ask the model for an overview or summary. You can compile these summaries into a comprehensive summary of the entire document once all chunks are processed.

   **Prompt Example**:
   - *“I’ll provide a long document section by section. Please summarize each section, and at the end, provide an overall summary based on all sections. Here’s the first section: [input].”*

### 5. **Ask for Step-by-Step Processing**:
   In cases where you want the model to focus on a detailed analysis, instruct it to analyze the document in stages (first identify themes, then summarize, then extract details).

   **Prompt Example**:
   - *“Here is a long document. First, identify the main themes and topics discussed. After that, I will provide specific sections for deeper analysis.”*

   This layered approach ensures the model stays within the token limit while still providing thorough insight.

### 6. **Leverage Hierarchical Summaries**:
   Start with a high-level summary of the entire document or sections of it, and then drill down into more detail as needed. This keeps the response within the token limit but allows for deeper exploration where required.

   **Prompt Example**:
   - *“Please give me a high-level summary of this document. Then, I’ll ask for detailed summaries of the sections I’m most interested in.”*

### 7. **Use Key Term Searches**:
   If the document is searchable, ask the model to focus on key terms or phrases that are relevant. You can use this to extract relevant portions for more targeted analysis.

   **Prompt Example**:
   - *“Search this document for mentions of [specific keyword]. Summarize the relevant sections or paragraphs that mention it.”*

### 8. **Request the Model to Identify Chunk Sizes**:
   Sometimes it’s helpful to let the model guide how to break up the text. You can ask it to stop once the token limit is approached, allowing for a natural chunking process.

   **Prompt Example**:
   - *“Here’s a large document. Please process it in sections and stop before the token limit is reached. Summarize each section as you go.”*

This method is more hands-off and allows GPT to manage the document in digestible portions.

---

By using these strategies, you can ensure that GPT or any LLM processes long documents effectively, avoiding token overflow while still capturing the important insights. You’ll get more accurate and coherent responses, even when working with extensive content.