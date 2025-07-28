class interactive_button:
    def __init__(self, name: str, use: str):
        self._name = name
        self._use = use

    def __str__(self):
        return f"Button(name={self._name}, use={self._use})"

    
    def __init__(self, name: str, use: str):
        self._name = name
        self._use = use
    
    @classmethod
    # Create a copy of another Button object
    def copy(cls, other):
        return cls(other._name, other._use)
    

    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def use(self):
        return self._use
    
    @use.setter
    def use(self, value):
        self._use = value
