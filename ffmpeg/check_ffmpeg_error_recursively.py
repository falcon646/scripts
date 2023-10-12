import os
import subprocess

def check_output_video(video_path):
    try:
        # Run FFmpeg to probe the output video
        command = ['ffmpeg', '-v', 'error', '-i', video_path, '-f', 'null', '-']
        process = subprocess.Popen(command, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        # Check FFmpeg's output for issues
        if b'error' in stderr or b'warning' in stderr:
            return True  # Issues detected
        else:
            return False  # No issues
    except Exception as e:
        print(f"Error checking video: {e}")
        return True  # Assume there are issues if an error occurs

def check_specific_videos_in_subdirectories(root_directory, video_name_pattern):
    for root, dirs, files in os.walk(root_directory):
        for directory in dirs:
            subdirectory_path = os.path.join(root, directory)
            output_video_path = os.path.join(subdirectory_path, video_name_pattern)

            if os.path.isfile(output_video_path):
                has_issues = check_output_video(output_video_path)

                if has_issues:
                    print(f"Issues detected in the video: {output_video_path}")
                else:
                    print(f"No issues detected in the video: {output_video_path}")

# Root directory where you want to check the specific output videos
root_directory = 'F:\Courses\Java\Design Patterns in Java - Concepts & Hands On Projects'  # Replace with the actual root directory
# Specific video name pattern (e.g., 'output.mp4')
video_name_pattern = 'output_demuxer.mp4'  # Replace with your video name pattern

# Call the function to check specific output videos in subdirectories
check_specific_videos_in_subdirectories(root_directory, video_name_pattern)
