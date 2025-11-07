import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    abs_path = os.path.abspath(full_path)
    working_abs_path = os.path.abspath(working_directory)
    if not working_abs_path.endswith(os.sep):
        working_abs_path += os.sep

    if not (abs_path.startswith(working_abs_path) or abs_path == os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
    if os.path.isdir(abs_path):   
        try:
            file_list = os.listdir(abs_path)
            string = ""
            for file in file_list:
                full_file_path = os.path.join(abs_path, file)
                string += f"- {file}: file_size={os.path.getsize(full_file_path)} bytes, is_dir={os.path.isdir(full_file_path)}\n"
            return string
        except Exception as e:
            return f"Error: {e}"
    else:
        return f'Error: "{directory}" is not a directory'
    