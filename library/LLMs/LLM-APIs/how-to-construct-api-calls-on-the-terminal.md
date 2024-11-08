---
title: "How to construct API calls on the terminal"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

It seems the easiest way to test out an API is by just running a command in a terminal? Let's take the example you just provided. CURL will just output on the screen right? So what would I need to type to see if the call worked?

# Output

Yes, you can use **cURL** in a terminal to quickly test out an API call. cURL is a command-line tool that allows you to make HTTP requests and see the response directly in your terminal.

Here’s how you would structure a **cURL** command for the **Mediastack API** to search for the term "shooting attack":

### cURL Command:

```bash
curl "http://api.mediastack.com/v1/news?access_key=YOUR_API_KEY&keywords=shooting%20attack&date=2024-10-06"
```

### Breakdown of the Command:
- `curl`: This is the command-line tool to make the HTTP request.
- `"http://api.mediastack.com/v1/news?access_key=YOUR_API_KEY&keywords=shooting%20attack&date=2024-10-06"`: This is the full URL you are querying. The parameters include:
  - `access_key`: Your personal API key from Mediastack (replace `YOUR_API_KEY` with your actual key).
  - `keywords`: This is the term you are searching for, in this case, "shooting attack." The space is URL-encoded as `%20`.
  - `date`: You can specify the date of the event you're looking for in the format `YYYY-MM-DD`.

### Expected Output:
Once you run this command, the response from Mediastack should be displayed on your terminal screen in **JSON format**, which will contain a list of articles or news events that match your query. If successful, you should see a result like this:

```json
{
    "pagination": {
        "limit": 10,
        "offset": 0,
        "count": 3,
        "total": 3
    },
    "data": [
        {
            "author": "Times of Israel",
            "title": "Border cop killed, 10 wounded in terror shooting attack at Beersheba central bus station",
            "description": "A terror attack occurred in Beersheba...",
            "source": "Times of Israel",
            "published_at": "2024-10-06T12:00:00Z",
            "url": "https://www.timesofisrael.com/..."
        },
        ...
    ]
}
```

### If There’s an Error:
- If you don't get any results, check that your **API key** is correct and that the parameters are formatted correctly.
- If the query itself fails (e.g., API key is invalid or the service is down), cURL will usually output an error message explaining what went wrong.

### Tips for Using cURL:
- You can redirect the output to a file using the `-o` option if you don’t want the result to be shown on the screen:
  
  ```bash
  curl "http://api.mediastack.com/v1/news?access_key=YOUR_API_KEY&keywords=shooting%20attack&date=2024-10-06" -o output.json
  ```

This will save the response to a file named `output.json` in your current directory.

### Alternative Method:
If you're more comfortable with **Postman** or a similar API testing tool, you can also paste the URL into those tools and view the structured output without using a command-line interface. This might make parsing through the output a bit easier.