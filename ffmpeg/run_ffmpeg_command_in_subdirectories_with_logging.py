import os
import subprocess
import logging

# Configure logging
log_file = 'ffmpeg_errors.log'
logging.basicConfig(filename=log_file, level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def run_ffmpeg_command_in_subdirectories(root_directory):
    for root, dirs, files in os.walk(root_directory):
        for directory in dirs:
            subdirectory_path = os.path.join(root, directory)
            merge_txt_path = os.path.join(subdirectory_path, 'merge.txt')
            output_demuxer_path = os.path.join(subdirectory_path, 'output_demuxer.mp4')
            
            try:
                # Run the ffmpeg command in the subdirectory
                subprocess.run(['ffmpeg', '-f', 'concat', '-safe', '0', '-i', merge_txt_path, '-c', 'copy', output_demuxer_path])
                print(f'Successfully ran ffmpeg command in {subdirectory_path}')
            except Exception as e:
                error_message = f'Error running ffmpeg command in {subdirectory_path}: {e}'
                print(error_message)
                logging.error(error_message)

# Root directory where you want to run the ffmpeg command in subdirectories
root_directory = 'F:\Courses\Java\Design Patterns in Java - Concepts & Hands On Projects'  # Replace with the actual root directory

# Call the function to run the ffmpeg command in subdirectories
run_ffmpeg_command_in_subdirectories(root_directory)



# same as run_ffmpeg_command_in_subdirectories with loggin support
#  Run ffmpeg -f concat -safe 0 -i join_video.txt -c copy output_demuxer.mp4 in all subfolders from the given root folder to merge the videos Make sure you already have generated the merger.txt and videos_length.txt before running this  
