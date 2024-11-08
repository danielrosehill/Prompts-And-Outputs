---
title: "How to list column names in table on PSQL"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Summary:** You are asking how to list the columns in the `documents` table using `psql` in PostgreSQL.

### Listing Columns in a Table Using `psql`

To view the columns of a table (like `documents`) in PostgreSQL, you can use the `\d` command in the `psql` command-line interface.

#### Step-by-Step Instructions:

1. **Connect to the PostgreSQL Database Using `psql`**
   - If you’re inside the Docker container:
     ```bash
     psql -U outline -d outline
     ```
   - Replace `outline` with your PostgreSQL username and database name if they are different.

2. **List Columns in the `documents` Table**
   - Run the following command:
     ```sql
     \d documents
     ```
   - This will display the structure of the `documents` table, including:
     - Column names
     - Data types
     - Indexes and constraints

3. **View More Detailed Information (Optional)**
   - For even more details about the table, including descriptions, run:
     ```sql
     \d+ documents
     ```

### Example Output

When you run `\d documents`, you might see something like this:
```plaintext
                                    Table "public.documents"
   Column    |            Type             | Collation | Nullable |               Default
-------------+-----------------------------+-----------+----------+-------------------------------------
 id          | uuid                        |           | not null | uuid_generate_v4()
 title       | character varying           |           |          |
 content     | text                        |           |          |
 created_at  | timestamp without time zone |           | not null | now()
 updated_at  | timestamp without time zone |           | not null | now()
 user_id     | uuid                        |           |          |
 collection_id | uuid                      |           |          |
Indexes:
    "documents_pkey" PRIMARY KEY, btree (id)
```

### Summary
1. **Connect to the PostgreSQL database using `psql`.**
2. **Run `\d documents`** to list the columns and details of the `documents` table.
3. **Use `\d+ documents`** for more detailed information.

These commands will help you see how the `documents` table is structured, which can be useful for verifying that your Outline KM data is correctly stored.