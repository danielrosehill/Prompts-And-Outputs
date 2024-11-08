---
title: "Code-based data visualisation and charting frameworks"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



To generate charts automatically with a framework like Matplotlib or other alternatives, and integrate it into your workflow, including using VS Code, here are some of the best options:

## 1. Matplotlib (Python)

Matplotlib is one of the most popular Python libraries for data visualization, and it's widely used due to its flexibility and extensive customization options. It integrates seamlessly with VS Code when you use Python extensions.

### How to Use Matplotlib:

1. **Install Matplotlib**:
   ```bash
   pip install matplotlib
   ```
2. **Basic Example**:
   ```python
   import matplotlib.pyplot as plt

   # Define your data
   x = [1, 2, 3, 4]
   y = [10, 20, 25, 30]

   # Create a simple line chart
   plt.plot(x, y)
   plt.xlabel('X-axis')
   plt.ylabel('Y-axis')
   plt.title('Simple Line Chart')

   # Show the chart
   plt.show()
   ```
3. **Integration with VS Code**:
   - Install the Python extension in VS Code.
   - Write your Python script and run it directly within VS Code’s terminal or interactive window.

Matplotlib is highly customizable but requires you to define most elements manually, making it great for detailed control over your visualizations\[5].

## 2. Seaborn (Python)

Seaborn is built on top of Matplotlib and simplifies the process of creating statistical visualizations. It’s great for generating aesthetically pleasing charts with minimal code.

### How to Use Seaborn:

1. **Install Seaborn**:
   ```bash
   pip install seaborn
   ```
2. **Basic Example**:
   ```python
   import seaborn as sns
   import matplotlib.pyplot as plt

   # Load sample dataset
   data = sns.load_dataset('iris')

   # Create a scatter plot
   sns.scatterplot(x='sepal_length', y='sepal_width', data=data)

   # Show the plot
   plt.show()
   ```

Seaborn is perfect for users who want quick and elegant statistical plots without needing to configure every detail manually\[5].

## 3. Plotly (Python & JavaScript)

Plotly is a powerful library for creating interactive and publication-quality graphs. It supports both Python and JavaScript environments and can be integrated into web applications.

### How to Use Plotly (Python):

1. **Install Plotly**:
   ```bash
   pip install plotly
   ```
2. **Basic Example**:
   ```python
   import plotly.express as px

   # Load sample data
   df = px.data.iris()

   # Create a scatter plot
   fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species')

   # Show the plot in a browser or notebook
   fig.show()
   ```

Plotly also integrates well with VS Code when using Jupyter notebooks or running scripts in the terminal\[5]. It allows for interactive charts that can be embedded in web applications.

## 4. QuickChart (No-Code Solution)

If you prefer a no-code approach, QuickChart allows you to create chart templates online and generate charts automatically using API endpoints.

### How to Use QuickChart:

1. Go to the QuickChart [chart maker](https://quickchart.io/documentation/chart-maker/).
2. Define your chart using their interface.
3. Save the chart as an API template.
4. You can use the API endpoint to generate charts dynamically by passing new data via URL parameters\[2].

This solution is ideal if you're looking for simplicity and need to embed charts in emails or other non-code environments.

## 5. Bokeh (Python)

Bokeh excels at creating interactive plots that can be embedded directly into web applications or dashboards.

### How to Use Bokeh:

1. **Install Bokeh**:
   ```bash
   pip install bokeh
   ```
2. **Basic Example**:
   ```python
   from bokeh.plotting import figure, show

   # Create a new plot with title and axis labels
   p = figure(title="Simple Line Chart", x_axis_label='x', y_axis_label='y')

   # Add a line renderer with legend and line thickness
   p.line([1, 2, 3, 4], [10, 20, 25, 30], legend_label="Temp.", line_width=2)

   # Show the results in a browser window
   show(p)
   ```

Bokeh is perfect for users who want interactive visualizations directly in their web browsers without needing JavaScript expertise\[5].

## 6. Chart.js (JavaScript)

If you're working in web development and prefer JavaScript-based solutions, Chart.js is an excellent choice for creating responsive and interactive charts using HTML5 canvas elements.

### How to Use Chart.js:

1. Include Chart.js in your HTML file:
   ```html
   <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
   ```
2. Basic example:
   ```html
   <canvas id="myChart"></canvas>
   <script>
     var ctx = document.getElementById('myChart').getContext('2d');
     var myChart = new Chart(ctx, {
         type: 'bar',
         data: {
             labels: ['Red', 'Blue', 'Yellow', 'Green'],
             datasets: [{
                 label: '# of Votes',
                 data: [12, 19, 3, 5],
                 backgroundColor: ['rgba(255, 99, 132)', 'rgba(54, 162, 235)', 'rgba(255, 206, 86)', 'rgba(75, 192, 192)']
             }]
         }
     });
   </script>
   ```

Chart.js is widely used in web applications due to its simplicity and responsiveness\[1].

---

In summary:

- For Python users working in VS Code: **Matplotlib**, **Seaborn**, or **Plotly** are great options.
- For web developers or those looking for no-code solutions: consider **QuickChart** or **Chart.js**.

Citations:\
\[1] <https://www.monterail.com/blog/javascript-libraries-data-visualization>\
\[2] <https://quickchart.io/documentation/chart-maker/>\
\[3] <https://stackshare.io/matplotlib/alternatives>\
\[4] <https://github.com/hal9ai/awesome-dataviz>\
\[5] <https://dev.to/taipy/7-best-python-visualization-libraries-for-2024-5h9f>
