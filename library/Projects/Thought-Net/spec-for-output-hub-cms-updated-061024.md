---
title: "Spec for Output Hub CMS updated 061024"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Please identify a list of CMS toosl that meet these criteria (or any kind of software)

It can be self hosted or it can be SaaS. But if it's SaaS there needs to be a good backup functionality. 

The tool (probably a CMS but maybe defined as something else) needs to be able to do all the following:

- They have native support for markdown. You can paste markdown into them and they'll instantly render it into readable text (ie, the formatting is autoconverted)
- They're backed by some kind of database
- Easy to set up. It doesn't take long to get some kind of GUI / backend running
- You can create custom fields to match your project. E.g. in my output hub management system I don't need "posts" and "pages" but I do need "outputs" (for saving outputs) and prompts
- Ideally, you can create relationships between these custom post types. Ie, I can associate a prompt with an output with an agent
- Scalable, easy to use, but powerful
- Can be used as an internal tool / doesn't have to be a public facing site 

suggest as many options as you can think of that meet these specs

# Output

Sure! Here's a list of CMS tools and other platforms that meet most, if not all, of the criteria you've mentioned. I focused on systems that are either self-hosted or SaaS with good backup capabilities and meet your functional requirements such as Markdown support, database backing, and customization for custom fields and relationships.

### 1. **Sanity.io (Headless CMS)**
   - **Type**: SaaS / Self-hosted (via Sanity Studio)
   - **Markdown Support**: Sanity supports rich text that can easily handle Markdown.
   - **Database Backing**: Sanity stores data as JSON documents backed by its real-time content lake.
   - **Custom Fields**: Highly flexible with the ability to define custom content types and fields.
   - **Relationships**: Relationships between content types are possible.
   - **Ease of Setup**: Fairly straightforward to set up with Sanity Studio.
   - **Internal Tool Usage**: Can be used as an internal CMS with a customized interface.

### 2. **Strapi**
   - **Type**: Self-hosted / On-premise
   - **Markdown Support**: Has Markdown support through plugins or fields in content types.
   - **Database Backing**: Uses relational databases such as SQLite, PostgreSQL, or MySQL.
   - **Custom Fields**: Allows for custom content types, fields, and flexible data modeling.
   - **Relationships**: Native support for relationships between different content types.
   - **Ease of Setup**: Installation is easy, requiring minimal setup to get running.
   - **Internal Tool Usage**: Perfect for internal tools, highly customizable interface.

### 3. **Contentful**
   - **Type**: SaaS
   - **Markdown Support**: Supports Markdown through its rich text editor.
   - **Database Backing**: Uses a proprietary content backend, but you can access all data via an API.
   - **Custom Fields**: Custom content types and fields are fully supported.
   - **Relationships**: Strong support for linking and relating entries.
   - **Ease of Setup**: Very easy to get started with a simple and intuitive GUI.
   - **Backup Functionality**: Contentful offers backup options and export features.
   - **Internal Tool Usage**: Often used as a backend for headless CMS use cases, including internal tools.

### 4. **Directus**
   - **Type**: Self-hosted / SaaS
   - **Markdown Support**: Supports Markdown fields natively.
   - **Database Backing**: Connects to your existing SQL database and works as an API-first wrapper.
   - **Custom Fields**: Completely customizable data models and fields.
   - **Relationships**: Excellent support for relational data modeling.
   - **Ease of Setup**: Quick setup with a visual interface.
   - **Internal Tool Usage**: Suitable for internal content management, with strong data modeling.

### 5. **Notion (With API Extensions)**
   - **Type**: SaaS
   - **Markdown Support**: Natively supports Markdown import and rendering.
   - **Database Backing**: Uses a proprietary database structure, with the ability to create tables and link data.
   - **Custom Fields**: Pages can be structured with any fields needed.
   - **Relationships**: Tables/databases can be linked together.
   - **Ease of Setup**: Extremely easy to set up.
   - **Backup Functionality**: You can export Notion pages/databases in Markdown or other formats to create backups.
   - **Internal Tool Usage**: Often used as an internal wiki or documentation hub, ideal for managing content within teams.

