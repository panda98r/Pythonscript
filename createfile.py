# Python script to create a hari.txt file in /home/ubuntu/ place 

file_path = "/home/ubuntu/hari.txt"

# Open the file in write mode ('w') and create it if doesn't exist
with open(file_path, 'w') as file:
    # put some text
    file.write("My first file created in /home/ubuntu/\n")

print(f"File created successfully at {file_path}")

