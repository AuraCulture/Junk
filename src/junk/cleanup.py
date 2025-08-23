import os
import shutil
from typing import List, Tuple


def clean_up() -> bool:
    """
    Clean up files and folders listed in junk.fat.
    
    Returns:
        bool: True if all deletions were successful, False otherwise
    """
    junk_file = 'junk.fat'
    

    if not os.path.exists(junk_file):
        print("No junk.fat file found in the current directory.")
        return False
    
    try:

        encodings_to_try = ['utf-8', 'utf-8-sig', 'utf-16', 'cp1252']
        files_to_delete = None
        
        for encoding in encodings_to_try:
            try:
                with open(junk_file, 'r', encoding=encoding) as file:
                    files_to_delete = [line.strip() for line in file.readlines() if line.strip()]
                break
            except UnicodeDecodeError:
                continue
        
        if files_to_delete is None:
            print("Error: Could not read junk.fat file. Please check the file encoding.")
            return False
        
        if not files_to_delete:
            print("junk.fat is empty.")
            os.remove(junk_file)
            return True
        
        failed_deletions = []
        successful_deletions = []
        
        for item in files_to_delete:
            try:
                if os.path.exists(item):
                    if os.path.isfile(item):
                        os.remove(item)
                        successful_deletions.append(f"Deleted file: {item}")
                    elif os.path.isdir(item):
                        shutil.rmtree(item)
                        successful_deletions.append(f"Deleted directory: {item}")
                    else:
                        failed_deletions.append(f"Unknown item type: {item}")
                else:
                    print(f"Item not found (skipping): {item}")
            except Exception as e:
                failed_deletions.append(f"Failed to delete {item}: {e}")
        

        for success in successful_deletions:
            print(success)
        
        for failure in failed_deletions:
            print(f"WARNING: {failure}")
        

        if not failed_deletions:
            os.remove(junk_file)
            print("All items deleted successfully. Removed junk.fat.")
            return True
        else:
            print(f"Some deletions failed. Keeping junk.fat for retry.")
            return False
            
    except Exception as e:
        print(f"An error occurred during cleanup: {e}")
        return False
