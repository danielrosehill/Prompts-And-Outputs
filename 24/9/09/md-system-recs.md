# Prompt

While I'm working on building an optimal system for storing GPT outputs, I've decided that as a short term measure I'm going to just save everything in a Github repository. As you remember, the core components of the GPT output organisation system I'm building are saved post outputs, saved prompts, and saved custom GPT configurations. You also know that I'm very insistent on building my system on a relational database. So reducing it to a series of flat files is a bit frustrating! Can you suggest an organisational structure I can follow to make my repository as useful as possible? I'd like to be able to search through my previous output generations and tag them. Can I do any of this with a simple markdown filesystem? Do you have any ideas for how I can make this system as useful but simple as possible?

# Output

Here's a practical organizational structure for your GitHub repository that should help you maintain clarity and accessibility while keeping things simple:

### 1. **Top-Level Directory Structure**
   - **`/prompts/`**: Store all saved prompts.
   - **`/outputs/`**: Store all saved GPT outputs.
   - **`/configurations/`**: Store custom GPT configurations.
   - **`/tags/`**: Store tag metadata or tag mappings.

### 2. **Naming Conventions**
   - **Timestamps**: Use timestamps in the filenames to keep track of when the content was generated. Format them as `YYYYMMDD_HHMMSS`.
   - **Descriptive Names**: Append a short description to each file’s name to easily identify the content.
     - Example: `20240909_client_project_brainstorm.md`

### 3. **File Structure within Each Directory**
   - **`/prompts/`**
     - Store each prompt as a separate Markdown file.
     - Include metadata at the top (using YAML front matter) to describe the prompt.
     ```markdown
     ---
     id: prompt_001
     title: "Client Project Brainstorm"
     date: 2024-09-09
     tags: [client, brainstorm]
     ---
     
     ## Prompt
     What are some creative marketing strategies for a client in the tech industry?
     ```
     
   - **`/outputs/`**
     - Store each output in its own Markdown file.
     - Include metadata at the top to describe the output and link it to the associated prompt.
     ```markdown
     ---
     id: output_001
     prompt_id: prompt_001
     date: 2024-09-09
     tags: [client, marketing, strategy]
     ---
     
     ## Output
     Here are some creative marketing strategies...
     ```
     
   - **`/configurations/`**
     - Store each custom GPT configuration in a separate Markdown file.
     - Include metadata to describe the configuration.
     ```markdown
     ---
     id: config_001
     date: 2024-09-09
     tags: [client, marketing]
     ---
     
     ## Configuration
     Model: GPT-4
     Temperature: 0.7
     Max Tokens: 3000
     ```

### 4. **Tagging System**
   - **Tagging in YAML Front Matter**: Use YAML front matter in each Markdown file to store tags. This allows for easy future extraction and searching.
   - **Central Tag Registry**: Maintain a file within the `/tags/` directory to keep a list of all tags used, with descriptions if necessary.
     - Example: `tags.md`
     ```markdown
     - client: Related to client work
     - brainstorm: Idea generation and brainstorming sessions
     ```

### 5. **Search and Retrieval**
   - **Manual Search**: You can manually search through your repository using GitHub’s search functionality. Searching for specific tags or keywords within files should be straightforward.
   - **Tag Mapping**: If you want to manually organize files based on tags, create a mapping in the `/tags/` directory that lists files associated with each tag.
   - **README.md**: Create a top-level `README.md` file that explains the structure, how to add files, and how to use tags effectively.

### 6. **Automated Tagging (Optional)**
   - If you want a simple automated solution, consider creating a script that extracts metadata from each file and generates a summary or index. This script could run locally and push updates to the repository.

### 7. **Example Directory Structure**
   ```
   /GPT-Workbench/
   ├── prompts/
   │   ├── 20240909_client_project_brainstorm.md
   │   └── 20240908_weekly_planning.md
   ├── outputs/
   │   ├── 20240909_client_project_brainstorm_output.md
   │   └── 20240908_weekly_planning_output.md
   ├── configurations/
   │   ├── 20240909_marketing_config.md
   │   └── 20240908_general_config.md
   └── tags/
       └── tags.md
   ```

### 8. **Version Control and Collaboration**
   - GitHub’s version control will automatically track changes, allowing you to revert to previous versions if needed.
   - If you collaborate with others, encourage them to follow the same structure and tagging conventions.

This setup should provide you with a simple, yet powerful way to manage your GPT outputs, prompts, and configurations while maintaining flexibility for future expansion.