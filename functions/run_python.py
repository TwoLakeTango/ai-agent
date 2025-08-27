def run_python_file(working_directory, file_path, args=[]):
    target_file_path = os.path.abspath(os.path.join(working_directory,file_path))
    abs_working_dir = os.path.abspath(working_directory)
    try:
        if not target_file_path.startswith(abs_working_dir):
            return f'Error: Cannot execute "{target_file_path}" as it is outside the permitted working directory'
        elif not os.path.exists(target_file_path):
            return f'Error: File "{target_file_path}" not found.'
        elif target_file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'
        else:
            subprocess.run()
    except: f"Error: executing Python file: {e}"