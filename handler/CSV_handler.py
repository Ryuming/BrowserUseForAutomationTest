import pandas as pd

class CSVHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        try:
            self.data = pd.read_csv(file_path)
        except Exception:
            self.data = pd.DataFrame()

    def read_csv(self):
        """Read the CSV file and return its content as a DataFrame."""
        try:
            self.data = pd.read_csv(self.file_path)
            print(f"Data successfully read from {self.file_path}.")
            return self.data
        except FileNotFoundError:
            print(f"File {self.file_path} not found.")
            return None
        except pd.errors.EmptyDataError:
            print(f"File {self.file_path} is empty.")
            return None
        except pd.errors.ParserError:
            print(f"Error parsing CSV file {self.file_path}.")
            return None

    def write_csv(self, data):
        """Write a DataFrame to a CSV file."""
        try:
            data.to_csv(self.file_path, index=False)
            print(f"Data successfully written to {self.file_path}.")
        except IOError as e:
            print(f"Error writing to file {self.file_path}: {e}")

    def append_csv(self, data):
        """Append a DataFrame to a CSV file."""
        try:
            data.to_csv(self.file_path, mode='a', header=False, index=False)
            print(f"Data successfully appended to {self.file_path}.")
        except IOError as e:
            print(f"Error appending to file {self.file_path}: {e}")

    def clear_file(self):
        """Clear the content of the CSV file."""
        try:
            with open(self.file_path, 'w') as f:
                f.truncate(0)  # Clear the file content
            print(f"File {self.file_path} has been cleared.")
        except IOError as e:
            print(f"Error clearing file {self.file_path}: {e}")

    def get_dataframe(self) -> pd.DataFrame:
        """Return the DataFrame containing the CSV data."""
        return self.data

    def get_num_rows(self) -> int:
        """Return the number of rows in the DataFrame."""
        return len(self.data)-1

    def get_num_columns(self) -> int:
        """Return the number of columns in the DataFrame."""
        return len(self.data.columns)

    