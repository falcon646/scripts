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

# Example usage
output_video_path = 'output_demuxer.mp4'  # Replace with the path to your output video




has_issues = check_output_video(output_video_path)

if has_issues:
    print("Issues detected in the output video.")
else:
    print("No issues detected in the output video.")