### 6. **KeystoneJS**
   - **Type**: Self-hosted
   - **Markdown Support**: Supports Markdown fields.
   - **Database Backing**: Built on Node.js and supports MongoDB and PostgreSQL.
   - **Custom Fields**: Highly customizable schema and field types.
   - **Relationships**: Provides relationship support between content types.
   - **Ease of Setup**: Easy setup using modern JavaScript frameworks.
   - **Internal Tool Usage**: Can be used for both internal tools and public-facing websites.

### 7. **Ghost CMS**
   - **Type**: SaaS / Self-hosted
   - **Markdown Support**: Uses Markdown as the default editor.
   - **Database Backing**: Uses MySQL or SQLite for data storage.
   - **Custom Fields**: Less flexible in terms of creating completely custom post types but still allows some degree of customization.
   - **Relationships**: Limited ability to create complex relationships between custom content types.
   - **Ease of Setup**: Extremely easy to set up with either the self-hosted or hosted version.
   - **Backup Functionality**: Offers backup options through its API or with the managed SaaS offering.

### 8. **Appsmith**
   - **Type**: Self-hosted / SaaS
   - **Markdown Support**: Markdown widgets are available.
   - **Database Backing**: Connects to existing databases like PostgreSQL, MySQL, etc.
   - **Custom Fields**: Since it’s an internal tool builder, you can create whatever custom inputs you need.
   - **Relationships**: You can define relationships within your database and surface them via custom interfaces.
   - **Ease of Setup**: Appsmith is focused on ease of use, with drag-and-drop components.
   - **Internal Tool Usage**: Primarily meant for internal tools and dashboards.

### 9. **Baserow**
   - **Type**: Self-hosted / SaaS
   - **Markdown Support**: Supports Markdown rendering in text fields.
   - **Database Backing**: Uses PostgreSQL for data storage.
   - **Custom Fields**: Custom fields and data types are fully supported.
   - **Relationships**: Supports linking between tables for relational data.
   - **Ease of Setup**: Very easy to use and set up with a simple GUI.
   - **Internal Tool Usage**: Designed for internal use as a database tool similar to Airtable.

### 10. **Netlify CMS**
   - **Type**: Self-hosted (Git-based)
   - **Markdown Support**: Uses Markdown files for content storage.
   - **Database Backing**: No database; uses Git for version control and data storage.
   - **Custom Fields**: Highly customizable collections and fields.
   - **Relationships**: Basic relationship support by linking between collections.
   - **Ease of Setup**: Fairly easy if you're comfortable with Git-based workflows.
   - **Internal Tool Usage**: Can be used internally, but more common for static site generation.

### 11. **WeWeb (Headless CMS)**
   - **Type**: SaaS
   - **Markdown Support**: Allows for Markdown rendering.
   - **Database Backing**: Integrates with various backends like Airtable, Google Sheets, and more.
   - **Custom Fields**: Custom data modeling is possible.
   - **Relationships**: Supports relationships if your backend supports it.
   - **Ease of Setup**: Drag-and-drop interface makes setup straightforward.
   - **Internal Tool Usage**: Can easily be used as an internal CMS or for web apps.

### 12. **Payload CMS**
   - **Type**: Self-hosted
   - **Markdown Support**: Supports Markdown out of the box.
   - **Database Backing**: Uses MongoDB for content storage.
   - **Custom Fields**: Easily create custom content types with different fields.
   - **Relationships**: Supports relational fields for complex content relationships.
   - **Ease of Setup**: Easy setup, especially for JavaScript developers.
   - **Internal Tool Usage**: Can be used internally with customizable interfaces.

These tools all support Markdown rendering, custom fields, relationships, scalability, and easy-to-use backends. Depending on your specific use case—such as the level of control over hosting, customization needs, and whether you prefer a SaaS or self-hosted solution—you might find one of these more suitable than the others. 

Let me know if you need more information or guidance on any specific tool!