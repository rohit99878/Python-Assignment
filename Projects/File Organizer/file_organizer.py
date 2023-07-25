import os
import shutil

def organize_files(source_directory, destination_directory):
    if not os.path.exists(source_directory):
        print(f"Source directory '{source_directory}' does not exist.")
        return

    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    file_count = 0
    for filename in os.listdir(source_directory):
        file_path = os.path.join(source_directory, filename)

        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1][1:]  # Extract the file extension
            if file_extension:
                destination_folder = os.path.join(destination_directory, file_extension.upper())
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                shutil.move(file_path, os.path.join(destination_folder, filename))
                file_count += 1

    print(f"{file_count} files organized successfully!")

def file_organizer():
    print("File Organizer")
    source_directory = input("Enter the source directory path: ")
    destination_directory = input("Enter the destination directory path: ")
    organize_files(source_directory, destination_directory)

if __name__ == "__main__":
    file_organizer()
