class Task():
    def __init__(self, id,title,description, due_date, completed):##Initialize the attributes
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def mark_complete(self):
        pass

    def to_dict(self):
        pass

    def __str__(self):
        return f"{self.id} {self.title} {self.description} {self.due_date} {self.completed}"
    
    