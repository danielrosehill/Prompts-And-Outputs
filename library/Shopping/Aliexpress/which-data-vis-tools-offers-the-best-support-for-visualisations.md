---
title: "Which data vis tools offers the best support for visualisations"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Summary of your prompt**: You are asking which self-hostable data visualization platform offers the widest variety of visualizations, and whether geovisualizations are supported.

Here’s an evaluation of several **self-hostable data visualization platforms** in terms of the variety of visualizations they offer and their support for **geovisualizations**:

### 1. **Apache Superset**
   - **Variety of Visualizations**:
     - **Wide range** of chart types, including bar charts, line charts, pie charts, time-series visualizations, and more advanced visualizations like heatmaps, Sankey diagrams, and treemaps.
     - Specialized visualizations such as word clouds, box plots, and pivot tables.
   - **Geovisualizations**: **Yes**, supported via `deck.gl` and `Mapbox`. You can create maps that show data by region, point, or even 3D visualizations (e.g., using latitude and longitude).
   - **Overall Flexibility**: Superset is **highly flexible** in the types of visualizations it offers, especially for analytics-heavy use cases and geospatial data.

### 2. **Grafana**
   - **Variety of Visualizations**:
     - Primarily focused on **time-series** data but supports many visualizations, including graphs, histograms, heatmaps, bar charts, tables, and single-stat panels.
     - Strong support for **real-time data**, making it great for monitoring and dynamic dashboards.
     - Custom visualization options via plugins.
   - **Geovisualizations**: **Yes**, supported through plugins like `Grafana Worldmap` and `Grafana Geomap`.
   - **Overall Flexibility**: Grafana is very flexible for **time-series and real-time data** visualizations, but it is more limited when it comes to non-temporal data and specialized charts compared to Superset or Plotly Dash.

### 3. **Plotly Dash**
   - **Variety of Visualizations**:
     - **Extensive** support for many kinds of visualizations, including standard charts (line, bar, scatter), advanced visualizations (histograms, box plots, 3D surface plots, and radar charts), and **highly customized** visualizations built with Python.
     - You can build practically any visualization you can code, including **interactive** charts, animations, and live-updating visualizations.
   - **Geovisualizations**: **Yes**, supported via `plotly` or `dash-leaflet`. It supports maps, choropleths, and more complex geospatial plots.
   - **Overall Flexibility**: Plotly Dash is one of the most flexible platforms, providing **high customization** and a vast array of visualization types. If you're comfortable coding in Python, you can extend its functionality significantly.

### 4. **Redash**
   - **Variety of Visualizations**:
     - Supports a decent range of visualizations like line charts, bar charts, pie charts, and tables.
     - Less variety compared to others like Superset and Plotly Dash, as it is more focused on simple visualizations for querying databases.
   - **Geovisualizations**: **Yes**, but limited. Redash supports basic geospatial visualizations like **maps** and choropleths, but it lacks advanced or interactive geospatial features.
   - **Overall Flexibility**: Redash is more focused on **querying and displaying data** and is less flexible in terms of customization and the variety of visualizations compared to Superset, Dash, or Grafana.

### 5. **Metabase**
   - **Variety of Visualizations**:
     - Basic visualizations such as line charts, bar charts, pie charts, and tables are well supported.
     - Limited support for more advanced or specialized visualizations compared to tools like Superset or Dash.
   - **Geovisualizations**: **Yes**, but limited. Metabase supports basic **map-based visualizations**, which can show data points on a map, but does not offer the rich interactivity or customization of Superset or Plotly Dash.
   - **Overall Flexibility**: Metabase is more suited for straightforward, **business intelligence-focused** visualizations and is not as flexible for complex or custom charts.

### 6. **Nocodb**
   - **Variety of Visualizations**:
     - Supports basic charts like bar graphs, line charts, and tables.
     - Primarily aimed at non-technical users, which limits the complexity of visualizations.
   - **Geovisualizations**: **Limited**. Nocodb supports basic geovisualizations, but it's not a platform built with advanced mapping in mind.
   - **Overall Flexibility**: Nocodb is more of a **no-code/low-code** platform, offering basic visualization types but not nearly as flexible or advanced as Superset, Dash, or Grafana for creating varied visualizations.

---

### Comparison of Visualization Variety and Geovisualization Support:

| Platform        | Variety of Visualizations             | Geovisualization Support         | Flexibility Level          |
|-----------------|---------------------------------------|----------------------------------|----------------------------|
| **Apache Superset** | Wide variety (heatmaps, Sankey, maps) | **Yes** (deck.gl, Mapbox)        | Very High                  |
| **Grafana**      | Strong for time-series, real-time data | **Yes** (Worldmap, Geomap plugins) | High (for time-series)     |
| **Plotly Dash**  | Extremely broad, custom visualizations | **Yes** (plotly, dash-leaflet)   | Extremely High (code-based) |
| **Redash**       | Decent, focused on simple charts      | **Yes**, but limited             | Moderate                   |
| **Metabase**     | Basic visualizations (line, bar, pie) | **Yes**, but basic               | Moderate                   |
| **Nocodb**       | Basic visualizations (tables, graphs) | **Limited**                      | Low                        |

