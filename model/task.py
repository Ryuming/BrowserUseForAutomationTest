

class Task:
    def __init__(self, taskID, taskName):
        self.taskID = taskID
        self.taskName = taskName

    #Copy constructor
    @classmethod
    def copy(cls, task):
        return cls(task.taskID, task.taskName)

    #Destructor
    def __del__(self):
        print(f"Task {self.taskID} with description '{self.taskName}' is being deleted.")


    
    
