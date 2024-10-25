import os
import file_paths

def read_last_n_lines(file_path, read_lines):
    with open(file_path, 'r') as file:
        lines = file.readlines()

        # Determine the number of lines to read
        num_lines_to_read = min(len(lines), read_lines)

        # Read the last 'num_lines_to_read' lines
        last_lines = lines[-num_lines_to_read:]

        return last_lines

# Example usage:
file_path = os.path.normpath(os.path.join(file_paths.csv_source_path, "test_result.txt"))
read_lines = 5

last_lines = read_last_n_lines(file_path, read_lines)
for line in last_lines:
    print(line.strip())  # Strip newline character from each line
