---
title: "How can GPT generate outputs from inputs with long documents in context"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Earlier I provided my home inventory to you (ChatGPT) in order to ask you to try to identify some surplus things I might be holding onto. In previous interactions I've provided an entire book in PDF form (about 300 pages) in order to receive a list of specific mentions in the book. In all these cases, I've received what seemed like reliable outputs from GPT that showed that the context was processed in full. But now you're mentioning tokenisation as being a limit. Were the previous generations hallucinations? If not, how was GPT able to process an "input" with so many tokens?
# Output

The difference you’re observing relates to how models process and handle context, specifically tokenization limits. Here's an explanation based on the evolution of GPT models:

1. **Previous Generations and Context Handling**: 
   In earlier interactions (like when you provided your home inventory or the 300-page PDF), GPT likely seemed to process large amounts of text and return meaningful outputs. However, this doesn’t mean the entire 300 pages or inventory list were being processed simultaneously. GPT works within a fixed context window (token limit), and earlier outputs would have been based on a summarization or segmentation approach. It might have processed sections of the text or been selectively prompted in chunks if you were inputting manageable amounts at a time. If the document was too large, it could only return results based on the portion of text that fit within the token limit, which could lead to missing information.

2. **Tokenization Limits**: 
   Every model has a limit to how many tokens (a token being a fragment of a word or full word) it can handle at once. For GPT-4, the token limit is around 8,000 tokens for GPT-4 base, and for GPT-4 Turbo, it can handle up to 128,000 tokens in some instances (though specific use cases may vary). These limits mean that if you provide a document exceeding this token count, the model won't process the entire document simultaneously. Instead, it could return responses from portions that fit within the token limit or based on the latest input provided.

3. **Hallucinations**: 
   Hallucinations in AI occur when the model generates outputs that sound convincing but aren’t based on the input data. In the case of large documents, if the model seems to respond to information that wasn’t explicitly included in the most recent prompt (or didn't fit within the token limit), it could be hallucinating based on what it "thinks" is relevant rather than actual context processing. So, the outputs would be based on partial data or a synthesized understanding of the subject matter.

4. **Segmented Processing**: 
   If your earlier interactions involved splitting the document into manageable chunks, GPT could have accurately processed each portion one at a time and then compiled the results. However, the model couldn't process 300 pages in one go. The impression of full-document processing might come from how the sections were summarized and connected across multiple turns of conversation.

In short, earlier outputs weren't necessarily hallucinations but were based on portions of the text the model could process. The tokenization limit would still have been a factor, even if it wasn’t immediately evident, and the model might have selectively generated responses based on the input at hand.