---
title: "Automatically read RSS feed at fixed interval"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt
I'm looking for a tool that can read out loud the latest X items from an RSS feed at a fixed interval. Do any such tools exist? (to be clear - I'm looking for text to speech - it should automatically read out the latest headlines)

# Output

Yes, there are tools that can automatically read out loud the latest items from an RSS feed at fixed intervals using text-to-speech (TTS) on Android. Here are some options you can consider:

### 1. **Tasker + AutoVoice**
   - **Tasker** combined with **AutoVoice** can automate this task by fetching the RSS feed content, parsing it, and using TTS to read it aloud.
   - You can set up a profile to run at a specific interval, fetch the RSS feed, extract the latest headlines, and use Tasker’s **Text-to-Speech** action to read them out loud. You may need a plugin like **AutoWeb** to parse the RSS feed.

### 2. **Voice RSS Feeds Reader Apps**
   - Some RSS reader apps support TTS functionality:
     - **Voice Reader RSS**: This app allows you to listen to RSS feed items using TTS. You can configure it to automatically read out new headlines at fixed intervals.
     - **Speech Central**: This app can fetch RSS feeds and read them aloud. You can set it up to check for new items periodically, and it will read the latest headlines using TTS.

### 3. **Podcast and RSS Feed Reader Apps with TTS**
   - Apps like **Podcast Addict** support RSS feeds and have a built-in TTS option. While it’s typically used for podcasts, you can add an RSS feed and set it to read the text of each item aloud.
   - **Voice Dream Reader**: Though primarily an e-book and PDF reader, Voice Dream Reader supports RSS feeds and has customizable TTS capabilities, which can be configured to read out new feed items.

### 4. **Google Assistant and IFTTT**
   - You can use **IFTTT** to fetch RSS feed headlines and send them to **Google Assistant** as a notification. While it’s not as automated, you can use a custom Google Assistant routine to read out the feed items on command, allowing for TTS reading.

### 5. **Custom Script with Automate**
   - **Automate** (by LlamaLab) is an app similar to Tasker that supports more straightforward scripting. You can create a flow that fetches RSS feeds at intervals, parses the headlines, and uses the built-in TTS to read them out.
   - This might require some setup with HTTP Get and Text-to-Speech blocks but allows for flexible, fully automated reading.

 