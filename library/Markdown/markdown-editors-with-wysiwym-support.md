---
title: "Markdown editors with WYSIWYM support"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, there are a few self-hostable markdown editors with database storage that also support WYSIWYM (single-pane, live preview) editing. Here are some of the best options for this setup:

### 1. **Outline**
   - **WYSIWYM Support**: Outline uses a single-pane WYSIWYM editor where markdown renders as rich text instantly as you type or paste.
   - **Database**: Built on PostgreSQL, ensuring reliable database-backed storage and indexing.
   - **Features**: Rich-text conversion, real-time collaboration, and structured document organization. It’s optimized for team knowledge bases, with roles, permissions, and integration with SSO.
   - **Repository**: [Outline on GitHub](https://github.com/outline/outline)

### 2. **BookStack**
   - **WYSIWYM Support**: While BookStack is primarily WYSIWYG, it has a markdown editor option that renders pasted markdown as rich text, though it lacks full inline WYSIWYM like Obsidian.
   - **Database**: Uses MySQL, MariaDB, or PostgreSQL.
   - **Features**: WYSIWYG and markdown support, real-time rendering, version control, permissions, and organizational tools. It’s suited for teams needing a self-hosted documentation platform.
   - **Repository**: [BookStack on GitHub](https://github.com/BookStackApp/BookStack)

### 3. **Wiki.js**
   - **WYSIWYM Support**: Wiki.js has an inline live preview for markdown in its editor, where formatted text appears as you type, although it does offer optional split-pane preview.
   - **Database**: Compatible with PostgreSQL, MySQL, MariaDB, and SQLite.
   - **Features**: Versatile document editor with markdown, authentication integrations (SSO, LDAP), role-based access, and support for structured content and modular plugins.
   - **Repository**: [Wiki.js on GitHub](https://github.com/Requarks/wiki)

### 4. **HedgeDoc** (formerly CodiMD)
   - **WYSIWYM Support**: HedgeDoc provides live preview as you type in a single pane, with automatic rendering of markdown to rich text.
   - **Database**: Supports PostgreSQL, MySQL, or SQLite for database storage.
   - **Features**: Real-time collaboration, single-pane live preview, role-based permissions, and support for plugins and theming.
   - **Repository**: [HedgeDoc on GitHub](https://github.com/hedgedoc/hedgedoc)

### Summary
For a single-pane WYSIWYM experience with self-hosting and database storage, **Outline** and **HedgeDoc** are the closest matches. **Wiki.js** also offers inline live preview with optional split-pane. If full WYSIWYM functionality (like Obsidian’s) is essential, **Outline** and **HedgeDoc** are particularly well-suited due to their live preview handling of both pasted and typed markdown.