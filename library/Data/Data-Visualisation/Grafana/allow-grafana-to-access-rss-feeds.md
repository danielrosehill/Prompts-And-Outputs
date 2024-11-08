---
title: "Allow Grafana to access RSS feeds"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, the **502 Bad Gateway error** you're encountering is likely caused by your **Cloudflare Access rule** blocking Grafana from fetching external resources like RSS feeds. When Cloudflare Access is enabled, it enforces access control by blocking requests from unauthenticated sources (such as Grafana trying to pull in external data like RSS feeds), leading to this error.

### How to Allow Grafana to Fetch RSS Feeds Behind Cloudflare Access:
You can resolve this by allowing your Grafana instance to bypass Cloudflare Access while it fetches external resources, like RSS feeds, without exposing the entire application to the public.

Here are a few approaches to solve this:

#### 1. **Bypass Cloudflare Access for Specific API Requests**:
You can configure Cloudflare to allow unauthenticated access to specific API endpoints or external resource-fetching actions by adding a **bypass rule**:
   - Go to your **Cloudflare Access dashboard**.
   - Under **Access Rules**, add a **bypass rule** that allows unauthenticated access to the URLs or services that fetch external RSS feeds.
   - Example: Allow requests to the plugin or RSS fetching services used by Grafana.

#### 2. **Service Token for API Requests**:
Create a **Cloudflare Service Token** for the specific requests that Grafana makes when it fetches external resources. This way, Grafana can authenticate via a token while fetching RSS feeds:
   - Go to **Cloudflare Access** and create a **Service Token**.
   - Add the service token as a header in Grafana’s RSS fetching requests to authenticate those without requiring user interaction.

#### 3. **Configure IP Whitelisting**:
You could configure **Cloudflare Access** to allow requests coming from the IP address of your Grafana instance without requiring authentication. This way, Grafana will be able to fetch external resources:
   - Under **Firewall Rules** in Cloudflare, create an **allow rule** for the IP address of the server hosting Grafana.

#### 4. **Custom Cloudflare Workers for API Calls**:
Alternatively, you can use **Cloudflare Workers** to handle the RSS fetching on behalf of Grafana. The worker can fetch the feed and return the data to Grafana:
   - Create a Cloudflare Worker that makes the request to the external RSS feed.
   - Grafana will query the Worker endpoint, and the worker can handle the request behind Cloudflare.

Each of these methods ensures that your Grafana dashboard can still fetch RSS feed data while keeping your application behind Cloudflare Access for security purposes.