import tkinter as tk
from tkinter import messagebox
from dashboard import Dashboard
from auth import register_user, authenticate_user, reset_password


class LoginWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("To-Do List - Login")
        self.root.geometry("450x250")
        self.root.resizable(False, False)

        self.build_login_ui()

    # ---------- LOGIN UI ----------
    def build_login_ui(self):
        self.clear_window()
        self.root.geometry("450x250")

        main_frame = tk.Frame(
            self.root, bd=2, relief="solid",
            highlightbackground="black", highlightthickness=1
        )
        main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

        # Title
        tk.Label(main_frame, text="Login", font=("Arial", 16, "bold")) \
            .grid(row=0, column=0, columnspan=2, pady=10)

        # Username
        tk.Label(main_frame, text="Username", width=12, anchor="e") \
            .grid(row=1, column=0, padx=10, pady=5)
        self.username_entry = tk.Entry(main_frame, width=30)
        self.username_entry.grid(row=1, column=1, padx=10, pady=5)

        # Password
        tk.Label(main_frame, text="Password", width=12, anchor="e") \
            .grid(row=2, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(main_frame, show="*", width=30)
        self.password_entry.grid(row=2, column=1, padx=10, pady=5)

        # Buttons
        btn_frame = tk.Frame(main_frame)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=15)

        tk.Button(
            btn_frame, text="Login",
            bg="blue", fg="white",
            font=("Arial", 10, "bold"),
            width=10, command=self.login
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            btn_frame, text="Sign Up",
            bg="green", fg="white",
            font=("Arial", 10, "bold"),
            width=10, command=self.build_signup_ui
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            btn_frame, text="Forgot?",
            bg="orange", fg="white",
            font=("Arial", 10, "bold"),
            width=10, command=self.build_forgot_ui
        ).grid(row=0, column=2, padx=5)

    # ---------- SIGN UP UI ----------
    def build_signup_ui(self, preset_username=""):
        self.clear_window()
        self.root.geometry("450x280")

        main_frame = tk.Frame(
            self.root, bd=2, relief="solid",
            highlightbackground="black", highlightthickness=1
        )
        main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

        tk.Label(main_frame, text="Sign Up", font=("Arial", 16, "bold")) \
            .grid(row=0, column=0, columnspan=2, pady=10)

        # Username
        tk.Label(main_frame, text="Username", width=12, anchor="e") \
            .grid(row=1, column=0, padx=10, pady=5)
        self.su_username = tk.Entry(main_frame, width=30)
        self.su_username.grid(row=1, column=1, padx=10, pady=5)
        self.su_username.insert(0, preset_username)

        # Password
        tk.Label(main_frame, text="Password", width=12, anchor="e") \
            .grid(row=2, column=0, padx=10, pady=5)
        self.su_password = tk.Entry(main_frame, show="*", width=30)
        self.su_password.grid(row=2, column=1, padx=10, pady=5)

        # Confirm
        tk.Label(main_frame, text="Confirm", width=12, anchor="e") \
            .grid(row=3, column=0, padx=10, pady=5)
        self.su_confirm = tk.Entry(main_frame, show="*", width=30)
        self.su_confirm.grid(row=3, column=1, padx=10, pady=5)

        # Buttons
        btn_frame = tk.Frame(main_frame)
        btn_frame.grid(row=4, column=0, columnspan=2, pady=15)

        tk.Button(
            btn_frame, text="Create",
            bg="blue", fg="white",
            font=("Arial", 10, "bold"),
            width=12, command=self.signup
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            btn_frame, text="Back",
            bg="gray", fg="white",
            font=("Arial", 10, "bold"),
            width=12,
            command=lambda: self.build_login_ui()
        ).grid(row=0, column=1, padx=5)

    # ---------- FORGOT PASSWORD ----------
    def build_forgot_ui(self):
        username = self.username_entry.get().strip()
        if not username:
            messagebox.showerror("Error", "Enter your username first")
            return
        self.build_signup_ui(preset_username=username)

    # ---------- LOGIC ----------
    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "All fields required")
            return

        if authenticate_user(username, password):
            self.root.destroy()     
            Dashboard(username)
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def signup(self):
        if self.su_password.get() != self.su_confirm.get():
            messagebox.showerror("Error", "Passwords do not match")
            return

        if register_user(self.su_username.get(), self.su_password.get()):
            messagebox.showinfo("Success", "Account created")
        else:
            reset_password(self.su_username.get(), self.su_password.get())
            messagebox.showinfo("Success", "Password reset")

        self.build_login_ui()

    # ---------- UTILITY ----------
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def run(self):
        self.root.mainloop()
