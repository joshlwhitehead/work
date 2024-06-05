import sys

def apply_equation(old_number, offset, scale):
    return (((old_number - offset) * scale) + offset)

def process_line(line, offset, scale):
    # Check if the line contains the label "TC:" and matches the specified format
    if "TC-1" in line:
        try:
            # Extracting the number after the first equals sign
            number_start = line.index("=") + 1
            number_end = line.index(",", number_start)
            old_number = float(line[number_start:number_end])

            # Applying the equation to get the new number
            new_number = apply_equation(old_number, offset, scale)

            print(f"old_number:{old_number:.2f}  new_number:{new_number:.2f}")

            # Replace the old number with the new number in the line
            new_line = line[:number_start] + f" {new_number:.2f}" + line[number_end:]
            return new_line
        except ValueError:
            pass
    return line

def process_file(input_file, output_file, offset, scale):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    updated_lines = [process_line(line, offset, scale) for line in lines]

    with open(output_file, 'w') as file:
        file.writelines(updated_lines)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py path/to/input_file.txt")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = "./model_adjuster_output.txt"  # Change this if you want a specific output file path
    offset = 51.7
    scale = 1.1

    process_file(input_file_path, output_file_path, offset, scale)
