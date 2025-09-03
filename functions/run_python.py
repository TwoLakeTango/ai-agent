import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    target_file_path = os.path.abspath(os.path.join(working_directory,file_path))
    abs_working_dir = os.path.abspath(working_directory)
    try:
        if not target_file_path.startswith(abs_working_dir):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        elif not os.path.exists(target_file_path):
            return f'Error: File "{file_path}" not found.'
        elif not target_file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'
        else:
            #run_output = subprocess.run([args], timeout=30, cwd=abs_working_dir, capture_output=True)
            run_output = subprocess.run(
                ['python', file_path, *args],
                timeout=30,
                cwd=abs_working_dir,
                capture_output=True
                )
            if run_output.returncode != 0:
                return f'Process existed with code {run_output.returncode}'
            elif run_output == None:
                return 'No output produced.'
            return f'STDOUT: {run_output.stdout}, STDERR: {run_output.stderr}'
    except Exception as e: 
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes the python file at the specified location.",
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