---
title: "Interactive stack recommendation GUI"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Would you be able to help me build a simple interactive GUI that would integrate with Anthropic by API and produce stack recommendations?

# Output
Certainly! I'd be happy to help you create a simple interactive GUI that integrates with Anthropic's API to produce stack recommendations. Based on your requirements, we can use PySimpleGUI for the GUI framework and integrate it with Anthropic's API. This approach will allow us to create a user-friendly interface while leveraging the power of Claude for generating recommendations.

Here's a basic outline of how we can structure this application:

1. Set up the environment and install required libraries
2. Create the GUI layout using PySimpleGUI
3. Implement the Anthropic API integration
4. Process user input and display recommendations

Let's go through each step:

## 1. Set up the environment and install required libraries

First, make sure you have Python installed. Then, create a virtual environment and install the required libraries:

```bash
python -m venv stack-recommender-env
source stack-recommender-env/bin/activate  # On Windows, use `stack-recommender-env\Scripts\activate`
pip install PySimpleGUI anthropic
```

## 2. Create the GUI layout using PySimpleGUI

Let's create a simple GUI with input fields for project requirements and a button to generate recommendations:

```python
import PySimpleGUI as sg

def create_gui():
    layout = [
        [sg.Text("Project Type:"), sg.Input(key="-PROJECT_TYPE-")],
        [sg.Text("Technical Requirements:"), sg.Multiline(key="-TECH_REQS-", size=(50, 3))],
        [sg.Text("Budget Constraints:"), sg.Input(key="-BUDGET-")],
        [sg.Text("Integration Needs:"), sg.Input(key="-INTEGRATIONS-")],
        [sg.Text("Scalability Requirements:"), sg.Input(key="-SCALABILITY-")],
        [sg.Checkbox("Open Source Preferred", key="-OPEN_SOURCE-")],
        [sg.Button("Generate Recommendations")],
        [sg.Multiline(key="-OUTPUT-", size=(60, 10), disabled=True)]
    ]
    
    return sg.Window("Stack Recommender", layout)
```

## 3. Implement the Anthropic API integration

Now, let's create a function to interact with the Anthropic API:

```python
import anthropic

def generate_recommendations(project_info):
    client = anthropic.Anthropic()
    
    prompt = f"""
    Based on the following project requirements, recommend the top 5 technology stack options:
    
    Project Type: {project_info['project_type']}
    Technical Requirements: {project_info['tech_reqs']}
    Budget Constraints: {project_info['budget']}
    Integration Needs: {project_info['integrations']}
    Scalability Requirements: {project_info['scalability']}
    Open Source Preferred: {project_info['open_source']}
    
    Please provide a brief explanation for each recommendation.
    """
    
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        temperature=0.5,
        system="You are a helpful assistant specializing in technology stack recommendations.",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return message.content[0].text
```

## 4. Process user input and display recommendations

Finally, let's tie everything together in the main application loop:

```python
def main():
    window = create_gui()
    
    while True:
        event, values = window.read()
        
        if event == sg.WINDOW_CLOSED:
            break
        
        if event == "Generate Recommendations":
            project_info = {
                "project_type": values["-PROJECT_TYPE-"],
                "tech_reqs": values["-TECH_REQS-"],
                "budget": values["-BUDGET-"],
                "integrations": values["-INTEGRATIONS-"],
                "scalability": values["-SCALABILITY-"],
                "open_source": values["-OPEN_SOURCE-"]
            }
            
            recommendations = generate_recommendations(project_info)
            window["-OUTPUT-"].update(recommendations)
    
    window.close()

if __name__ == "__main__":
    main()
```

To run this application, you'll need to set your Anthropic API key as an environment variable:

```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

Then, you can run the script:

```bash
python stack_recommender.py
```

This simple GUI application allows users to input their project requirements and generates stack recommendations using the Anthropic API. The recommendations are then displayed in the output area of the GUI.

You can further enhance this application by:

1. Adding error handling and input validation
2. Implementing a loading indicator while waiting for API responses
3. Allowing users to save and load project requirements
4. Adding more detailed input fields for specific technology preferences
5. Implementing a feature to compare different recommended stacks

This basic implementation should give you a good starting point for creating an interactive GUI that integrates with the Anthropic API to produce stack recommendations. You can build upon this foundation to create a more comprehensive tool tailored to your specific needs.

 





## Extracted Prompts
[[Prompts/Interactive stack recommendation GUI.md#Prompt 1|Prompt 1]]
