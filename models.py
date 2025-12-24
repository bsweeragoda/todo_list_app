class Task:
    def __init__(self, name, priority, due_date, category, status="Pending"):
        self.name = name
        self.priority = priority
        self.due_date = due_date
        self.category = category
        self.status = status

    def to_dict(self):
        return self.__dict__
