---
title: "What could I use to display the Keplr frontend data then"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

So Keplr can't really be a self standing frontend on its own? If not can you give me a CMS that I can embed it into? in this case, the "CMS" would just be a wrapper for serving up visualisation pages

# Output

You're right—**Kepler.gl** isn't intended to be a **self-standing frontend**. It excels at **data visualization**, but you’ll need a CMS or web framework to wrap around it for a full-fledged site, allowing you to manage other content while embedding your Kepler.gl visualizations. Here are some CMS options where Kepler.gl can be embedded as part of a broader visualization project:

### 1. **Ghost (Headless CMS or Full CMS)**
   - **Why it's good**: **Ghost** is a modern CMS that's lightweight, fast, and markdown-friendly. It can act as either a **headless CMS** or a traditional CMS. You can embed **Kepler.gl** maps within Ghost posts or pages using the custom HTML block feature.
   - **How to use**: Create posts with custom code or embeds for Kepler.gl. You can also extend Ghost with custom themes or templates for better integration of visualizations.
   - **Pros**:
     - Clean, modern CMS with built-in support for markdown.
     - Can act as a static site generator, allowing for fast load times.
   - **Website**: [Ghost](https://ghost.org/)

### 2. **Strapi (Headless CMS)**
   - **Why it's good**: **Strapi** is a highly flexible **headless CMS** that provides a powerful API to manage and serve content. You can use Strapi to manage content and integrate **Kepler.gl** by embedding the visualizations into pages that are built using the CMS.
   - **How to use**: Strapi manages the backend API, while your frontend could be powered by something like **Next.js** or **Gatsby**. The Kepler.gl maps can be integrated by fetching data from Strapi's API or embedding static visualizations within the frontend.
   - **Pros**:
     - Highly customizable and flexible.
     - Supports easy data management and content publishing.
   - **Website**: [Strapi](https://strapi.io/)

### 3. **WordPress (Classic CMS or Headless with REST API)**
   - **Why it's good**: **WordPress** is a versatile CMS that can handle content management and visual embedding. With **custom HTML blocks** or plugins, you can embed Kepler.gl visualizations directly into WordPress pages or posts.
   - **How to use**: Create custom posts or pages that include Kepler.gl visualizations through the block editor (Gutenberg) or custom shortcodes. If using **headless WordPress**, the frontend could be built using **Gatsby** or **Next.js**, while the WordPress REST API delivers the content.
   - **Pros**:
     - Large ecosystem and flexibility for content publishing.
     - Extensive support for embedding third-party visualizations.
   - **Website**: [WordPress](https://wordpress.org/)

### 4. **Netlify CMS (Static Site Generator + Headless CMS)**
   - **Why it's good**: **Netlify CMS** is a lightweight, **open-source CMS** that integrates well with static site generators like **Gatsby** or **Hugo**. This setup allows you to manage content while embedding Kepler.gl visualizations in the pages or posts.
   - **How to use**: Manage content using Netlify CMS, and embed **Kepler.gl** visualizations using custom HTML blocks or markdown. The frontend can be powered by **Gatsby** to combine both static content and dynamic data visualizations.
   - **Pros**:
     - Ideal for static sites with dynamic components.
     - Easy integration with Git-based workflows.
   - **Website**: [Netlify CMS](https://www.netlifycms.org/)

### 5. **Contentful (Headless CMS with API Integration)**
   - **Why it's good**: **Contentful** is a **headless CMS** that allows you to manage content and serve it through an API. You can use **Contentful** to manage the rest of your site's content and integrate Kepler.gl visualizations into your frontend by pulling dynamic data via the API.
   - **How to use**: Set up your content in Contentful and create API-driven pages that embed Kepler.gl visualizations. The frontend can be built using **Next.js** or **Gatsby** to display the visualizations alongside the rest of your content.
   - **Pros**:
     - Highly scalable and flexible for content-driven websites.
     - Strong API integration for embedding external visualizations.
   - **Website**: [Contentful](https://www.contentful.com/)

### Conclusion:
- **Ghost** or **WordPress** would be great if you want a full CMS for managing not only visualizations but also blog posts, articles, and other content.
- **Strapi** or **Contentful** work well if you're looking for a **headless CMS** to serve up content via API to a custom frontend (like **Next.js** or **Gatsby**) where you can integrate Kepler.gl visualizations.

By embedding Kepler.gl into one of these CMS platforms, you'll have the ability to manage content and visualizations together, making it a more cohesive and **user-friendly experience** for your audience. Let me know which platform resonates most with you!