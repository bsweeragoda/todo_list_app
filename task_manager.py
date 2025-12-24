from models import Task

def add_task(tasks, task):
    tasks.append(task.to_dict())

def delete_task(tasks, index):
    tasks.pop(index)

def mark_completed(tasks, index):
    tasks[index]["status"] = "Completed"
