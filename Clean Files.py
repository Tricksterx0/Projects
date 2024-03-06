import os
import shutil
import errno

def clean_recycling_bin():
    try:
        # Get the path to the Recycling Bin
        recycling_bin = os.path.expanduser("~") + "\\Recycle Bin"
        
        # List all files in the Recycling Bin
        files = os.listdir(recycling_bin)
        
        # Delete each file in the Recycling Bin
        for file in files:
            file_path = os.path.join(recycling_bin, file)
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except OSError as e:
                if e.errno == errno.EACCES:
                    print(f"Could not delete {file_path}. File is in use.")
                else:
                    print(f"Error deleting {file_path}: {e}")
            
        print("Recycling Bin cleaned successfully!")
    except Exception as e:
        print(f"Error cleaning Recycling Bin: {e}")

def clean_windows_temp_prefetch():
    try:
        # Get the path to the Temp folder
        temp_folder = os.environ.get('TEMP', 'C:\\Windows\\Temp')
        
        # Get the path to the Prefetch folder
        prefetch_folder = 'C:\\Windows\\Prefetch'
        
        # List all files in the Temp folder
        temp_files = os.listdir(temp_folder)
        
        # List all files in the Prefetch folder
        prefetch_files = os.listdir(prefetch_folder)
        
        # Delete each file in the Temp folder
        for file in temp_files:
            file_path = os.path.join(temp_folder, file)
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except OSError as e:
                if e.errno == errno.EACCES:
                    print(f"Could not delete {file_path}. File is in use.")
                else:
                    print(f"Error deleting {file_path}: {e}")
            
        # Delete each file in the Prefetch folder
        for file in prefetch_files:
            file_path = os.path.join(prefetch_folder, file)
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except OSError as e:
                if e.errno == errno.EACCES:
                    print(f"Could not delete {file_path}. File is in use.")
                else:
                    print(f"Error deleting {file_path}: {e}")
            
        print("Windows Temp and Prefetch folders cleaned successfully!")
    except Exception as e:
        print(f"Error cleaning Windows Temp and Prefetch folders: {e}")

if __name__ == "__main__":
    clean_recycling_bin()
    clean_windows_temp_prefetch()
