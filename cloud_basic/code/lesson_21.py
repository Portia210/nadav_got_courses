from SshToServer import SshToServer


ssh_to_server = SshToServer(r"C:\Users\hp\Documents\סיכומים נדב גוטהייט\my_key_pair.pem", "13.220.23.193", "ubuntu") # add r before the path to avoid issues with backslashes

output, error = ssh_to_server.runRemoteCommand("python3 server_side.py")

if error:
    print("Error:", error)

if output:
    print("Command output:")
    print(output)





