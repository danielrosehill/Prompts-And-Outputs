---
title: "Script for generating date folders interactively"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Please write a Python script whose purpose is to generate year and month folders. It's an interactive terminal application.

Firstly, the script should ask the user whether it wants to generate the folders in the directory the script is running in (option 1, default) or in another directory (2)

If the user opts for 2, the script asks the user to provide the path.

Next the script asks the user which years it wishes to develop directories for.

The options are 2022,2023,2024,2025,2026,2027,2028,2029,2030

The user "chooses" by using the space bar to denote x marks. The user can choose all of the options are only 1.

Finally the script generates the requested folders at the requested location.

The folders for the years are generated with the last two numbers. So 2023 should be created as 23. Within each year folder there are 12 subfolders numbered 1 through 12. Each folder corresponds to a month.

Then the script ends.

# Output

Here is a Python script that accomplishes the task of generating year and month folders as specified. It uses the `curses` library for interactive terminal input and can generate folders in the current directory or in a custom path.

```python
import os
import curses

# Function to choose a directory
def choose_directory():
    choice = input("Where would you like to generate folders?\n1. Current directory (default)\n2. Specify a directory\nEnter 1 or 2: ").strip()
    if choice == '2':
        directory = input("Please provide the full path to the directory: ").strip()
        if not os.path.exists(directory):
            print("Directory does not exist. Exiting.")
            return None
    else:
        directory = os.getcwd()
    return directory

# Function to show and get year selections from the user
def choose_years():
    years = ["2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"]
    selected_years = []
    
    def interactive_menu(stdscr):
        curses.curs_set(0)  # Hide cursor
        stdscr.clear()
        stdscr.addstr("Use SPACE to select/deselect years. Press ENTER when done.\n")
        selected = [False] * len(years)
        current_idx = 0

        while True:
            for idx, year in enumerate(years):
                if idx == current_idx:
                    stdscr.addstr(idx + 2, 0, f"> {year}", curses.A_REVERSE)
                else:
                    mark = "x" if selected[idx] else " "
                    stdscr.addstr(idx + 2, 0, f"  [{mark}] {year}")

            key = stdscr.getch()

            if key == curses.KEY_UP and current_idx > 0:
                current_idx -= 1
            elif key == curses.KEY_DOWN and current_idx < len(years) - 1:
                current_idx += 1
            elif key == ord(' '):
                selected[current_idx] = not selected[current_idx]
            elif key == ord('\n'):
                break

        return [years[i] for i, sel in enumerate(selected) if sel]

    selected_years = curses.wrapper(interactive_menu)
    return selected_years

# Function to create the year and month folders
def create_folders(directory, years):
    for year in years:
        year_short = year[-2:]
        year_path = os.path.join(directory, year_short)
        os.makedirs(year_path, exist_ok=True)

        for month in range(1, 13):
            month_path = os.path.join(year_path, str(month))
            os.makedirs(month_path, exist_ok=True)
        print(f"Created folders for {year_short} in {year_path}")

def main():
    # Step 1: Choose directory
    directory = choose_directory()
    if directory is None:
        return

    # Step 2: Choose years
    selected_years = choose_years()
    if not selected_years:
        print("No years selected. Exiting.")
        return

    # Step 3: Generate the folders
    create_folders(directory, selected_years)
    print("Folder generation complete.")

if __name__ == "__main__":
    main()
```

### How it works:
1. **Directory Selection**: It first asks if the user wants to generate folders in the current directory or another specified location.
2. **Year Selection**: It uses the `curses` library to display a menu where the user can use the spacebar to select years. After making the selection, pressing "Enter" finalizes the choice.
3. **Folder Generation**: Based on the selected years, the script creates year folders with the last two digits and 12 subfolders (one for each month).

### Requirements:
To run this script, you must have Python installed. The `curses` library comes pre-installed on Unix-based systems (Linux/macOS). For Windows, you'll need the `windows-curses` package.

To install `windows-curses` (for Windows users), run:
```bash
pip install windows-curses
```