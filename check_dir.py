import os

# Define the file path
directory_path = "krushna"

# Check if the directory exists or not
if os.path.exists(directory_path):
    print(f"The file '{directory_path}' exists.")
else:
    print(f"The file '{directory_path}' does not exist.")
