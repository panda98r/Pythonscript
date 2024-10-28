# Script to copy contents from one file to another
def copy_file_contents(source_file, destination_file):
    try:
        # Open source file in read mode and the destination file in write mode
        with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
            # Read the from the source and write content to the destination
            dest.write(src.read())
        print(f"Contents copied from {source_file} to {destination_file} successfully.")
    except FileNotFoundError:
        print(f"Error: The file '{source_file}' not found.")
    except IOError:
        print("Error: Unable to copy contennt ")

# Replace 'source.txt' and 'destination.txt' with your file names
copy_file_contents('/home/ubuntu/now.py', '/home/ubuntu/1.txt')

