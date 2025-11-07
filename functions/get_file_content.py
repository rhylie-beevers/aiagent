import os
from config import *

def get_file_content(working_directory, file_path):
    working_abs_path = os.path.abspath(working_directory)
    full_path = os.path.join(working_directory, file_path)
    abs_path = os.path.abspath(full_path)
    if not working_abs_path.endswith(os.sep):
        working_abs_path += os.sep
    if not (abs_path.startswith(working_abs_path) or abs_path == os.path.abspath(working_directory)):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory' 
    if not os.path.isfile(abs_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(f.read()) > len(f.read(MAX_CHARS)):
                file_content_string.append([f'...File "{file_path}" truncated at 10000 characters'])
    except Exception as e:
        return f"Error Encountered: {e}"