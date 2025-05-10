from SshToServer import SshToServer

bash_script_path = "lesson_31_server.sh"
file_to_search = input("Enter the file to search for: ")
seconds_to_wait = int(input("Enter the seconds to wait: "))

ssh_connection = SshToServer(r"C:\Users\hp\Documents\סיכומים נדב גוטהייט\my_key_pair.pem", "13.220.23.193", "ubuntu")

# Make the script executable
ssh_connection.runRemoteCommand(f"chmod +x {bash_script_path}")
print(f"chmod +x {bash_script_path}")

# Run the script and capture its output
output = ssh_connection.runRemoteCommand(f"./{bash_script_path} {file_to_search} {seconds_to_wait}")
print("Remote script output:")
print(output)






