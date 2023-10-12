import os

# Function to delete files with a specific extension recursively
def delete_files_with_extension(root_folder, extension):
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Deleted: {file_path}")

# Specify the root folder and the extension you want to delete
root_folder = 'F:\Courses\Java\Design Patterns in Java - Concepts & Hands On Projects'
extension = 'output_demuxer.mp4'

# Call the function to delete .srt files recursively
delete_files_with_extension(root_folder, extension)
