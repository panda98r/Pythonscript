import os

# Command to check Apache2 status
apache_status_command = 'systemctl is-active apache2'

# Function to check Apache2 service status
def check_apache_status():
    status = os.popen(apache_status_command).read().strip()
    if status == 'active':
        return "Apache2 is running."
    else:
        return "Apache2 is not running."

# Run the script
if __name__ == "__main__":
    status_message = check_apache_status()
    print(status_message)

