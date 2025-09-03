import os
from config import max_file_chars
from google.genai import types

def get_file_content(working_directory, file_path):
    output = []
    target_file_path = os.path.abspath(os.path.join(working_directory,file_path))
    abs_working_dir = os.path.abspath(working_directory)
    MAX_CHARS = max_file_chars
    try:
        if not target_file_path.startswith(abs_working_dir):
            return f'Error: Cannot list "{target_file_path}" as it is outside the permitted working directory'
        elif not os.path.isfile(target_file_path):
            return f'Error: File is not found or is not a regular file: {target_file_path}'
        else:
            with open(target_file_path, 'r') as f:
                file_content_string = f.read(MAX_CHARS)
            return f'{file_content_string}[...File "{target_file_path}" truncated at 10000 characters]'
    except Exception as e:
        return f"Error: {e}"
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Lists the content of the file as a string. Truncates the results after 10000 characters.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="This is the path within the working directory at which a specified file lives."
            )
        },
    ),
)