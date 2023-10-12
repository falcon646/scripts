import os
import re
import imageio

def process_video_directory(video_directory):
    # Get a list of video files in the directory
    video_files = [f for f in os.listdir(video_directory) if f.endswith('.mp4')]

    # Sort the video files based on the numeric part of the filenames
    video_files.sort(key=lambda x: int(re.search(r'\d+', x).group()))

    # Create a file to write the video lengths and names
    output_file = open(os.path.join(video_directory, 'video_lengths.txt'), 'w')

    total_duration = 0

    for filename in video_files:
        video_path = os.path.join(video_directory, filename)

        try:
            vid = imageio.get_reader(video_path)
        except Exception as e:
            print(f"Error reading video file: {e}")
            continue

        duration = vid.get_meta_data()['duration']
        formatted_duration = '{:02d}:{:02d}'.format(int(total_duration // 60), int(total_duration % 60))
        total_duration += duration
        output_file.write('{} {}\n'.format(formatted_duration, filename))

    # Close the output file
    output_file.close()

    # Print the total duration
    formatted_total_duration = '{:02d}:{:02d}'.format(int(total_duration // 60), int(total_duration % 60))
    print('Total Duration for {}: {}'.format(video_directory, formatted_total_duration))


root_directory = 'F:\Courses\Java\Design Patterns in Java - Concepts & Hands On Projects'  # Replace with the actual root directory
# Loop through all subdirectories in the root directory
for root, dirs, files in os.walk(root_directory):
    for directory in dirs:
        subdirectory_path = os.path.join(root, directory)
        
        # Call the function to process the subdirectory
        process_video_directory(subdirectory_path)


# generetae video_length_txt