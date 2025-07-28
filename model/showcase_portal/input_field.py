class input_field:
    def __init__(self, name: str, description: str, input_value:str):
        self._name = name
        self._description = description
        self._input_value = input_value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, description: str, input_value: str):
        self._name = value
        self._description = description
        self._input_value = input_value

    @property
    def description(self) -> str:
        return self._description
    
    @property
    def input_value(self) -> str:
        return self._input_value

    @description.setter
    def description(self, description: str):
        self._description = description

    @description.setter
    def input_value(self, input_value: str):
        self._input_value = input_value
        

    @classmethod
    def copy(cls, input_field: 'InputField') -> 'InputField':
        """Create a copy of the given input field."""
        return cls(input_field.name, input_field.description)
