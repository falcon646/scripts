import os
import shutil

# Specify the directory where the .mp4 files are located
folder_path = "F:\Courses\zerotomastery\DevOps Bootcamp Terraform"

# List all files in the folder and its subfolders
for root, _, files in os.walk(folder_path):
    for filename in files:
        if filename.endswith(".mp4"):
            # Get the full path of the .mp4 file
            file_path = os.path.join(root, filename)
            
            # Determine the new location in the parent folder
            new_path = os.path.join(folder_path, filename)
            
            try:
                # Move the file to the parent folder
                shutil.move(file_path, new_path)
                print(f"Moved: {file_path} to {new_path}")
            except Exception as e:
                print(f"An error occurred: {e}")


# move all video files inside the subdirs (of the root dir provided ) one directiry up 