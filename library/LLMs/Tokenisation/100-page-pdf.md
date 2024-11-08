import os
import random
import tkinter as tk
from tkinter import filedialog, messagebox
import markdown
from tkinter import scrolledtext
import json

CONFIG_PATH = os.path.expanduser("~/.config/markdown_gui_config.json")

class MarkdownEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Markdown Editor")
        self.root.geometry("800x600")
        self.base_directory = None
        self.current_file_path = None
        self.previous_file_path = None
        self.file_history = []
        self.font_size = 14
        
        self.create_widgets()
        self.load_config()

    def create_widgets(self):
        # Directory Selection
        self.dir_frame = tk.Frame(self.root)
        self.dir_frame.pack(pady=10)
        
        self.dir_label = tk.Label(self.dir_frame, text="Base Directory: Not Set", wraplength=600)
        self.dir_label.pack(side=tk.LEFT)
        
        self.dir_button = tk.Button(self.dir_frame, text="Set Directory", command=self.set_directory)
        self.dir_button.pack(side=tk.LEFT, padx=5)
        
        # Markdown Text Area
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, font=("Arial", self.font_size))
        self.text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        
        # Buttons Frame
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)
        
        self.save_button = tk.Button(self.button_frame, text="Save", command=self.save_file)
        self.save_button.pack(side=tk.LEFT, padx=5)
        
        self.next_button = tk.Button(self.button_frame, text="Next", command=self.load_random_file)
        self.next_button.pack(side=tk.LEFT, padx=5)
        
        self.previous_button = tk.Button(self.button_frame, text="Previous", command=self.load_previous_file)
        self.previous_button.pack(side=tk.LEFT, padx=5)
        
        self.increase_font_button = tk.Button(self.button_frame, text="Increase Font Size", command=self.increase_font_size)
        self.increase_font_button.pack(side=tk.LEFT, padx=5)
        
        self.decrease_font_button = tk.Button(self.button_frame, text="Decrease Font Size", command=self.decrease_font_size)
        self.decrease_font_button.pack(side=tk.LEFT, padx=5)
        
        # Keyboard Shortcut for Save
        self.root.bind("<Control-s>", lambda event: self.save_file())

    def load_config(self):
        if os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, 'r') as f:
                config = json.load(f)
                self.base_directory = config.get('base_directory')
                if self.base_directory:
                    self.dir_label.config(text=f"Base Directory: {self.base_directory}")
                    self.load_random_file()

    def save_config(self):
        with open(CONFIG_PATH, 'w') as f:
            json.dump({'base_directory': self.base_directory}, f)

    def set_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.base_directory = directory
            self.dir_label.config(text=f"Base Directory: {self.base_directory}")
            self.save_config()
            self.load_random_file()

    def load_random_file(self):
        if not self.base_directory:
            messagebox.showwarning("Warning", "Please set the base directory first.")
            return
        
        markdown_files = []
        for root, _, files in os.walk(self.base_directory):
            markdown_files.extend([os.path.join(root, file) for file in files if file.endswith('.md')])
        
        if not markdown_files:
            messagebox.showwarning("Warning", "No markdown files found in the selected directory.")
            return
        
        if self.current_file_path:
            self.file_history.append(self.current_file_path)
        
        self.current_file_path = random.choice(markdown_files)
        with open(self.current_file_path, 'r') as f:
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, f.read())

    def load_previous_file(self):
        if self.file_history:
            self.current_file_path = self.file_history.pop()
            with open(self.current_file_path, 'r') as f:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, f.read())
        else:
            messagebox.showwarning("Warning", "No previous file to load.")

    def save_file(self):
        if self.current_file_path:
            with open(self.current_file_path, 'w') as f:
                f.write(self.text_area.get(1.0, tk.END))
            messagebox.showinfo("Info", "File saved successfully!")
        else:
            messagebox.showwarning("Warning", "No file loaded to save.")

    def increase_font_size(self):
        self.font_size += 2
        self.text_area.config(font=("Arial", self.font_size))

    def decrease_font_size(self):
        if self.font_size > 4:
            self.font_size -= 2
            self.text_area.config(font=("Arial", self.font_size))

if __name__ == "__main__":
    root = tk.Tk()
    app = MarkdownEditorApp(root)
    root.mainloop()