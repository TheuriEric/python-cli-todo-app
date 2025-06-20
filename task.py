
class Task():
    def __init__(self, id,title,description, due_date, completed):##Initialize the attributes
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def mark_complete(self):

        self.completed = "Completed"

    def to_dict(self):
        return {
            "Id": self.id,
            "Title": self.title,
            "Description" : self.description,
            "Due date" : self.due_date,
            "Status" : self.completed
        }



    def __str__(self):
        return f"{self.id} {self.title} {self.description} {self.due_date} {self.completed}"
    
