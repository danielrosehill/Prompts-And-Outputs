---
title: "Hosted media screens projects"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Are there any self hostable projects that are specialised in creating media dashboards with custom grid views of multiple live media streams (TV channels). The streams I'd like to embed are simply delivered as web sites rather than actual media streams. And I'd like to embed a couple of other items in a display too

# Output

If you're looking to create a media dashboard that can display multiple live media streams delivered as embedded websites, along with other customizable elements, here are some self-hostable options that can support a grid layout for web content:

### 1. **Smashing (formerly Dashing)**
   - **Overview**: Smashing is an open-source dashboard framework that allows you to create custom dashboards with widgets. It can display web content, making it well-suited for embedding live news streams that are accessed as web pages.
   - **Features**: Smashing supports embedding HTML widgets, including iframes, which means you can easily embed live media streams from websites. You can also add other elements like RSS feeds, images, or custom HTML.
   - **Customization**: It offers flexible layout options, allowing you to create custom grid views of your embedded content. You can manage everything via simple widget configurations, with Ruby being the primary language for customizations.
   - **Community & Support**: Smashing has an active GitHub community, and since it’s a fork of Dashing, there are plenty of tutorials and community resources available.

### 2. **Grafana (with the Text/HTML Panel)**
   - **Overview**: While typically used for data visualization, Grafana supports embedding web content through the Text/HTML panel, making it possible to create custom dashboards that include embedded websites.
   - **Features**: Grafana’s grid layout is highly customizable, allowing you to embed multiple web-based live streams alongside other visualizations or alerts. You can add HTML and iframes, providing flexibility for different types of embedded content.
   - **Customization**: Grafana is highly flexible, so you can arrange your media streams in a grid format alongside other items like images, text, and real-time data visualizations. It’s particularly useful if you want to blend media streams with other metrics or monitoring elements.
   - **Community & Support**: Grafana has a large and active community, with extensive documentation and plugins, which makes customization and troubleshooting easier.

### 3. **MagicMirror²**
   - **Overview**: MagicMirror² is an open-source platform originally developed for smart mirrors but is highly customizable and can be repurposed for media dashboards. It supports displaying web content and can be hosted on a Linux server.
   - **Features**: MagicMirror² has a rich ecosystem of modules, and you can embed web pages or live media streams via iframes. It supports custom layouts, which can be configured to show multiple streams in a grid format.
   - **Customization**: MagicMirror² is modular and highly customizable. You can easily integrate additional modules, such as weather widgets or calendar feeds, alongside your media streams. Layouts are defined in configuration files, so you have control over positioning and appearance.
   - **Community & Support**: MagicMirror² has an active community, with a large library of user-contributed modules and frequent updates. The forums and GitHub repository offer support and ideas for customization.

### 4. **Info-beamer**
   - **Overview**: Info-beamer is an open-source digital signage software that is well-suited for embedding web content. It can handle multiple web-based streams in a grid layout, and you can customize the dashboard to include additional items as well.
   - **Features**: Info-beamer allows you to build custom layouts with iframes for embedding websites. It’s lightweight and can handle multiple streams efficiently, making it ideal for continuous display.
   - **Customization**: Layouts can be configured via Lua scripts, giving you control over the placement and arrangement of web streams. It also supports overlays, so you can add other items like text, images, or custom HTML content.
   - **Community & Support**: Info-beamer is popular in the Raspberry Pi community, with active forums and good documentation available.

### 5. **Dashy**
   - **Overview**: Dashy is a self-hosted dashboard that can be configured to display web content, including iframes and embedded websites. It’s designed for creating visually appealing and highly customizable dashboards.
   - **Features**: Dashy supports custom HTML, making it possible to embed live news streams and other elements directly within a grid layout. You can also add widgets for additional items, such as weather, RSS feeds, or custom alerts.
   - **Customization**: Dashy’s configuration file is YAML-based, which allows for easy modifications and custom layouts. It’s particularly focused on visual customizability, so you can create a polished, grid-based display.
   - **Community & Support**: Dashy has a growing GitHub community, and its focus on easy configuration makes it accessible for users with minimal coding knowledge.

Each of these platforms provides the flexibility to embed web-based media streams and arrange them in a grid alongside other elements, making them ideal for a custom media dashboard tailored to your needs. For ease of use and extensive customization, **Grafana** and **Smashing** are particularly strong options, while **MagicMirror²** and **Dashy** offer visually appealing interfaces that are easy to adapt for varied content.