---

### **Recommendation for Widest Variety**:
1. **Plotly Dash** provides the **widest possibilities** for creating highly customizable visualizations, including geovisualizations, as it is code-based and can render almost anything you can program.
   
2. **Apache Superset** offers a **broad range of pre-built visualizations** and excellent geospatial capabilities with deck.gl and Mapbox, making it a strong option for users who prefer a UI-driven approach but still want flexibility.

If you prioritize flexibility in visualizations and geovisualizations, **Plotly Dash** is your best option. If you prefer a platform with powerful built-in visualizations and an easy-to-use interface, **Apache Superset** is highly recommended.

# Additional data visualisation tools
**Summary of your prompt**: You would like additional self-hostable data visualization platforms with a wide variety of visualization options, including support for geovisualizations.

Here are **additional self-hostable platforms** that offer a variety of visualization options, including geovisualizations:

### 1. **Kepler.gl**
   - **Variety of Visualizations**:
     - **Specializes in geovisualizations**. You can create visualizations with large-scale geospatial datasets, such as heatmaps, point clusters, arcs, trips (trajectory data), and 3D visualizations.
     - Supports time-based visualizations to show data over time on a map.
   - **Geovisualizations**: **Yes**, it’s built for geospatial data. Supports Mapbox and large-scale datasets, with advanced geospatial features like 3D rendering and animation.
   - **Overall Flexibility**: While it is focused specifically on geospatial data, it is highly flexible within this domain, making it a great tool for interactive maps and large-scale location-based data.

   **Self-hosting**: Can be self-hosted as a web app using Docker or integrated into other platforms like Jupyter or Node.js environments.
   
   **Example stack**:
   - Backend: Kepler.gl (with or without server-side support, depending on needs)
   - Database: PostgreSQL or GeoJSON files
   - Frontend: Kepler.gl’s geospatial visualization engine

### 2. **Carto**
   - **Variety of Visualizations**:
     - Focused on **geospatial analysis** and visualization.
     - Supports interactive maps with data layers, point clusters, heatmaps, and real-time data visualizations.
     - Advanced spatial analysis tools like routing, proximity analysis, and custom geospatial modeling.
   - **Geovisualizations**: **Yes**, Carto is a specialized platform for geospatial data visualization. It integrates with Mapbox and other mapping engines to provide rich map-based visualizations.
   - **Overall Flexibility**: Extremely flexible for geovisualizations, especially for spatial analysis and interactive map creation.

   **Self-hosting**: Carto can be self-hosted as **Carto On-Premise**, providing full control over the platform and data.

   **Example stack**:
   - Backend: Carto On-Premise
   - Database: PostgreSQL (with PostGIS extension)
   - Frontend: Carto’s visualization and analysis tools

### 3. **Vega and Vega-Lite**
   - **Variety of Visualizations**:
     - Vega and Vega-Lite are declarative frameworks for creating a **wide variety of visualizations** using JSON-like syntax. They support line charts, bar charts, scatter plots, and more advanced visualizations like treemaps, radar charts, and force-directed graphs.
     - Interactive elements can be embedded, such as tooltips, filtering, zooming, and panning.
   - **Geovisualizations**: **Yes**, you can create maps and geospatial visualizations, including choropleths, symbol maps, and projections with layers.
   - **Overall Flexibility**: Vega offers **high flexibility** as you can customize almost any aspect of the visualization through code, making it one of the most powerful options for custom data visualizations.

   **Self-hosting**: Vega and Vega-Lite can be used within web applications, and you can host the platform yourself using Node.js, Jupyter notebooks, or other server-side frameworks.
   
   **Example stack**:
   - Backend: Node.js (for handling data queries and serving the visualizations)
   - Database: PostgreSQL
   - Frontend: Vega or Vega-Lite embedded in your website or app

### 4. **GeoServer**
   - **Variety of Visualizations**:
     - Specialized in **geospatial data visualization**. You can create interactive maps, layers, and other geographic features.
     - Supports advanced geospatial capabilities like feature and raster data.
   - **Geovisualizations**: **Yes**, GeoServer is built specifically for geospatial data. It supports multiple formats (e.g., GeoJSON, KML, WFS) and integrates with mapping libraries like Leaflet and OpenLayers.
   - **Overall Flexibility**: GeoServer is highly flexible in terms of geospatial visualization and data delivery, making it ideal for users needing robust geovisualizations and geographic data management.

   **Self-hosting**: GeoServer is fully self-hostable and integrates with PostGIS (PostgreSQL) for advanced geospatial queries and visualization.

   **Example stack**:
   - Backend: GeoServer (connected to PostGIS in PostgreSQL)
   - Database: PostgreSQL with PostGIS
   - Frontend: Leaflet, OpenLayers, or another mapping library for visualization

