import os

def count_srt_files(folder_path):
    try:
        srt_files = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".vtt"):
                    srt_files.append(file)
        
        srt_count = len(srt_files)
        
        return srt_count
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return 0

def list_srt_files(folder_path):
    try:
        srt_files = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".vtt"):
                    file_path = os.path.join(root, file)
                    srt_files.append(file_path)
        
        return srt_files
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return []

def delete_srt_files(srt_files):
    try:
        for file_path in srt_files:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    folder_path = r'F:\Courses\Kubernetes\Udemy - Kubernetes Hands-On - Deploy Microservices to the AWS Cloud'  # Replace with the path to your folder
    
    # Count .srt files
    srt_count = count_srt_files(folder_path)
    print(f"Number of .srt files found: {srt_count}")
    
    # List .srt files
    srt_files = list_srt_files(folder_path)
    if srt_count > 0:
        print("List of .srt files:")
        for file_path in srt_files:
            print(file_path)
    
    #Delete .srt files
    if srt_count > 0:
        delete_srt_files(srt_files)
        print("Deletion complete.")
    else:
        print("No .srt files found to delete.")


