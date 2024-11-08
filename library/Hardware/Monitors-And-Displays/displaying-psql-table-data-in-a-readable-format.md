---
title: "Displaying PSQL table data in a readable format"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Summary:** You are asking how to make the output of your PostgreSQL query more readable when displaying it from the command line, as it's not currently laying out in a clear grid format.

### Improving Readability of Query Output in `psql`

When using `psql`, the default output can sometimes be difficult to read, especially for wider content. Here are a few ways to improve the readability:

### 1. **Use `\x` to Enable Expanded Display**

- **Command**: `\x`
- The `\x` command in `psql` toggles **expanded display mode**, which arranges each row vertically instead of horizontally. This can be very useful if the data in columns (like `content`) is too wide to fit comfortably on the screen.
- **How to Use**:
  ```sql
  \x
  SELECT title, content FROM documents;
  ```
- **Result**:
  ```plaintext
  -[ RECORD 1 ]-------------------------
  title   | Test Note
  content | This is a test note for verification.
  -[ RECORD 2 ]-------------------------
  title   | Meeting Notes
  content | Notes from the meeting on Oct 27.
  ```

### 2. **Adjust Output Width Using `\pset`**

- **Command**: `\pset format` and `\pset columns`
- You can control how the output is displayed using `\pset`. For example, setting the format to `aligned` and specifying a `columns` width helps:
  ```sql
  \pset format aligned
  \pset columns 80
  SELECT title, content FROM documents;
  ```
- This will make the output display more neatly across the screen, assuming there is enough width.

### 3. **Redirect Output to a File for Easier Reading**

- **Command**: `\o <filename>`
- If you want to review the output without worrying about terminal formatting, redirect the results to a file:
  ```sql
  \o output.txt
  SELECT title, content FROM documents;
  \o
  ```
- The output will be saved to `output.txt`, which you can open with any text editor to view in a more readable format.

### 4. **Use `psql` Options for Better Output on the Command Line**

- **Command**: Use `-P` and `--expanded` options
- You can directly use these flags from the command line to enable expanded output when you run the query:
  ```bash
  psql -U outline -d outline -c "SELECT title, content FROM documents;" --expanded
  ```
- This will automatically display the query results in an expanded, vertical format without needing to toggle `\x` inside `psql`.

### Summary:
1. **Toggle Expanded View**: Use `\x` before running your query.
2. **Adjust Output Width**: Use `\pset` to improve how the table is displayed.
3. **Redirect Output to a File**: Use `\o` to save results for easier reading.
4. **Use Command-Line Options**: Add `--expanded` for direct expanded output.

These methods should help you display your query results in a more readable format from the command line when using `psql`.