### 5. **Airflow + Data Studio**
   - **Variety of Visualizations**:
     - While Airflow is primarily for managing data pipelines, it can be combined with visualization platforms like **Google Data Studio** for a wide range of visualizations, including time-series, bar charts, and more.
     - Visualizations are defined and managed dynamically, making it great for building automated, complex visualization pipelines.
   - **Geovisualizations**: Supported when combined with a platform like Data Studio or Leaflet for maps, choropleths, and more.
   - **Overall Flexibility**: High flexibility for building custom, automated visualization workflows using Airflow’s powerful pipeline capabilities, though visualization options depend on the front-end tool used.

   **Self-hosting**: Airflow can be self-hosted, but you would need to integrate it with a self-hostable visualization tool (such as Grafana or Superset) for the front end.

   **Example stack**:
   - Backend: Airflow (for data pipeline orchestration)
   - Database: PostgreSQL
   - Frontend: Data Studio or another visualization layer (e.g., Superset or Dash)

### 6. **Leaflet (with custom setup)**
   - **Variety of Visualizations**:
     - Leaflet is an **open-source JavaScript library** for interactive maps. It supports basic map visualizations (points, polygons) and can be extended with plugins for more complex charts and map features like heatmaps and marker clustering.
     - Can be integrated with other charting libraries (e.g., D3.js, Plotly) to expand its visual capabilities.
   - **Geovisualizations**: **Yes**, built specifically for geospatial data. Leaflet is lightweight and supports interactive, customizable maps.
   - **Overall Flexibility**: Leaflet is highly flexible when combined with other libraries, making it ideal for custom geovisualizations and interactive mapping.

   **Self-hosting**: You can easily self-host Leaflet as part of a custom web application, connecting to a database like PostgreSQL with PostGIS for geospatial queries.

   **Example stack**:
   - Backend: Custom server (Node.js, Flask, etc.)
   - Database: PostgreSQL (with PostGIS for geospatial data)
   - Frontend: Leaflet, extended with libraries like D3.js for advanced visualizations

### 7. **D3.js**
   - **Variety of Visualizations**:
     - **Extremely powerful** for creating a broad range of custom visualizations, from standard charts (line, bar, scatter) to complex, interactive visualizations like network diagrams, chord diagrams, treemaps, and advanced animations.
     - D3.js offers **complete control** over visualizations and interactions, allowing for infinite possibilities in how data is represented.
   - **Geovisualizations**: **Yes**, D3.js supports full-fledged geospatial visualizations, including maps, projections, and topologies. You can create choropleths, symbol maps, and other complex geospatial visualizations.
   - **Overall Flexibility**: D3.js is **one of the most flexible** data visualization libraries available, but it requires significant coding expertise.

   **Self-hosting**: D3.js is a JavaScript library that can be used within any web application or platform, making it fully self-hostable.

   **Example stack**:
   - Backend: Custom server (Node.js, Flask, etc.)
   - Database: PostgreSQL
   - Frontend: D3.js (JavaScript) for fully custom visualizations

---

### **Additional Platforms Summary**:

| Platform        | Variety of Visualizations             | Geovisualization Support         | Flexibility Level          |
|-----------------|---------------------------------------|----------------------------------|----------------------------|
| **Kepler.gl**    | Specializes in geospatial visualization | **Yes**, advanced 3D maps         | High for geovisualizations  |
| **Carto**        | Wide range of geospatial tools         | **Yes**, advanced geospatial maps | High for geospatial data    |
| **Vega/Vega-Lite** | Very broad (declarative visualizations) | **Yes**, choropleths, symbol maps | Extremely High (code-based) |
| **GeoServer**    | Geospatial data and mapping           | **Yes**, full geospatial support  | High for GIS applications   |
| **Airflow + Data Studio** | Depends on front-end tool used  | **Yes**, through integrations    | Moderate to High            |
| **Leaflet**      | Focuses on maps but highly extendable | **Yes**, interactive maps         | High (with extensions)      |
| **D3.js**        | Extremely broad, full customization   | **Yes**, fully customizable maps  | Extremely High (code-based) |

---

### **Recommendation for Flexibility in Visualization**:
1. **D3.js** provides the **widest possibilities** for creating custom visualizations, including geovisualizations, but requires advanced coding