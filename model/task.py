

class Task:
    def __init__(self, taskID, taskName, prompt):
        self.taskID = taskID
        self.taskName = taskName
        self.prompt = prompt

    #Copy constructor
    @classmethod
    def copy(cls, task):
        return cls(task.taskID, task.taskName, task.prompt)

    #Destructor
    def __del__(self):
        print(f"Task {self.taskID} with description '{self.taskName}' is being deleted.")

    def 
    

    
    
