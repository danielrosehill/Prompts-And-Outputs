---
title: "Validating a batch of URLs"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

is there any way to provide a batch of URLs and validate them? Many of these don't work

Yes, there's a way to validate a batch of URLs to determine if they are accessible and functioning correctly. Here’s how you can do it using a Python script:

### Python Script to Validate URLs

This script will take a list of URLs and check whether each URL is accessible (i.e., returns a successful HTTP status code).

1. **Input:** Provide the list of URLs to the script (as a text file or directly in the script).
2. **Output:** The script will print which URLs are valid and which are not.

```python
import requests

# List of URLs to validate
urls = [
    "https://www.bbc.com/news/world/middle_east",
    "https://www.theguardian.com/world/israel",
    "https://www.cnn.com/middle-east",
    # Add more URLs here
]

# Function to validate URLs
def validate_urls(url_list):
    for url in url_list:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                print(f"VALID: {url}")
            else:
                print(f"INVALID: {url} (Status Code: {response.status_code})")
        except requests.RequestException as e:
            print(f"INVALID: {url} (Error: {e})")

# Validate the URLs
validate_urls(urls)
```

### How This Script Works:
1. **Input List**: You need to add your URLs to the list (`urls`).
2. **Requests Library**: The script uses Python's `requests` library to make HTTP GET requests.
3. **Timeout**: The script includes a `timeout` parameter (10 seconds) to avoid waiting too long for unresponsive URLs.
4. **Response Status**:
   - URLs that return **status code 200** (OK) are considered valid.
   - If the status code is anything other than 200 or if an error occurs (e.g., timeout, connection error), the URL is marked as invalid.

### How to Use:
- **Install Requests**: If you haven't already, you can install the `requests` library using:
  ```sh
  pip install requests
  ```
- **Run the Script**: After saving the script to a `.py` file, you can run it using Python:
  ```sh
  python validate_urls.py
  ```

### Notes:
- The **status code** helps determine if the page is valid:
  - **200**: Successful request.
  - **404**: Page not found.
  - **403**: Forbidden (access restricted).
  - Other status codes could indicate redirection, server issues, etc.
- You can also write the results to a file instead of printing them, depending on your needs.

If you provide me with the URLs, I could help run a similar validation in Python, or you can run the script locally to validate them yourself.