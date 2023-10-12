import os
import re

# Function to create merge.txt in each subfolder
def create_merge_txt(root_folder):
    for root, dirs, files in os.walk(root_folder):
        merge_txt_path = os.path.join(root, 'merge.txt')
        
        # Filter out only .mp4 files
        mp4_files = [f"'{file}'" for file in files if file.endswith('.mp4')]
        mp4_files.sort(key=lambda x: int(re.search(r'\d+', x).group()))
        
        # Write to merge.txt with the specified format
        with open(merge_txt_path, 'w') as merge_file:
            for mp4_file in mp4_files:
                merge_file.write(f"file {mp4_file}\n")

# Specify the root folder where you want to create merge.txt files
root_folder = 'F:\Courses\Java\Design Patterns in Java - Concepts & Hands On Projects'

# Call the function to create merge.txt files in subfolders
create_merge_txt(root_folder)


# generate merge.txt recursively