---
title: "Creating Basic GUI For Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To create a basic GUI for your GPT Workbench project on Linux that interfaces with your Supabase database, I suggest using Python with the `tkinter` library for the GUI and `requests` or `httpx` for making API calls to Supabase. Below is a simple example of how to set up a basic GUI that allows you to read, write, and edit `prompt_outputs` from your Supabase database.

### Prerequisites

1. **Install Python Packages**:
   - Install the required packages using `pip`:
     ```bash
     pip install tkinter requests
     ```

2. **Create a Python Script**:

```python
import tkinter as tk
from tkinter import messagebox, ttk
import requests

# Supabase credentials
SUPABASE_URL = "https://jpbwzmachlphbdbvduap.supabase.co"
SUPABASE_API_KEY = "xxxxxxxVCJ9.xxxxxxxxxxxxxxxxxxxxxIjoyMDQwNzY2NzMxfQ.3Jmgie7xl5c-xj79hGLxiUIe8ifatlpW_ky4tDdoTIY"

headers = {
    "apikey": SUPABASE_API_KEY,
    "Authorization": f"Bearer {SUPABASE_API_KEY}",
    "Content-Type": "application/json"
}

# Function to fetch data from Supabase
def fetch_data():
    try:
        response = requests.get(
            f"{SUPABASE_URL}/rest/v1/prompt_outputs?select=id,summary,output_text,output_edited,created_at",
            headers=headers
        )
        if response.status_code == 200:
            return response.json()
        else:
            messagebox.showerror("Error", "Failed to fetch data from Supabase")
            return []
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return []

# Function to update data in Supabase
def update_data(id, output_edited):
    try:
        response = requests.patch(
            f"{SUPABASE_URL}/rest/v1/prompt_outputs?id=eq.{id}",
            json={"output_edited": output_edited},
            headers=headers
        )
        if response.status_code == 204:
            messagebox.showinfo("Success", "Data updated successfully")
        else:
            messagebox.showerror("Error", "Failed to update data")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to display data in the table
def display_data():
    rows = fetch_data()
    for i, row in enumerate(rows):
        tree.insert("", "end", values=(row["id"], row["summary"], row["output_text"], row["output_edited"], row["created_at"]))

# Function to handle row selection
def on_row_select(event):
    selected_item = tree.selection()[0]
    values = tree.item(selected_item, "values")
    edit_output_text.delete(1.0, tk.END)
    edit_output_text.insert(tk.END, values[3])
    current_id.set(values[0])

# Function to save the edited data
def save_data():
    id = current_id.get()
    edited_text = edit_output_text.get(1.0, tk.END).strip()
    update_data(id, edited_text)
    refresh_table()

# Function to refresh the table after update
def refresh_table():
    for row in tree.get_children():
        tree.delete(row)
    display_data()

# Set up the main GUI window
root = tk.Tk()
root.title("GPT Workbench GUI")

# Set up the table to display data
tree = ttk.Treeview(root, columns=("ID", "Summary", "Output Text", "Output Edited", "Created At"), show='headings')
tree.heading("ID", text="ID")
tree.heading("Summary", text="Summary")
tree.heading("Output Text", text="Output Text")
tree.heading("Output Edited", text="Output Edited")
tree.heading("Created At", text="Created At")
tree.bind("<<TreeviewSelect>>", on_row_select)
tree.pack()

# Set up the text area for editing output
edit_output_text = tk.Text(root, height=10)
edit_output_text.pack()

# Set up the save button
save_button = tk.Button(root, text="Save", command=save_data)
save_button.pack()

# Variable to hold the current selected ID
current_id = tk.StringVar()

# Display the data in the table
display_data()

# Run the application
root.mainloop()
```

### Explanation:

- **`fetch_data` Function**: This function fetches the data from your Supabase database using the provided API endpoint and credentials. It retrieves the `id`, `summary`, `output_text`, `output_edited`, and `created_at` fields.
- **`update_data` Function**: This function allows you to update the `output_edited` field of a specific record by its `id`.
- **`display_data` Function**: Populates the `Treeview` widget with data from the database.
- **`on_row_select` Function**: Handles row selection in the table, allowing the user to edit the `output_edited` field in the `Text` widget.
- **`save_data` Function**: Saves the edited content back to Supabase by calling the `update_data` function.

### Running the Application

To run the GUI application:

1. Save the above script to a file named `gpt_workbench_gui.py`.
2. Run the script using Python:
   ```bash
   python3 gpt_workbench_gui.py
   ```

This script will create a simple GUI that shows the contents of the `prompt_outputs` table in a table format, allows you to select a row, edit the `output_edited` field, and save the changes back to your Supabase database.

This is a basic implementation and can be expanded with additional features, such as adding new records, deleting records, pagination, or more advanced editing capabilities.