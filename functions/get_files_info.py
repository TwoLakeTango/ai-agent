import os

def get_files_info(working_directory, directory="."):
    output = []
    target_dir = os.path.abspath(os.path.join(working_directory, directory))
    abs_working_dir = os.path.abspath(working_directory)
    try:
        if not target_dir.startswith(abs_working_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        elif not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        else:
            for file in os.listdir(target_dir):
                file_path = os.path.join(target_dir, file)
                file_size = os.path.getsize(file_path)
                is_dir = os.path.isdir(file_path)
                output.append(f"- {file}: file_size={file_size} bytes, is_dir={is_dir}")
            #return "Result for current directory:"
            return "\n".join(output)
    except Exception as e:
        return f"Error: {e}"
    

    #return absolute_directory
    #if working_directory not in absolute_directory:
        #return f'Error: cannot list "{directory}" as it is outsize the permitted working directory'
    
    
"""file_paths = []
    for node_name, content in working_directory.items():
        new_path = f"{directory}/{node_name}"
        if content is None:
            file_paths.append(new_path)
        else:
            file_paths.extend(get_files_into(content, new_path))
    return file_paths"""