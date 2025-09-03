import os
from google.genai import types

def write_file(working_directory, file_path, content):
    target_file_path = os.path.abspath(os.path.join(working_directory,file_path))
    abs_working_dir = os.path.abspath(working_directory)
    #MAX_CHARS = max_file_chars
    try:
        if not target_file_path.startswith(abs_working_dir):
            return f'Error: Cannot write to "{target_file_path}" as it is outside the permitted working directory'
        elif not os.path.exists(target_file_path):
            os.makedirs(os.path.dirname(target_file_path),exist_ok=True)
            with open(target_file_path, 'w') as f:
                f.write(content)
            return f'Successfully created and wrote to "{target_file_path}" ({len(content)} characters written)'
        else:
            with open(target_file_path, 'w') as f:
                f.write(content)
            return f'Successfully wrote to "{target_file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes to the file at the specified file path. If the file does not exist, then the file is created and the content written.",
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
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="This is the content that is written to the file as part of the request."
            )
        },
    ),
)