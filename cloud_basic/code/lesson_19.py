from SshToServer import SshToServer

ssh_to_server = SshToServer(r"C:\Users\hp\Documents\סיכומים נדב גוטהייט\my_key_pair.pem", "13.220.23.193", "ubuntu") # add r before the path to avoid issues with backslashes

# Get output and error as separate variables
output, error = ssh_to_server.runRemoteCommand("date +%s")

# If there's an error, print it
if error:
    print("Error:", error)

# If there's output, print it
if output:
    print("Command output:")
    print(output)


