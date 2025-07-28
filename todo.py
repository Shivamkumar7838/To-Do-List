import tkinter as tk
from tkinter import messagebox, simpledialog
import os

# Save file path
FILE_NAME = "tasks.txt"

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.task_listbox = tk.Listbox(root, width=50, height=15, font=("Arial", 12))
        self.task_listbox.pack(pady=10)

        self.entry = tk.Entry(root, width=40, font=("Arial", 12))
        self.entry.pack(pady=5)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        add_btn = tk.Button(btn_frame, text="Add Task", width=12, command=self.add_task)
        add_btn.grid(row=0, column=0, padx=5)

        del_btn = tk.Button(btn_frame, text="Delete Task", width=12, command=self.delete_task)
        del_btn.grid(row=0, column=1, padx=5)

        save_btn = tk.Button(btn_frame, text="Save Tasks", width=12, command=self.save_tasks)
        save_btn.grid(row=0, column=2, padx=5)

        load_btn = tk.Button(btn_frame, text="Load Tasks", width=12, command=self.load_tasks)
        load_btn.grid(row=0, column=3, padx=5)

        self.load_tasks()

    def add_task(self):
        task = self.entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            self.task_listbox.delete(selected)
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def save_tasks(self):
        with open(FILE_NAME, "w") as f:
            tasks = self.task_listbox.get(0, tk.END)
            for task in tasks:
                f.write(task + "\n")
        messagebox.showinfo("Success", "Tasks saved successfully!")

    def load_tasks(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as f:
                for line in f:
                    task = line.strip()
                    if task:
                        self.task_listbox.insert(tk.END, task)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
