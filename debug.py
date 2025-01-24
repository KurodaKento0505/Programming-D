import os
import subprocess
import csv
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory', required=True, help="Path to the directory containing folders with .exe files.")
    parser.add_argument('--exe_file_name', required=True, help="Name of the executable file to search for and execute.")
    parser.add_argument('--debug_args', required=False, help="Optional arguments to pass to the executable file, separated by spaces.")
    return parser.parse_args()


def main():
    args = parse_arguments()
    directory = args.directory
    exe_file_name = args.exe_file_name
    debug_args = args.debug_args.split() if args.debug_args else []

    # Set output file path to one level above the given directory
    parent_directory = os.path.dirname(os.path.abspath(directory))
    output_csv = os.path.join(parent_directory, "execution_results.csv")

    if os.path.isdir(directory):
        execute_exe_files(directory, output_csv, exe_file_name, debug_args)
    else:
        print("The provided path is not a valid directory.")


def execute_exe_files(directory, output_csv, exe_file_name, debug_args):
    """
    Searches for and executes all .exe files named in the directory and its subfolders.

    Parameters:
        directory (str): The path to the directory containing folders with .exe files.
        output_csv (str): Path to the CSV file to save execution results.
        exe_file_name (str): The name of the executable file to execute.
        debug_args (list): List of additional arguments to pass to the .exe file during execution.

    Outputs:
        A CSV file containing the directory name and the output of each execution.
    """
    with open(output_csv, mode="w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Directory", "Execution Output"])

        for folder_name in os.listdir(directory):
            folder_path = os.path.join(directory, folder_name)

            # Check if the current path is a folder
            if os.path.isdir(folder_path):
                exe_file_path = os.path.join(folder_path, exe_file_name)
                if os.path.exists(exe_file_path):
                    try:
                        result = subprocess.run(
                            [exe_file_path, *debug_args],
                            check=True,
                            capture_output=True,
                            text=True
                        )

                        # Write to CSV
                        csv_writer.writerow([folder_name, result.stdout.strip()])
                    except subprocess.CalledProcessError as e:
                        print(f"Error executing {exe_file_path}: {e.stderr}")
                        csv_writer.writerow([folder_name, f"Error: {e.stderr.strip()}"])


if __name__ == "__main__":
    main()