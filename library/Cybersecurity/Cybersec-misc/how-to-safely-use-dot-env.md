---
title: "How to safely use dot env"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# prompt

I'm working on creating a Github repository to share a simple script based on the OpenAI API. I need to use two credentials in my dot env for my API key and database string. I want anybody to be able to use this project. but I also want to be able to use it myself (of course!). what's the safest way to store these credentials in this public repo?

# output

To securely share your project in a public GitHub repository while keeping your API key and database connection string private, you can follow these steps:

### 1. **Use a `.env.example` File**
   - **Purpose**: Provide an example file that shows users what environment variables they need to define, without including your actual credentials.
   - **How to Do It**:
     - Create a `.env.example` file in your project.
     - In this file, list the environment variable names without the actual sensitive values.
     - Example:
       ```plaintext
       OPENAI_API_KEY=your_openai_api_key_here
       DATABASE_URL=your_database_url_here
       ```
   - **Commit to Repository**: Commit this `.env.example` file to your repository to guide others on what environment variables they need to set up.

### 2. **Add `.env` to `.gitignore`**
   - **Purpose**: Ensure that your actual `.env` file, which contains your real credentials, is not included in your Git repository.
   - **How to Do It**:
     - Add `.env` to your `.gitignore` file:
       ```plaintext
       .env
       ```
     - This prevents Git from tracking changes to the `.env` file, keeping your credentials secure.

### 3. **Use Environment Variables in Your Code**
   - **Purpose**: Write your script so that it reads from the environment variables defined in the `.env` file.
   - **How to Do It**:
     - Install a package like `python-dotenv` to load environment variables from a `.env` file:
       ```bash
       pip install python-dotenv
       ```
     - Load the environment variables in your script:
       ```python
       from dotenv import load_dotenv
       import os

       load_dotenv()

       openai_api_key = os.getenv("OPENAI_API_KEY")
       database_url = os.getenv("DATABASE_URL")

       # Now you can use openai_api_key and database_url in your code
       ```
   
### 4. **Document How to Use the Project**
   - **Purpose**: Help users set up their environment variables by providing clear instructions in the repository’s `README.md` file.
   - **How to Do It**:
     - In your `README.md`, include a section on "Setup" that explains how to:
       - Copy the `.env.example` file to `.env`
       - Populate the `.env` file with their own credentials
       - Example:
         ```markdown
         ## Setup

         1. Clone the repository.
         2. Copy `.env.example` to `.env`.
         3. Edit the `.env` file to add your OpenAI API key and database URL:
            ```
            cp .env.example .env
            ```
         4. Run the script.
         ```

### 5. **Use GitHub Secrets for CI/CD (Optional)**
   - **Purpose**: If you plan to integrate continuous integration or continuous deployment (CI/CD) workflows using GitHub Actions, use [GitHub Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets) to store your credentials securely.
   - **How to Do It**:
     - Go to your GitHub repository settings.
     - Navigate to "Secrets and variables" under "Security".
     - Add your API key and database URL as secrets.
     - Reference these secrets in your GitHub Actions workflows.

By following these steps, you can safely store and manage your credentials while allowing others to use your project without exposing sensitive information.