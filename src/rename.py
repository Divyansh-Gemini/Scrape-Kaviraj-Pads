import os
import re

def clean_filename(filename):
    """Remove numbers and special characters from a filename."""
    return re.sub(r'[^a-zA-Z\s\.]', '', filename).strip()

def rename_files_in_directory(directory_path):
    """Rename files in the given directory by modifying only the filename (not the extension)."""
    if not os.path.exists(directory_path):
        print(f"Error: Directory '{directory_path}' does not exist.")
        return

    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' is not a directory.")
        return

    for filename in os.listdir(directory_path):
        old_path = os.path.join(directory_path, filename)

        if os.path.isfile(old_path):  # Process only files
            # Split the filename into name and extension
            name, ext = os.path.splitext(filename)
            # Clean only the filename part
            cleaned_name = clean_filename(name)
            # Recombine the cleaned name with the original extension
            new_name = f"{cleaned_name}{ext}"
            new_path = os.path.join(directory_path, new_name)

            # Rename file if the name has changed
            if old_path != new_path:
                os.rename(old_path, new_path)
                print(f"Renamed: '{filename}' -> '{new_name}'")

if __name__ == "__main__":
    rename_files_in_directory("songs")
