---
title: "Exporting a markdown repository into a Neo graph database"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, you can programmatically ingest your collection of Markdown files into Neo4j. Here’s a structured approach to achieve this:

### 1. **Parse Markdown Files**
   - Use Python to read each Markdown file, extract the content, metadata (like titles, dates, tags), and any links or internal references. The `frontmatter` Python package can help if you use YAML metadata at the start of each file.

### 2. **Prepare Data for Neo4j Nodes and Relationships**
   - Each file will represent a **node** in Neo4j, and you can store relevant details (e.g., title, content, tags) as properties on the node.
   - If files contain links to other files or related topics, you can create **relationships** between nodes to represent these links in Neo4j.

### 3. **Set Up a Script to Import Data**
   - **Connect to Neo4j**: Use the `neo4j` Python driver to connect to your Neo4j instance.
   - **Create Nodes and Relationships**: Write a script to parse your Markdown files, create nodes for each file, and add relationships based on links or thematic tags.

Here’s a sample Python script outline to get you started:

#### Step-by-Step Script Example

1. **Install Required Libraries**:
   ```bash
   pip install neo4j markdown2 frontmatter
   ```

2. **Python Script**:
   ```python
   import os
   from neo4j import GraphDatabase
   import frontmatter
   import markdown2

   # Connection details for Neo4j
   URI = "bolt://localhost:7687"  # Adjust according to your setup
   USERNAME = "neo4j"
   PASSWORD = "your_password"

   # Initialize Neo4j driver
   driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

   def parse_markdown_file(file_path):
       """Extracts content and metadata from a Markdown file."""
       with open(file_path, 'r') as f:
           post = frontmatter.load(f)
           content_html = markdown2.markdown(post.content)
           metadata = post.metadata
       return metadata, content_html

   def create_node(tx, title, content, tags):
       """Creates a node in Neo4j for each file with properties."""
       tx.run("CREATE (n:Document {title: $title, content: $content, tags: $tags})",
              title=title, content=content, tags=tags)

   def create_relationship(tx, title1, title2, rel_type="RELATED"):
       """Creates a relationship between nodes in Neo4j."""
       tx.run("""
           MATCH (a:Document {title: $title1}), (b:Document {title: $title2})
           MERGE (a)-[:RELATION {type: $rel_type}]->(b)
       """, title1=title1, title2=title2, rel_type=rel_type)

   def ingest_markdown_files(folder_path):
       """Ingests all Markdown files in a folder into Neo4j."""
       with driver.session() as session:
           for filename in os.listdir(folder_path):
               if filename.endswith(".md"):
                   file_path = os.path.join(folder_path, filename)
                   metadata, content = parse_markdown_file(file_path)
                   
                   # Extract title, tags from metadata, or default to filename
                   title = metadata.get("title", filename)
                   tags = metadata.get("tags", [])

                   # Create a node for each file
                   session.write_transaction(create_node, title, content, tags)

                   # Optional: Link nodes based on related tags
                   for tag in tags:
                       session.write_transaction(create_relationship, title, tag, "TAGGED_AS")

   # Run the ingestion
   folder_path = "path/to/your/markdown_files"
   ingest_markdown_files(folder_path)

   # Close Neo4j driver connection
   driver.close()
   ```

### Explanation of Key Parts

1. **Parsing Markdown Files**:
   - The `parse_markdown_file` function reads each Markdown file, extracts metadata, and converts the Markdown content to HTML for easier storage and retrieval.

2. **Creating Nodes**:
   - The `create_node` function creates a `Document` node in Neo4j with properties like `title`, `content`, and `tags`. Adjust these properties based on your metadata needs.

3. **Creating Relationships**:
   - The `create_relationship` function adds connections between notes based on shared tags or any internal links, capturing relationships within the knowledge graph.

4. **Ingesting All Files**:
   - The `ingest_markdown_files` function loops over all Markdown files in a directory, calling the `create_node` function for each file and optionally linking nodes with shared tags or other criteria.

This approach should allow you to ingest your Markdown collection into Neo4j programmatically, establishing an interactive knowledge graph ready for search and exploration.