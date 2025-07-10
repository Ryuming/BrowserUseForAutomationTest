import json 


class FileHandler:
    def __init__(self, filePath):
        self.filePath = filePath

    def readAndPrintJSON(self):
        """Read a JSON file and return its content."""
        try:
            with open(self.filePath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data
        except FileNotFoundError:
            print(f"File {self.filePath} not found.")
            return None
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file {self.filePath}.")
            return None

    def writeJSON(self, data):
        """Write data to a JSON file."""
        try:
            with open(self.filePath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"Data successfully written to {self.filePath}.")
        except IOError as e:
            print(f"Error writing to file {self.filePath}: {e}")    

    def appendJSON(self, data):
        """Append data to a JSON file."""
        try:
            with open(self.filePath, 'a', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
                f.write('\n')  # Add a newline for readability
            print(f"Data successfully appended to {self.filePath}.")
        except IOError as e:
            print(f"Error appending to file {self.filePath}: {e}")

    def clearFile(self):
        """Clear the content of a JSON file."""
        try:
            with open(self.filePath, 'w', encoding='utf-8') as f:
                f.truncate(0)  # Clear the file content
            print(f"File {self.filePath} has been cleared.")
        except IOError as e:
            print(f"Error clearing file {self.filePath}: {e}")

    def fileExists(self):
        """Check if the file exists."""
        try:
            with open(self.filePath, 'r', encoding='utf-8'):
                return True
        except FileNotFoundError:
            return False
        except IOError as e:
            print(f"Error checking file {self.filePath}: {e}")
            return False

    def getFilePath(self):
        """Return the file path."""
        return self.filePath

    def setFilePath(self, newPath):
        """Set a new file path."""
        self.filePath = newPath
        print(f"File path updated to {self.filePath}.")

    def readFile(self) -> str:
        """Read the content of the file."""
        try:
            with open(self.filePath, 'r', encoding='utf-8') as f:
                content = f.read()
            return content
        except FileNotFoundError:
            print(f"File {self.filePath} not found.")
            return ""
        except IOError as e:
            print(f"Error reading file {self.filePath}: {e}")
            return ""

    def writeFile(self, content):
        """Write content to the file."""
        try:
            with open(self.filePath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Content successfully written to {self.filePath}.")
        except IOError as e:
            print(f"Error writing to file {self.filePath}: {e}")