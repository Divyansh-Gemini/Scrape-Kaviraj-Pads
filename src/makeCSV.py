import os
import csv

def write_filenames_to_csv(directory_path, output_csv):
    try:
        # Ensure the directory exists
        if not os.path.isdir(directory_path):
            print(f"Error: The directory '{directory_path}' does not exist.")
            return
        
        # Get a list of files in the directory
        file_names = os.listdir(directory_path)
        
        # Open the CSV file for writing
        with open(output_csv, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            # Write each file name to a new row
            for file_name in file_names:
                if os.path.isfile(os.path.join(directory_path, file_name)):  # Ensure it's a file
                    writer.writerow([file_name[:-4]])  # Remove the file extension
        
        print(f"File names have been written to '{output_csv}' successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace with your directory path and desired output CSV file name
directory_path = "new_songs"
output_csv = "pad.csv"

write_filenames_to_csv(directory_path, output_csv)
