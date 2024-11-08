---
title: "Sample Python script for text automation"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*




please provide a demonstration python script which could be used to summarise a long report<br>

**ChatGPT**<br>

Certainly! Here's a simple Python script that uses the OpenAI GPT-3 model to summarize a long report. This script assumes you have access to the OpenAI API.

    python

Copy code

`import openai # Replace 'your_openai_api_key' with your actual OpenAI API key openai.api_key = 'your_openai_api_key' def summarize_report(report_text, max_tokens=150): """ Summarizes a long report using OpenAI GPT-3. Parameters: report_text (str): The full text of the report to summarize. max_tokens (int): The maximum number of tokens in the summary. Returns: str: The summarized text. """ try: response = openai.Completion.create( engine="text-davinci-003", # Specify the model you want to use prompt=f"Summarize the following report:\n\n{report_text}\n\nSummary:", max_tokens=max_tokens, n=1, stop=None, temperature=0.7 ) summary = response.choices[0].text.strip() return summary except Exception as e: return f"An error occurred: {e}" # Example usage report = """ Your long report text goes here. It can be multiple paragraphs and quite lengthy. The script will generate a summary of this content. """ summary = summarize_report(report) print("Summary:") print(summary)`

### Instructions:

1.  **API Key**: Replace `'your_openai_api_key'` with your OpenAI API key. You can obtain this key by signing up on the [OpenAI website](https://beta.openai.com/signup/).
    
2.  **Input Text**: Replace the `report` variable's content with the actual text of the report you want to summarize.
    
3.  **Max Tokens**: Adjust the `max_tokens` parameter to control the length of the summary. The more tokens you allow, the longer the summary can be.
    
4.  **Temperature**: The `temperature` parameter controls the randomness of the output. A lower value (e.g., 0.2) makes the output more deterministic, while a higher value (e.g., 0.8) makes it more creative.
    
5.  **Run the Script**: Execute the script to generate a summary of the report.
    

### Note:

This script requires an internet connection and access to the OpenAI API. If you encounter any issues or need additional customization, you can adjust the parameters accordingly.

4o

please revise the output to include a cost estimate on summarising a 10 page PDF

ChatGPT

To estimate the cost of summarizing a 10-page PDF report using the OpenAI API, we need to consider the following:

1.  **Character and Token Count**: OpenAI charges are based on the number of tokens processed. A token roughly corresponds to 4 characters of English text, and 1,000 tokens cost a certain amount depending on the model used.
    
2.  **Model Used**: The pricing may vary depending on whether you use models like `text-davinci-003` or `text-curie-001`.
    

For the purpose of this example, let's assume:

*   Each page contains roughly 500 words.
    
*   An average word length is 5 characters.
    
*   The model used is `text-davinci-003`.
    

### Estimation Calculation

1.  **Word Count**: 10 pages \* 500 words = 5,000 words
    
2.  **Character Count**: 5,000 words \* 5 characters/word = 25,000 characters
    
3.  **Token Count**: 25,000 characters / 4 = 6,250 tokens (approximate)
    

**Cost Calculation**: Assuming a cost of $0.06 per 1,000 tokens for `text-davinci-003`:

*   Cost for 6,250 tokens: 6,250 tokens/1,000×0.06 USD=0.375 USD6,250 \\text{ tokens} / 1,000 \\times 0.06 \\text{ USD} = 0.375 \\text{ USD}6,250 tokens/1,000×0.06 USD=0.375 USD
    

Therefore, the estimated cost for summarizing a 10-page PDF report using `text-davinci-003` is approximately **$0.375**.

### Revised Python Script with Cost Estimate

    python

Copy code

`import openai # Replace 'your_openai_api_key' with your actual OpenAI API key openai.api_key = 'your_openai_api_key' def summarize_report(report_text, max_tokens=150): """ Summarizes a long report using OpenAI GPT-3. Parameters: report_text (str): The full text of the report to summarize. max_tokens (int): The maximum number of tokens in the summary. Returns: str: The summarized text. """ try: response = openai.Completion.create( engine="text-davinci-003", # Specify the model you want to use prompt=f"Summarize the following report:\n\n{report_text}\n\nSummary:", max_tokens=max_tokens, n=1, stop=None, temperature=0.7 ) summary = response.choices[0].text.strip() return summary except Exception as e: return f"An error occurred: {e}" # Example usage report = """ Your long report text goes here. It can be multiple paragraphs and quite lengthy. The script will generate a summary of this content. """ summary = summarize_report(report) print("Summary:") print(summary) # Cost estimate pages = 10 words_per_page = 500 characters_per_word = 5 tokens_per_character = 1/4 tokens = pages * words_per_page * characters_per_word * tokens_per_character cost_per_1000_tokens = 0.06 estimated_cost = (tokens / 1000) * cost_per_1000_tokens print(f"Estimated Cost: ${estimated_cost:.3f}")`<br>

### Key Considerations:

*   **Token Estimate**: The actual number of tokens can vary based on the content and formatting of the report.
    
*   **API Usage**: Ensure you have an API key and appropriate billing setup on OpenAI's platform.
    
*   **Cost Variance**: The cost may vary based on actual token usage and model choice.
    

This estimate provides a rough cost for the summarization task. The actual cost may differ slightly depending on the specifics of the text and the OpenAI pricing model.