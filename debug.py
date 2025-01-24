import os
import subprocess
import csv
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory', required=True, help="Path to the directory containing folders with .exe files.")
    parser.add_argument('--exe_file_name', required=True, help="Name of the executable file to search for and execute.")
    parser.add_argument('--input_file', required=True, help="Name of the executable file to search for and execute.")
    parser.add_argument('--debug_args', required=False, help="Optional arguments to pass to the executable file, separated by spaces.")
    return parser.parse_args()


def main():
    args = parse_arguments()
    directory = args.directory
    exe_file_name = args.exe_file_name
    input_file = args.input_file
    debug_args = args.debug_args.split() if args.debug_args else []

    # Set output file path to one level above the given directory
    parent_directory = os.path.dirname(os.path.abspath(directory))
    output_csv = os.path.join(parent_directory, "execution_results.csv")

    if os.path.isdir(directory):
        execute_exe_files(directory, output_csv, exe_file_name, input_file, debug_args)
    else:
        print("The provided path is not a valid directory.")


def execute_exe_files(directory, output_csv, exe_file_name, input_file, debug_args):
    results = []

    # Read input values from the input file
    with open(input_file, 'r', encoding='utf-8') as file:
        input_values = file.read()

    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)

        if os.path.isdir(folder_path):
            exe_file_path = os.path.join(folder_path, exe_file_name)
            if os.path.exists(exe_file_path):
                try:
                    # Pass input_values as standard input to the executable
                    result = subprocess.run(
                        [exe_file_path, *debug_args],
                        text=True,
                        input=input_values,
                        capture_output=True,
                        check=True
                    )
                    results.append((folder_name, result.stdout.strip()))
                except subprocess.CalledProcessError as e:
                    results.append((folder_name, f"Error during execution: {e.stderr.strip()}"))
            else:
                results.append((folder_name, f"Error: {exe_file_name} not found"))

    # Write results to CSV
    with open(output_csv, mode="w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Directory", "Execution Output"])
        csv_writer.writerows(results)



if __name__ == "__main__":
    main()