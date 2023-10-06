import os
import glob

# Specify the folder path where your video files are located
folder_path = 'H:\Ashwin Courses Backup\Development\DSA'

num_video_files = 0

# Use os.walk to traverse the directory and its subdirectories
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.mp4') or file.endswith('.mkv'):
            num_video_files += 1

print(f"Number of .mp4 and .mkv files in the folder and its subfolders: {num_video_files}")
