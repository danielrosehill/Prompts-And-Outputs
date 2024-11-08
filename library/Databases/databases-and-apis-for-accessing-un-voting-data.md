---
title: "Databases and APIs for accessing UN voting data"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

are there databases or APIs that list voting records at major international fora like the UN and which can provide free and historical data of same?

# Output

Yes, there are several **databases** and **APIs** that provide access to voting records at major international fora, such as the **United Nations (UN)**, and many of these resources offer free and historical data:

### 1. **UN Digital Library**
   The **UN Digital Library** provides access to voting records from the **UN General Assembly (UNGA)** and **Security Council**. It includes data from 1946 onwards and allows you to explore the voting history of different countries, including roll call votes. The library is searchable, and while there is no direct API for this data, it is accessible via their online portal.

   - **Website**: [UN Digital Library](https://digitallibrary.un.org)

### 2. **UNdata API**
   The **UNdata API** provides access to a wide range of UN statistics, including voting data. It allows developers to query datasets using REST or SOAP services and return results in various formats like JSON, XML, or CSV. This API is useful for retrieving **dynamic, programmatic access** to UN data, and it's free to use, though some setup is required to work with specific datasets.

   - **Documentation**: [UNdata API](https://data.un.org/Host.aspx?Content=API)

### 3. **Harvard Dataverse (UN Votes Dataset)**
   The **Harvard Dataverse** hosts a dataset containing the **UN General Assembly voting records** from 1946 to recent years. This dataset, curated by Erik Voeten, includes information on how each country voted on various resolutions, along with additional metadata like vote descriptions and issue areas. You can download the dataset directly and integrate it with your own applications.

   - **GitHub Project**: [UN Voting Data on GitHub](https://github.com/dgrtwo/unvotes)
   - **Harvard Dataverse**: [UN Votes Dataset](https://dataverse.harvard.edu)

### 4. **UN Votes Package for R**
   The **unvotes** R package provides an easy-to-use interface for accessing **UN General Assembly voting data**. It includes detailed voting records of countries, making it a great option for researchers or developers using **R**. You can easily query and analyze the voting records programmatically.

   - **Installation and Use**: Available on CRAN and GitHub for R users.
   - **GitHub Repository**: [UN Votes R Package](https://github.com/dgrtwo/unvotes)

### 5. **Other Data Sources**
   - **World Politics Data Lab** also provides insights and analysis of **UN voting records**, focusing on member states' behavior and patterns at the General Assembly, Security Council, and other bodies.
   - **Al Jazeera** has visualized some UN voting data for specific issues like Palestinian conflict votes, which are derived from the **Harvard Dataverse** dataset.

By using these resources, you can access comprehensive **historical voting records** from the UN and use **APIs** or downloadable datasets for research or development purposes.