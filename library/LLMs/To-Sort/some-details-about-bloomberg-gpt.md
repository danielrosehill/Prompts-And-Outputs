---
title: "Some details about Bloomberg GPT"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'd love to learn more about bloomberg GPT. what features does it offer and how much does it cost to use? It is a local LLM? Are there licensing fees?

# Output

**BloombergGPT** is a proprietary large language model (LLM) specifically developed for the financial domain by Bloomberg. It features **50 billion parameters** and was trained using a combination of domain-specific financial data and general-purpose text data, resulting in a training set of over **700 billion tokens**. This mixed approach allows BloombergGPT to excel in finance-specific tasks while still maintaining competitive performance in more general NLP benchmarks. It was built with the intention of providing best-in-class results for various financial use cases, such as **sentiment analysis**, **financial question answering**, and **named entity recognition** relevant to the financial sector【213】.

### Features of BloombergGPT
- **Domain-Specific Expertise**: BloombergGPT has been trained on a comprehensive dataset named "FinPile," which consists of financial documents, news articles, financial filings, and other relevant resources collected by Bloomberg over several decades. This unique dataset ensures that the model is particularly effective at financial tasks.
- **Performance in Financial Applications**: It can be used for generating **Bloomberg Query Language (BQL)** outputs, making suggestions for **news headlines**, and analyzing large volumes of financial data, which sets it apart from general-purpose models【213】.

### Deployment and Licensing
- **Local LLM**: BloombergGPT is **not a local model**; instead, it is a proprietary service intended primarily for use through Bloomberg's own infrastructure, such as the **Bloomberg Terminal**.
- **Access and Cost**: The model is proprietary, meaning that it is **not available for public use** or download as an independent package. Users need to access it through Bloomberg's professional services, like the **Bloomberg Terminal**, which has a high cost typically used by financial institutions. Specific costs are not publicly disclosed, but Bloomberg's services are generally on the more expensive side, aimed at enterprise clients rather than individual users【212】.
- **Licensing Fees**: Since BloombergGPT is proprietary, there are likely significant **licensing fees** associated with accessing it, especially since it integrates with other Bloomberg services for financial professionals.

### Alternatives for a Similar Use Case
If you’re interested in an open-source approach to financial language models, a project called **FinGPT** offers a community-driven and open-source framework that aims to create models similar to BloombergGPT. FinGPT focuses on democratizing financial NLP and provides tools for developing domain-specific models using financial data from public sources. This could be an attractive option if you prefer an open model with more flexibility and without the high costs associated with proprietary solutions like BloombergGPT【212】.

BloombergGPT is highly specialized and effective for financial professionals using Bloomberg's services, but for others interested in similar technology without the high costs and restrictions, exploring open-source options like FinGPT might be worthwhile.