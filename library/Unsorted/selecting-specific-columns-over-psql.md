---
title: "Selecting specific columns over PSQL"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Summary:** You want to query the `documents` table in PostgreSQL to display only the values of the `title` and `content` columns.

### Querying Specific Columns in PostgreSQL

To display just the `title` and `content` from the `documents` table, you can run a `SELECT` query in `psql`.

#### Step-by-Step Instructions:

1. **Connect to the PostgreSQL Database**
   - Use `psql` to connect to your Outline database:
     ```bash
     psql -U outline -d outline
     ```

2. **Run the Query to Select `title` and `content`**
   - Execute the following SQL query:
     ```sql
     SELECT title, content FROM documents;
     ```

3. **Add Conditions (Optional)**
   - If you want to filter the results (e.g., only show a specific note), you can add a `WHERE` clause:
     ```sql
     SELECT title, content FROM documents WHERE title LIKE '%Test Note%';
     ```

### Example Output

Running the query:
```sql
SELECT title, content FROM documents;
```

Might return:
```plaintext
        title         |            content
----------------------+----------------------------------
 Test Note            | This is a test note for verification.
 Meeting Notes        | Notes from the meeting on Oct 27.
 Sample Document      | Some sample content for Outline KM.
```

### Summary
1. **Connect to PostgreSQL**: Use `psql -U outline -d outline`.
2. **Run the Query**: `SELECT title, content FROM documents;`.
3. **Optional Filtering**: Use `WHERE` to narrow down the results.

These commands will help you verify that the notes are correctly stored in the `documents` table of your Outline KM setup.