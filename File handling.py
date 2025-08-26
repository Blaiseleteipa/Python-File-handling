def main():
    try:
        input_file = input("Enter the filename to read: ")
        with open(input_file, "r") as file:
            content = file.read()
        modified_content = content.upper()
        output_file = "modified_" + input_file
        with open(output_file, "w") as file:
            file.write(modified_content)
        print(f"File successfully modified and saved as '{output_file}'.")
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
# This code snippet demonstrates basic list operations in Python.