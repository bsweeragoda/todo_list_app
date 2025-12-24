import tkinter as tk
from tkinter import ttk, messagebox
from streamlit import form
from tkcalendar import DateEntry
from storage import load_tasks, save_tasks
from models import Task

class Dashboard:
    def __init__(self, username):
        self.username = username
        self.tasks = load_tasks(username)

        self.root = tk.Tk()
        self.root.title("To-Do List Dashboard")
        self.root.geometry("900x500")

        self.build_ui()
        self.refresh_tasks()
        self.root.mainloop()

    def build_ui(self):
        main = tk.Frame(self.root, padx=15, pady=15)
        main.pack(fill="both", expand=True)

        tk.Label(
            main,
            text=f"Welcome, {self.username}",
            font=("Arial", 18, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=10)

        # ---------- FORM ----------
        form = tk.LabelFrame(main, text="Task Details", padx=10, pady=10)
        form.grid(row=1, column=0, sticky="nw")

        labels = ["Task Name", "Priority", "Category", "Due Date"]
        for i, label in enumerate(labels):
            tk.Label(form, text=label).grid(row=i, column=0, sticky="w", pady=5)

        self.name_entry = tk.Entry(form, width=25)
        self.name_entry.grid(row=0, column=1)

        self.priority = ttk.Combobox(form, values=["High", "Low"], state="readonly")
        self.priority.grid(row=1, column=1)

        self.category = ttk.Combobox(
            form, values=["Work", "Personal", "Study"], state="readonly"
        )
        self.category.grid(row=2, column=1)

        self.due_date = DateEntry(form)
        self.due_date.grid(row=3, column=1)

        # ---------- BUTTONS ----------
        buttons = tk.Frame(main)
        buttons.grid(row=2, column=0, pady=10)

        tk.Button(buttons, text="Add Task", width=12, command=self.add_task)\
            .grid(row=0, column=0, padx=5)

        tk.Button(buttons, text="Delete Task", width=12, command=self.delete_task)\
            .grid(row=0, column=1, padx=5)

        tk.Button(buttons, text="Complete Task", width=15, command=self.complete_task)\
            .grid(row=0, column=2, padx=5)

        # ---------- TOP BAR ----------
        top_bar = tk.Frame(main)
        top_bar.grid(row=0, column=0, columnspan=2, sticky="ew", pady=10)
        top_bar.columnconfigure(0, weight=1)

        # Welcome label on the left
        tk.Label(
            top_bar,
            text=f"Welcome, {self.username}",
            font=("Arial", 18, "bold")
        ).grid(row=0, column=0, sticky="w")

        # Logout button on the right (red)
        tk.Button(
            top_bar,
            text="Logout",
            font=("Arial", 10, "bold"),
            fg="white",
            bg="red",
            activebackground="#cc0000",
            activeforeground="white",
            relief="raised",
            padx=10,
            pady=3,
            command=self.logout
        ).grid(row=0, column=1, sticky="e")

        # ---------- TASK LIST ----------
        list_frame = tk.LabelFrame(main, text="Tasks")
        list_frame.grid(row=1, column=1, rowspan=2, sticky="nsew", padx=10)

        self.task_list = tk.Listbox(list_frame, width=80)
        self.task_list.pack(fill="both", expand=True)

        main.columnconfigure(1, weight=1)
        main.rowconfigure(1, weight=1)

    # ---------- LOGIC ----------
    def add_task(self):
        name = self.name_entry.get().strip()
        priority = self.priority.get()
        category = self.category.get()
        due_date = self.due_date.get_date().strftime("%Y-%m-%d")

        if not name or not priority or not category:
            messagebox.showerror("Error", "All fields are required")
            return

        task = Task(name, priority, due_date, category)
        self.tasks.append(task.to_dict())
        save_tasks(self.username, self.tasks)
        self.refresh_tasks()

        self.name_entry.delete(0, tk.END)
        self.priority.set("")
        self.category.set("")

    def delete_task(self):
        selected = self.task_list.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Select a task to delete")
            return

        index = selected[0]
        self.tasks.pop(index)
        save_tasks(self.username, self.tasks)
        self.refresh_tasks()

    def complete_task(self):
        selected = self.task_list.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Select a task to complete")
            return

        index = selected[0]
        self.tasks[index]["status"] = "Completed"
        save_tasks(self.username, self.tasks)
        self.refresh_tasks()

    def refresh_tasks(self):
        self.task_list.delete(0, tk.END)

        for i, task in enumerate(self.tasks, start=1):
            icon = "✔" if task["status"] == "Completed" else "⏳"
            text = (
                f"{i}. {icon} {task['name']} | "
                f"{task['priority']} | "
                f"{task['category']} | "
                f"{task['due_date']} | "
                f"{task['status']}"
            )
            self.task_list.insert(tk.END, text)

    # create logout function
    def logout(self):
        from login import LoginWindow  
        self.root.destroy()  
        LoginWindow().run()  

