import os
import subprocess
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory', required=True, help="Path to the directory containing folders with .exe files.")
    parser.add_argument('--exe_file_name', required=True, help="Name of the executable file to search for and execute.")
    return parser.parse_args()


def main():
    args = parse_arguments
    directory = args.directory
    exe_file_name = args.exe_file_name
    if os.path.isdir(directory):
        compile_c_files_in_folders(directory, exe_file_name)
    else:
        print("The provided path is not a valid directory.")


def find_c_files_recursive(directory):
    """
    Recursively searches for C files in the directory and returns their paths.

    Parameters:
        directory (str): The directory to search for C files.

    Returns:
        list: A list of paths to C files.
    """
    c_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".c"):
                c_files.append(os.path.join(root, file))
    return c_files

def compile_c_files_in_folders(directory, exe_file_name):
    """
    Searches for C files in each folder and compiles them into executable files.

    Parameters:
        directory (str): The path to the directory containing folders with C files.
    """
    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)

        # Check if the current path is a folder
        if os.path.isdir(folder_path):
            print(f"Checking folder: {folder_name}")

            # Check if an .exe file already exists in the folder
            exe_file_path = os.path.join(folder_path, exe_file_name)
            if os.path.exists(exe_file_path):
                print(f"Executable file already exists in {folder_name}, skipping.")
                continue

            # Find all .c files recursively in the folder
            c_files = find_c_files_recursive(folder_path)

            if not c_files:
                print(f"No C files found in {folder_name} or its subfolders.")
                continue

            # Compile the first C file found
            for c_file_path in c_files:
                try:
                    print(f"Compiling {c_file_path} to {exe_file_path}...")
                    result = subprocess.run(
                        ["gcc", c_file_path, "-o", exe_file_path],
                        check=True,
                        capture_output=True,
                        text=True
                    )
                    print(f"Compiled successfully: {exe_file_path}")
                    break  # Compile only one .c file per folder
                except subprocess.CalledProcessError as e:
                    print(f"Error compiling {c_file_path}: {e.stderr}")

if __name__ == "__main__":
    main()