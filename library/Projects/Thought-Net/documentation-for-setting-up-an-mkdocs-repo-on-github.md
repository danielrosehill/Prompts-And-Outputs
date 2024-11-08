---
title: "Documentation for setting up an MKDocs repo on Github"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Please provide me with a guide to setting up a public documentation repo on Github using MKDocs. 
Show me how to do that in this order:

1) Create the repo with MkDocs
2) Set up the repo in Github and configure the local repo appropriately
3) Preview the site as I'm building it
4) Push to Github
# Output
Here's a step-by-step guide to setting up a public documentation repository on GitHub using **MkDocs**:

### Step 1: Create the Repo with MkDocs
1. **Install MkDocs**:
   ```bash
   pip install mkdocs
   ```

2. **Create a New MkDocs Project**:
   ```bash
   mkdocs new my-docs
   cd my-docs
   ```

### Step 2: Set Up the Repo in GitHub
1. **Initialize a Git Repository**:
   ```bash
   git init
   ```

2. **Create a New Repository on GitHub**:
   - Go to GitHub and create a new repository (e.g., `my-docs`).

3. **Connect Local Repo to GitHub**:
   ```bash
   git remote add origin https://github.com/yourusername/my-docs.git
   ```

### Step 3: Preview the Site
1. **Run MkDocs Locally**:
   ```bash
   mkdocs serve
   ```
   - Open `http://127.0.0.1:8000` in your browser to see the live preview.

### Step 4: Push to GitHub
1. **Add and Commit Changes**:
   ```bash
   git add .
   git commit -m "Initial commit"
   ```

2. **Push to GitHub**:
   ```bash
   git push -u origin main
   ```

### Final Steps
- Configure GitHub Pages in the repository settings to serve your documentation from the `gh-pages` branch or the `main` branch, depending on your preference.

This setup will allow you to build and publish your documentation easily using MkDocs on GitHub!