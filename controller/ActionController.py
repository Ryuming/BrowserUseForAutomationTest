

class ActionController:
    def __init__(self):
        self.actions = []
        
    def selectAction(self, actionID, targetObject)
        """Select an action based on the action ID and target object."""
        if actionID == 1:
            return self.openBrowser(targetObject)
        elif actionID == 2:
            return self.clickElement(targetObject)
        elif actionID == 3:
            return self.fillForm(targetObject)
        else:
            raise ValueError("Invalid action ID")

