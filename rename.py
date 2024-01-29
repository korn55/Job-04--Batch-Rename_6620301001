import os

def rename_files(directory, file_extension):
    #Check if the Directory exists or not.
    if not os.path.exists(directory):
        print(f"Directory '{directory}' ไม่พบ")
        return
    
# Collect all files in the Directory with the file_extension extension.
    files = [file for file in os.listdir(directory) if file.endswith(file_extension)]

# Sort files by name
    files.sort()


    for i, file in enumerate(files, start=1):

        new_name = f"{i:03d}{file_extension}"

        old_path = os.path.join(directory, file)
    ew_path = os.path.join(directory, new_name)

    os.rename(old_path, new_path)
    print(f"Rename: {file} = {new_name}")


directory_path = "D:/Job-04--Batch-Rename_6620301001"  
file_extension_to_rename = ".jpg"
rename_files(directory_path, file_extension_to_rename)
