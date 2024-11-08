---
title: "Adding weather forecasts to Grafana dashboards"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, it is absolutely possible to add weather forecasting to **Grafana dashboards** by integrating data from weather APIs. Grafana’s flexibility allows you to connect to weather APIs, retrieve the relevant data (such as temperature, humidity, wind speed, and forecasts), and visualize it in various formats like graphs, single stats, or heatmaps.

### Steps to Add Weather Forecasting to Grafana

Here’s a guide to integrating weather forecasting into your Grafana dashboard:

### 1. **Choose a Weather API**
   Several free and paid weather APIs provide weather forecasts. Here are some popular ones:
   - **OpenWeatherMap**: Offers free and paid plans with access to current weather, forecasts, and historical data.
   - **WeatherAPI**: Provides global weather data, including current conditions, forecasts, and historical data.
   - **Visual Crossing**: Allows you to access weather forecasts and historical data.
   - **Meteomatics**: Offers highly detailed and accurate weather data, although it is a premium service.

   Example: **OpenWeatherMap** is a popular choice for free weather data:
   - **Free tier**: 60 API calls per minute, with 5-day forecast and current weather data.
   - **API Documentation**: [OpenWeatherMap API](https://openweathermap.org/api)

### 2. **Get Your API Key**
   - Sign up for an API key from the chosen weather service (for example, OpenWeatherMap).
   - Once you have your API key, you can use it to access weather data.

### 3. **Install a JSON Plugin in Grafana**
   - Grafana doesn’t directly support weather APIs, but you can use the **SimpleJSON** or **JSON API** plugin to fetch data from APIs.
   - To install the **JSON API** plugin:
     1. Go to **Configuration > Plugins** in Grafana.
     2. Search for **JSON API**.
     3. Click **Install** and follow the prompts.

### 4. **Set Up the Weather API Data Source**
   - After the plugin is installed, configure the data source to point to the weather API endpoint.
   - For OpenWeatherMap, the URL to retrieve the 5-day forecast would look like this:
     ```bash
     https://api.openweathermap.org/data/2.5/forecast?q=CityName&appid=YourAPIKey&units=metric
     ```
     Replace `CityName` with your desired location and `YourAPIKey` with your actual API key.

### 5. **Create a Panel for Weather Data**
   1. Go to **Dashboards** and click **New Dashboard**.
   2. **Add a new panel** and select the JSON API data source you created.
   3. Customize the query to pull the specific weather data you want to visualize (e.g., temperature, humidity, or wind speed).
   4. Choose the visualization type (e.g., single stat for current temperature, time series for forecasted temperatures, or gauges for real-time weather metrics).

### 6. **Visualize Weather Data**
   You can visualize weather data in several formats in Grafana:
   - **Time-Series Graphs**: Display forecasts such as temperature trends over the next 5 days.
   - **Single Stat**: Show current weather metrics like temperature, humidity, or wind speed.
   - **Gauge Panels**: Represent values like temperature, pressure, or UV index.
   - **Heatmaps**: Use heatmaps for hourly or daily temperature variation over time.

### Example: OpenWeatherMap Configuration for Grafana
Let’s say you want to display the current temperature for a city:
1. Use the following API call to get the current weather:
   ```bash
   https://api.openweathermap.org/data/2.5/weather?q=CityName&appid=YourAPIKey&units=metric
   ```
2. The response will include data like this:
   ```json
   {
      "main": {
         "temp": 15.75,
         "pressure": 1012,
         "humidity": 87
      },
      "wind": {
         "speed": 4.12
      },
      "weather": [{
         "description": "clear sky"
      }]
   }
   ```
3. In Grafana, set up a JSON API data source and query this endpoint. You can then display the **temperature** or **wind speed** in a single stat panel or track the data over time with a time-series graph.

### 7. **Customize Refresh Rate**
   - Weather APIs usually update every hour or so. Set your panel’s refresh rate in Grafana to match the frequency of the API updates.
   - For instance, you can set the panel to refresh every **30 minutes** by configuring the dashboard settings.

### Suggested Free Weather APIs for Grafana

1. **OpenWeatherMap**:
   - Provides free access to current weather, hourly forecasts, and 5-day forecasts.
   - **Free Tier**: 60 API calls per minute.
   - [OpenWeatherMap API](https://openweathermap.org/api)

2. **WeatherAPI**:
   - Offers weather forecasts, current conditions, and more, with a free tier.
   - **Free Tier**: 1 million calls/month.
   - [WeatherAPI](https://www.weatherapi.com/)

3. **Visual Crossing**:
   - Offers historical and forecasted weather data with a focus on data visualization.
   - **Free Tier**: 1000 API calls/day.
   - [Visual Crossing API](https://www.visualcrossing.com/weather-api)

4. **Meteomatics**:
   - A highly accurate and precise weather API, with support for advanced features like aviation forecasts. Free access may be limited.
   - [Meteomatics API](https://www.meteomatics.com/en/)

### Conclusion:
Adding weather forecasts to Grafana dashboards is entirely possible using the **JSON API plugin** and weather data from providers like **OpenWeatherMap** or **WeatherAPI**. With the steps outlined above, you can visualize various weather metrics, such as temperature, humidity, and wind speed, directly in Grafana using free or low-cost APIs.