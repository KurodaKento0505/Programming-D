import os
import zipfile
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory', required=True, help="Path to the directory containing folders with .exe files.")
    return parser.parse_args()


def main():
    args = parse_arguments()
    directory = args.directory
    if os.path.isdir(directory):
        unzip_files_in_folders(directory)
    else:
        print("The provided path is not a valid directory.")


def unzip_files_in_folders(directory):
    """
    Unzips all zip files in each subfolder of the given directory.

    Parameters:
        directory (str): The path to the directory containing subfolders with zip files.
    """
    # Iterate through each folder in the directory
    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)
        
        # Check if the current path is a folder
        if os.path.isdir(folder_path):
            print(f"Checking folder: {folder_name}")

            # Iterate through each file in the folder
            for file_name in os.listdir(folder_path):
                if file_name.endswith(".zip"):
                    zip_path = os.path.join(folder_path, file_name)
                    extract_path = os.path.join(folder_path, file_name[:-4])

                    # Unzip the file
                    try:
                        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                            print(f"Extracting: {zip_path} to {extract_path}")
                            zip_ref.extractall(extract_path)
                    except zipfile.BadZipFile:
                        print(f"Error: {zip_path} is not a valid zip file.")

if __name__ == "__main__":
    main()
