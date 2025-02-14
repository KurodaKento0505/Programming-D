import os
import subprocess
import csv
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory', required=True, help="Path to the directory containing folders with .exe files.")
    parser.add_argument('--exe_file_name', required=True, help="Name of the executable file to search for and execute.")
    parser.add_argument('--input_file', required=False, help="Name of the input file to pass to the executable.")
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
    output_csv = os.path.join(parent_directory, f"execution_results_{os.path.split(directory)[1]}.csv")

    if os.path.isdir(directory):
        execute_exe_files(directory, output_csv, exe_file_name, input_file, debug_args)
    else:
        print("The provided path is not a valid directory.")


def execute_exe_files(directory, output_csv, exe_file_name, input_file, debug_args):
    results = {}

    # Read input values from the input file
    input_values = ""
    if input_file and os.path.exists(input_file):
        with open(input_file, 'r', encoding='utf-8') as file:
            input_values = file.read()

    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)

        if os.path.isdir(folder_path):
            exe_file_path = os.path.join(folder_path, exe_file_name)
            if os.path.exists(exe_file_path):
                try:
                    result = subprocess.run(
                        [exe_file_path, *debug_args],
                        # text=True,
                        universal_newlines=True,
                        input=input_values,
                        capture_output=True,
                        check=True,
                        encoding="utf-8",
                        errors="ignore"
                    )
                    results[folder_name] = result.stdout.strip()
                except subprocess.CalledProcessError as e:
                    results[folder_name] = f"Error during execution: {e.stderr.strip()}"
            else:
                results[folder_name] = f"Error: {exe_file_name} not found"

    # Update or create CSV
    update_or_create_csv(output_csv, results)


def update_or_create_csv(output_csv, results):
    # Load existing data if the CSV file exists
    existing_data = {}
    if os.path.exists(output_csv):
        with open(output_csv, mode="r", encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file)
            headers = next(csv_reader, [])
            for row in csv_reader:
                if len(row) > 1:
                    existing_data[row[0]] = row[1:]

    # Merge results into existing data
    for folder, output in results.items():
        if folder in existing_data:
            existing_data[folder].append(output)
        else:
            existing_data[folder] = [output]

    # Write back to the CSV
    headers = ["Directory"] + [f"Run {i + 1}" for i in range(len(max(existing_data.values(), key=len, default=[])))]
    with open(output_csv, mode="w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(headers)
        for folder, outputs in sorted(existing_data.items()):
            csv_writer.writerow([folder] + outputs)


if __name__ == "__main__":
    main()
