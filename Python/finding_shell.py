import os
import fnmatch

def find_files_with_strings(root_dir, search_strings):
    matches = []
    for root, dirnames, filenames in os.walk(root_dir):
        for filename in fnmatch.filter(filenames, '*'):
            file_path = os.path.join(root, filename)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                for line in file:
                    if any(search_string in line for search_string in search_strings):
                        matches.append(file_path)
                        break  # If any string is found in the current file, no need to continue checking this file

    return matches

# Replace 'your_directory' with the directory you want to search in
directory_to_search = 'your_directory'
search_strings = ['system', 'shell_exec', 'eval']

found_files = find_files_with_strings(directory_to_search, search_strings)

if found_files:
    print("Found the following files containing the search strings:")
    for file in found_files:
        print(file)
else:
    print(f"The search strings {', '.join(search_strings)} were not found in any files within the directory '{directory_to_search}'.")
