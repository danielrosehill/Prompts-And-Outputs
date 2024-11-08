---
title: "How does indentation work in YAML"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


In YAML, **indentation** is critical, as it defines the structure of the document. YAML relies on indentation to denote nesting and hierarchy, similar to Python. Here's what you need to know about how to properly format YAML and why it’s important:

### Key Points on YAML Indentation:
1. **Consistency**: YAML does not tolerate inconsistencies in indentation. You must use **consistent spaces** for indentation, not tabs.
   - Most YAML parsers expect spaces and will raise errors if they encounter tabs.
   
2. **Use Spaces, Not Tabs**: Indentation should always be done with spaces, not tabs. Even a single tab in a YAML file will cause errors.
   - Many text editors (like VSCode, Sublime Text, etc.) allow you to configure them to automatically convert tabs into spaces.
   - It’s best to configure your editor to use spaces for indentation in YAML files.

3. **Indentation Level**: The typical convention is to use **2 spaces** or **4 spaces** per indentation level. However, the key is to **remain consistent** throughout the document. Do not mix indentation levels.
   
4. **Offset of Individual Spaces**: Yes, **even a single space difference matters** in YAML. For example:
   ```yaml
   key1:
     key2: value2  # Correct (consistent 2 spaces)
   ```
   - But if you accidentally use an extra space or tab, it will break the YAML file:
   ```yaml
   key1:
      key2: value2  # Incorrect (inconsistent indentation)
   ```

### Example of Correct YAML Indentation:
```yaml
services:
  outline:
    image: docker.getoutline.com/outlinewiki/outline:latest
    env_file: ./docker.env
    ports:
      - "3000:3000"
    volumes:
      - storage-data:/var/lib/outline/data
    depends_on:
      - postgres
      - redis
    environment:
      PGSSLMODE: disable  # Disable SSL for PostgreSQL
  postgres:
    image: postgres
    env_file: ./docker.env
    ports:
      - "5432:5432"
    volumes:
      - database-data:/var/lib/postgresql/data
    environment:
      POSTGRES_USER: 'outline'
      POSTGRES_PASSWORD: 'p4fXErNVhMVrWoj3NPzW'
      POSTGRES_DB: 'outline'
```

In this example:
- Each level of indentation is consistently 2 spaces.
- The key-value pairs are properly aligned.

### Tips to Get YAML Indentation Right:
1. **Use a Proper Text Editor**:
   - Use an editor like **VSCode**, **Sublime Text**, or **Atom**, which highlights YAML syntax and can be configured to insert spaces instead of tabs.
   - Many editors provide plugins or features that help check for YAML syntax errors or inconsistencies.

2. **Set the Indentation Preferences**:
   - In VSCode, for example, you can set preferences for spaces and tabs:
     - Open **Settings**.
     - Search for "Indentation" and ensure that "Insert Spaces" is enabled.
     - Set the **tab size** to 2 or 4 spaces, depending on your preference.

3. **Check for Errors**:
   - Use an online YAML validator (like [YAML Lint](http://www.yamllint.com/)) to ensure your YAML file is valid and properly indented.

### Conclusion:
YAML requires precision when it comes to indentation, and individual space offsets can indeed cause issues. Always use spaces (not tabs), ensure consistent indentation levels, and stick to 2 or 4 spaces per level. A good text editor with YAML syntax support will help you maintain correct formatting.