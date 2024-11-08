---
title: "Get Hebrew fonts from Google fonts API"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Does Google Fonts have an API? And if so is there a way to legitimately extract a list of fonts in the Hebrew language? That's all I'm trying to do!

# Output

Yes, Google Fonts does have an API that allows you to access metadata for all font families served by Google Fonts. This API can be used to extract a list of fonts, including those in the Hebrew language subset.

### How to Use the Google Fonts API

1. **API Key**: First, you need to acquire an API key from the Google Cloud Platform. This key will be used to authenticate your requests to the Google Fonts API.

2. **API Request**: You can make a request to the Google Fonts API endpoint to retrieve font data. The endpoint is:
   ```
   https://www.googleapis.com/webfonts/v1/webfonts?key=YOUR-API-KEY
   ```

3. **Filter by Subset**: To get fonts that support Hebrew, you can filter the results by the `subset` parameter. Unfortunately, the subset filtering is not directly available in a single API call, but you can filter the JSON response manually after retrieving it.

4. **Sample Code**:
   Here is an example of how you might use Python to fetch and filter fonts that support Hebrew:

   ```python
   import requests

   # Replace 'YOUR-API-KEY' with your actual API key
   api_key = 'YOUR-API-KEY'
   url = f'https://www.googleapis.com/webfonts/v1/webfonts?key={api_key}'

   response = requests.get(url)
   fonts_data = response.json()

   # Filter fonts that support Hebrew
   hebrew_fonts = [font for font in fonts_data['items'] if 'hebrew' in font['subsets']]

   # Print font names and their files
   for font in hebrew_fonts:
       print(f"Font Name: {font['family']}")
       print(f"Files: {font['files']}")
       print("\n")
   ```

5. **JSON Response**: The response from the API includes various details about each font family, such as:
   - `family`: The name of the font family.
   - `subsets`: A list of scripts supported by the family.
   - `variants`: Different styles available for the family.
   - `files`: URLs to download the font files.

By using this method, you can legitimately extract a list of fonts that support Hebrew from Google Fonts using their official API.
 