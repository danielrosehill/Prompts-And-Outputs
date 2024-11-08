---
title: "Verifying that GDELT is still in existence"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, GDELT is operational and can be used for your security monitoring use case. It provides real-time analysis of global news, updates every 15 minutes, and uses powerful natural language processing and data mining techniques to analyze news from over 100 languages. You can use GDELT's API to search news reports for your security-related keywords and set up alerts for different severity levels. The API allows filtering based on location, publication language, and tone, which would be useful for focusing on Israel- and Jerusalem-specific events.

To test this out, you can create a GDELT query using the [GDELT API](https://blog.gdeltproject.org/gdelt-2-0-our-global-knowledge-graph-gets-a-new-api/). Here's an example query to look for recent news related to one of your keywords:

```bash
https://api.gdeltproject.org/api/v2/doc/doc?query="Rocket attack Jerusalem"&mode=ArtList&format=json
```

This will fetch articles related to rocket attacks in Jerusalem. You can substitute the keyword for others in your array and tweak parameters like the `mode` (e.g., `ArtList` for article lists or `TimelineVolRaw` for raw article counts).

You can experiment with this approach and build a monitoring system that triggers alerts based on the severity of the keywords detected.

Yes, you should URL-encode the query parameter to ensure that special characters like spaces are properly handled. Here’s the encoded version of the query URL for the **"Rocket attack Jerusalem"** example:

```bash
https://api.gdeltproject.org/api/v2/doc/doc?query=Rocket%20attack%20Jerusalem&mode=ArtList&format=json
```

This version encodes the space as `%20`, which ensures the query works correctly when making requests to the API. You can substitute the `"Rocket attack Jerusalem"` part with any other keyword or phrase from your array and encode it similarly.