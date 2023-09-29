import os
import re

# specify the folder which containes the files and the text file
file_path = r'F:\ContentList.txt'
folder_path = r'F:\a'

# Initialize an empty list to store the lines from the file
lines = []

#counter to appened number in front of the lines
counter = 1;

# Open and read the file line by line
with open(file_path, 'r') as file:
    for line in file:
        # Remove leading and trailing whitespace (including newline characters)
        line = line.strip()
        invalid_chars_pattern = r'[\/:*?"<>|]'
        # Replace invalid characters with the specified replacement character
        clean_name = re.sub(invalid_chars_pattern, " ", line)
        # Append the line to the list
        lines.append(f"{counter} - {clean_name}")
        counter += 1

# print the list created
for line in lines:
    print(line)

#store the list of files that needs to be renamed + make sure they are sorted in ascending order of number
files = sorted(os.listdir(folder_path), key=lambda x: int(x.split('.')[0]))

#logic to append the lines from the text file to the original file names
for i, file_name in enumerate(files):
        if os.path.isfile(os.path.join(folder_path, file_name)):
            # Get the file extension
            _, file_extension = os.path.splitext(file_name)
            
            # Create the new file name by appending the value and extension
            new_file_name = f"{lines[i]}{file_extension}"
            
            # Rename the file
            old_path = os.path.join(folder_path, file_name)
            new_path = os.path.join(folder_path, new_file_name)
            
            try:
                os.rename(old_path, new_path)
                print(f'Renamed: {old_path} -> {new_path}')
            except Exception as e:
                print(f"Error renaming {old_path}: {str(e)}")