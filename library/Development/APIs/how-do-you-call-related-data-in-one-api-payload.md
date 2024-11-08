---
title: "How Do You Call Related Data In One API Payload"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*



Yes, you can often write data to both a table and a related table in a single API request, but this depends on the specific API you're working with and its capabilities. Here's how it generally works:

### 1. **Embedded Data in a Single Request:**

\- Some APIs allow you to include related data within a single request. For example, you can send a request to create or update a record in a table and include related records as part of the request payload.

\- Example: In a request to create an order, you might include customer information and order items in the same payload.

\`\`\`json

{

"order": {

"order\_date": "2024-08-23",

"customer\_id": 123,

"items": \[

{"product\_id": 1, "quantity": 2},

{"product\_id": 2, "quantity": 1}

\]

}

}

\`\`\`

### 2. **Batch Requests:**

\- Some APIs support batch operations where you can send multiple requests in a single call. This can be useful for creating or updating records in both the main table and a related table simultaneously.

\- Example: Sending multiple `POST` or `PATCH` requests in a single API call.

\`\`\`json

\[

{

"method": "POST",

"url": "/api/v2/tables/orders",

"body": {"order\_date": "2024-08-23", "customer\_id": 123}

},

{

"method": "POST",

"url": "/api/v2/tables/order\_items",

"body": {"order\_id": 456, "product\_id": 1, "quantity": 2}

}

\]

\`\`\`

### 3. **Transaction Support:**

\- Some APIs provide transaction-like support, where multiple related operations are treated as a single unit. If one operation fails, the entire set of operations is rolled back. This ensures that data remains consistent.

### 4. **Chained API Calls:**

\- If the API doesn't support writing to multiple tables in a single request, you might need to make separate API calls. First, create or update the record in the main table, then use the resulting ID to write to the related table.

### 5. **API-Specific Features:**

\- Some APIs might have specific features or parameters that allow you to perform these operations more easily. Always check the API documentation to understand what capabilities are available.

### Example Use Case:

If you're working with an API for a relational database and want to create a customer record and associated orders in one go, the API might allow you to do so by embedding the orders within the customer record creation request. Alternatively, you might first create the customer, get the customer ID, and then use it to create the orders in a second request.

Always refer to the specific API documentation for detailed instructions and examples related to handling related records.