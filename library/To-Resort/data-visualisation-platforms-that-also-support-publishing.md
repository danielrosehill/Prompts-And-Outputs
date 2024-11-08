---
title: "Data visualisation platforms that also support publishing"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Summary of your prompt**: You're interested in whether any of the recommended frontends can do more than just display visualizations—specifically, you want platforms that allow you to create, manage, and publish visualizations, functioning as data publishing platforms or data visualization CMSes. You're looking for self-hostable options.

Here are some **self-hostable data publishing platforms** or **data visualization CMSes** that allow both the creation and publishing of interactive data visualizations:

### 1. **Superset (Apache Superset)**
   - **Description**: Apache Superset is a modern, open-source platform for creating, exploring, and sharing interactive data visualizations. It functions as both a **visualization creation tool** and a **publishing platform**.
   - **Features**:
     - Full dashboard and visualization creation capabilities with support for multiple chart types, including geospatial visualizations.
     - Simple interface for non-technical users to build and publish charts.
     - Highly interactive and customizable charts.
     - **Publishing**: Superset supports publishing and sharing dashboards with public or restricted access. It has a "public link" feature for sharing visualizations without user authentication.
     - It integrates natively with PostgreSQL and other databases.
   - **Why it’s a fit**: Apache Superset is a full-fledged platform that allows you to not only create but also **publish** interactive visualizations with basic navigation features.
   - **Self-hosting**: Can be deployed on your own infrastructure (supports Docker for easy deployment).

   **Example stack**:
   - Backend: Apache Superset
   - Database: PostgreSQL
   - Frontend: Superset’s built-in interface for chart creation, management, and publishing

### 2. **Metabase**
   - **Description**: Metabase is a business intelligence tool that lets you create visualizations directly from your data sources and provides features for managing and **publishing** dashboards.
   - **Features**:
     - A drag-and-drop interface to create visualizations, queries, and dashboards.
     - User-friendly for both technical and non-technical users.
     - **Publishing**: Metabase allows dashboards to be shared publicly (without authentication) or embedded within other websites. It also supports scheduling reports and auto-updating dashboards.
     - Supports PostgreSQL and other databases.
   - **Why it’s a fit**: Metabase works well as a **data visualization CMS**, offering easy publishing features and embedding options, along with robust visualization creation tools.
   - **Self-hosting**: Metabase can be self-hosted using Docker or deployed on various cloud platforms.

   **Example stack**:
   - Backend: Metabase (connected to PostgreSQL)
   - Database: PostgreSQL
   - Frontend: Metabase's dashboarding and publishing tools

### 3. **Kibana (Elasticsearch Stack)**
   - **Description**: Kibana is the visualization layer of the Elastic Stack, designed for analyzing and visualizing data stored in Elasticsearch but can be configured to connect with PostgreSQL via connectors.
   - **Features**:
     - Highly customizable visualizations, including geospatial data and real-time data feeds.
     - Interactive dashboards with user-defined filters.
     - **Publishing**: Dashboards and visualizations can be shared via embedded links or public URLs, allowing you to publish visualizations without user authentication.
     - Flexible for setting up interactive, live dashboards.
   - **Why it’s a fit**: Kibana is a more technical option, but its flexibility and ability to publish visualizations to the public make it a suitable **data visualization publishing platform**.
   - **Self-hosting**: Kibana is self-hostable alongside the Elastic Stack or connected to PostgreSQL via plugins.

   **Example stack**:
   - Backend: Kibana (Elastic Stack or PostgreSQL connector)
   - Database: PostgreSQL
   - Frontend: Kibana's built-in publishing and embedding features

### 4. **Redash**
   - **Description**: Redash is an open-source tool designed for querying databases and visualizing the results. It provides a simple way to create visualizations and share them publicly.
   - **Features**:
     - Provides an easy-to-use query editor for PostgreSQL and other databases.
     - Supports many visualization types (charts, tables, maps).
     - **Publishing**: Redash supports public sharing of dashboards and visualizations. It also allows embedding of dashboards into other websites, making it useful for publishing visualizations.
   - **Why it’s a fit**: Redash combines query building and visualization with the ability to **publish and share** data visualizations. It's less customizable than Superset or Metabase but simpler to use.
   - **Self-hosting**: Redash can be self-hosted using Docker, or deployed on various cloud services.

   **Example stack**:
   - Backend: Redash (connected to PostgreSQL)
   - Database: PostgreSQL
   - Frontend: Redash's dashboard and sharing features

### 5. **Nocodb**
   - **Description**: Nocodb is an open-source Airtable-like platform that connects to PostgreSQL and other databases. It turns your database into a smart spreadsheet interface where you can create and publish visualizations.
   - **Features**:
     - Create interactive charts, tables, and dashboards from your PostgreSQL database.
     - **Publishing**: Nocodb allows you to create and share public links to your dashboards, and you can embed these on any website. It also supports role-based access if you need limited access.
     - User-friendly, no-code interface for building data visualizations.
   - **Why it’s a fit**: Nocodb is a great **data publishing platform** for teams that want a no-code interface to manage data and publish dashboards easily. It also integrates well with different data sources.
   - **Self-hosting**: Easily self-hostable using Docker.

   **Example stack**:
   - Backend: Nocodb (connected to PostgreSQL)
   - Database: PostgreSQL
   - Frontend: Nocodb’s interface with public links or embedded dashboards

### 6. **Grafana with PostgreSQL**
   - **Description**: Grafana is a popular open-source platform for monitoring and visualizing time-series data, but it also works great for **publishing** static or real-time dashboards.
   - **Features**:
     - Integrates with PostgreSQL for querying data.
     - **Publishing**: Grafana allows dashboards to be shared publicly or embedded in other websites, with no need for user authentication.
     - Supports rich interactivity, including maps and real-time data feeds.
   - **Why it’s a fit**: Grafana is a good choice if you want a fully-featured **dashboard publishing platform** that supports live data visualizations, custom theming, and public sharing options.
   - **Self-hosting**: Grafana is self-hostable and supports Docker for easy deployment.

   **Example stack**:
   - Backend: Grafana (connected to PostgreSQL)
   - Database: PostgreSQL
   - Frontend: Grafana's dashboard interface and publishing tools

---

### Recommended Option:
If you're looking for a **self-hostable data publishing platform** that supports creating, managing, and publishing visualizations, **Apache Superset** is one of the best fits because:
- It allows full control over both the backend and frontend.
- It supports interactive dashboards, geovisualizations, and real-time data.
- You can share dashboards publicly, with or without authentication.
- It's highly customizable for UI and navigation elements.

**Metabase** and **Nocodb** are also excellent, simpler-to-use alternatives if you prefer low-code solutions while still offering public sharing and dashboard publishing capabilities.