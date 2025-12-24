📝 To-Do List Desktop Application (Python + Tkinter)

A simple and user-friendly desktop To-Do List application built using Python and Tkinter, featuring user authentication, task management, and a clean GUI.
Each user has their own task list, securely managed after login.

🚀 Features
🔐 Authentication

Login system

Sign-up (new account creation)
Forgot password (password reset)
Secure credential handling

📋 Task Management

Add new tasks
Set task priority, category, and due date
Mark tasks as completed
Delete tasks
Tasks are saved per user

🖥 User Interface

Clean Tkinter GUI
Row-based form layout
Colored buttons for better UX
Date picker for due dates
Logout functionality

🛠 Technologies Used

Python 3.9+
Tkinter (GUI framework)
tkcalendar (date picker)
JSON (local data storage)

📦 Requirements
Python Version
Python 3.9 or higher
Python Packages
Install dependencies using:
tkcalendar==1.6.1

⚠️ tkinter is included with Python and should not be installed via pip.

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/todo_list_app.git
cd todo_list_app

2️⃣ (Optional) Create Virtual Environment
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate # macOS / Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
python main.py

🧪 How It Works

Launch the application
Create a new account or log in
Add tasks with due dates and priorities
Manage tasks from the dashboard
Logout safely when done
All data is stored locally and separated per user.

🔒 Notes & Limitations

This is a desktop-only application
Data is stored locally (JSON)
Not intended for production authentication systems
Ideal for learning Tkinter, GUI layouts, and basic app architecture

🎓 Educational Value

This project demonstrates:
Tkinter layout management (grid, frame)
Window lifecycle handling
Modular Python design
Simple authentication logic
Event-driven programming

📜 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute it.

👤 Author

Buddhi Sampath
📍 Sri Lanka
🎓 Undergraduate | Software Development
