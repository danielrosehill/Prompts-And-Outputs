---
title: "Can you modify schemas with APIs"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*



Yes, you can use APIs to change the database schema, including creating or deleting columns, on managed PostgreSQL services that support schema manipulation through their API layers. Here are some platforms and methods that allow for such operations:

### 1. **Supabase**

\- **Supabase** provides a comprehensive API that allows you to interact with your PostgreSQL database, but it currently does not directly support schema modifications (like creating or deleting columns) through its RESTful or GraphQL APIs.

\- However, you can execute SQL commands directly via the Supabase SQL editor or through any PostgreSQL client to modify the schema.

\- **Custom API for Schema Changes**:

\- You can create a custom API function within Supabase that allows you to execute SQL commands for schema changes if needed.

### 2. **Hasura**

\- **Hasura** primarily focuses on providing a real-time GraphQL API for your data. It does not offer built-in APIs to modify the database schema (such as creating or deleting columns) directly through GraphQL.

\- **Using SQL via Hasura**:

\- You can use Hasura’s console or any connected PostgreSQL client to execute SQL commands to alter the schema.

\- Alternatively, you can create custom SQL functions within PostgreSQL and expose them through Hasura to manage schema changes indirectly.

### 3. **Directus**

\- **Directus** offers API endpoints for managing the schema, including creating and deleting tables, columns, and relationships.

\- **Schema Management API**:

\- You can use Directus API endpoints to perform schema modifications. This includes creating new fields (columns) or deleting existing ones via RESTful API requests.

\- **Example**:

\- **Create a Column**:

\`\`\`bash

POST /fields/:collection

\`\`\`

\- This API endpoint allows you to add a new column to a specific collection (table).

\- **Delete a Column**:

\`\`\`bash

DELETE /fields/:collection/:field

\`\`\`

\- This API endpoint lets you delete an existing column from a collection.

### 4. **PostgREST**

\- **PostgREST** exposes your PostgreSQL database schema as a RESTful API. However, it is designed primarily for interacting with data and does not natively support schema modifications via its API.

\- **Using SQL**:

\- Schema modifications like adding or deleting columns would need to be done using SQL commands directly via a PostgreSQL client or a custom endpoint that allows for SQL execution.

### 5. **Custom Solutions on General Platforms (e.g., Railway, Neon)**

\- On platforms like **Railway** or **Neon**, you typically connect to the PostgreSQL instance using standard tools or libraries (e.g., `psql`, `pgAdmin`, etc.) and execute SQL commands to modify the schema.

\- **Custom API**:

\- You can deploy your own API service on these platforms that accepts HTTP requests and executes SQL commands to modify the schema. This can be done using server-side languages like Node.js, Python, etc., combined with a PostgreSQL client library.

### Summary

While platforms like **Supabase** and **Hasura** don’t provide built-in API endpoints specifically for schema changes, **Directus** offers an API that can manage database schema directly, including creating and deleting columns. For other platforms, schema changes are typically done via SQL commands, either directly through a database client or by creating custom API endpoints that execute these commands.