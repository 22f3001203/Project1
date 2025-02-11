import os

def read_file(file_path: str) -> str:
    """Reads the contents of a file and returns it as a string."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
    
def write_file(file_path: str, content: str) -> None:
    """Writes content to a file."""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)
