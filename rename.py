import os

def rename_files(directory, file_extension):
    #Check if the Directory exists or not.
    if not os.path.exists(directory):
        print(f"Directory '{directory}' Not found")
        return
    
# Collect all files in the Directory with the file_extension extension.
    files = [file for file in os.listdir(directory) if file.endswith(file_extension)]

# Sort files by name
    files.sort()

    # Rename files in numerical order
    for i, file in enumerate(files, start=1):
        # Create a new file name
        new_name = f"{i:03d}{file_extension}"
        
        # Create the full file path
        old_path = os.path.join(directory, file)
        new_path = os.path.join(directory, new_name)

        # rename file
        os.rename(old_path, new_path)
        print(f"Rename: {file} = {new_name}")

# Call the function
directory_path = "D:/git_hub_repossi/Job-04--Batch-Rename_6620301001"  
file_extension_to_rename = ".jpg"
rename_files(directory_path, file_extension_to_rename)
