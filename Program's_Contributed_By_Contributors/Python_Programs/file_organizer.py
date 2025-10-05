# File Organizer - Hacktoberfest 2025 contribution
# Organizes files in a folder into subfolders by file type

import os
import shutil

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist!")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            ext = filename.split('.')[-1].lower()
            if not ext:
                ext = 'no_extension'
            target_folder = os.path.join(folder_path, ext)
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, filename))
    print(f"Files organized in '{folder_path}' by type.")

if __name__ == "__main__":
    folder = input("Enter the folder path to organize: ")
    organize_folder(folder)
