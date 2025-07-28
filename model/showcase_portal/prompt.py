class Prompt:
    def __init__(self, prompt_text: str, prompt_name: str):
        self.prompt_text = prompt_text
        self.prompt_name = prompt_name

    def __str__(self) -> str:
        return f"{self.prompt_name}: {self.prompt_text}"

    def __repr__(self) -> str:
        return f"Prompt(name={self.prompt_name!r}, text={self.prompt_text!r})"

    def __del__(self):
        print(f"Prompt '{self.prompt_name}' with text '{self.prompt_text}' is being deleted.")

    def copy(self) -> 'Prompt':
        """Create a copy of the current prompt."""
        return Prompt(self.prompt_text, self.prompt_name)

    def update(self, new_text: str) -> 'Prompt':
        """Update the prompt text."""
        self.prompt_text = new_text
        print(f"Prompt '{self.prompt_name}' updated to: {self.prompt_text}")
        return self


