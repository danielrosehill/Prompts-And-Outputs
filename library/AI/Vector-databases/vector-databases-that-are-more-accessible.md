---
title: "Vector databases that are more accessible"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I was under the impression that vector databases are very expensive. Can you think of some ways in which this project could be designed affordably?

# Output

You're right to be concerned about costs, but there are actually several affordable ways to implement vector database functionality for the Output Hub project. Here are some suggestions to keep costs down while still leveraging vector search capabilities:

1. Use PostgreSQL with pgvector extension:
PostgreSQL, which you're already planning to use, has a free extension called pgvector that adds vector similarity search capabilities. This allows you to store and query vector embeddings directly in your existing PostgreSQL database without needing a separate vector database.

Key benefits:
- No additional infrastructure costs
- Integrated with your existing database
- Open-source and free to use

2. Utilize Chroma DB:
Chroma is an open-source, lightweight vector database that's designed to be easy to set up and use. It can be run embedded within your application or as a small separate service.

Key benefits:
- Open-source and free
- Low resource requirements
- Easy to integrate with Python applications

3. Consider Qdrant:
Qdrant is an open-source vector database that offers a free self-hosted option. It's designed to be efficient and can run on modest hardware.

Key benefits:
- Open-source with a free self-hosted option
- Good performance on limited resources
- Supports filtering alongside vector search

4. Leverage Milvus:
Milvus is a popular open-source vector database that can be self-hosted for free. While it's more feature-rich than some alternatives, it can still be run affordably on modest hardware for smaller projects.

Key benefits:
- Open-source and free for self-hosting
- Scalable from small to large deployments
- Active community and good documentation

5. Use vector search capabilities in MongoDB:
If you're open to using MongoDB instead of PostgreSQL, it now offers vector search capabilities in its free Community Edition.

Key benefits:
- Integrated vector search in a full-featured database
- No need for a separate vector database
- Free Community Edition available

Implementation approach:

1. Start with PostgreSQL + pgvector:
   - This is likely the most cost-effective starting point, as it requires no additional infrastructure.
   - Use pgvector to store embeddings of your prompts and outputs.
   - Implement vector similarity search queries directly in your PostgreSQL database.

2. If you need more advanced vector search features:
   - Consider deploying Chroma DB or Qdrant alongside your PostgreSQL database.
   - Use these for vector search while keeping other data in PostgreSQL.
   - This split approach allows you to optimize each system for its strengths.

3. Scale up as needed:
   - As your project grows, you can evaluate whether to move to a more robust solution like Milvus or a cloud-hosted vector database service.

By starting with these affordable options, you can implement vector search capabilities in the Output Hub project without incurring significant additional costs. As the project scales and if more advanced features are needed, you can always migrate to more powerful solutions in the future.

 




## Extracted Prompts
[[Prompts/Vector databases that are more accessible.md#Prompt 1|Prompt 1]]
