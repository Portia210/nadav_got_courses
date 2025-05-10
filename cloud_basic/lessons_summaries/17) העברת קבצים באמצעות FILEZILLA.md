### Transferring Files Using FILEZILLA

To transfer files using FILEZILLA, follow these steps:

1. Open the software.
2. Navigate to `File > Sites Manager`.
3. Choose `SSH`.
4. Enter with a key file, select a `.pem` file.
5. Once the connection is established, you can simply drag and drop files.

#### Linux Commands Expansion:

In the context of transferring files using FILEZILLA, there are no specific Linux commands mentioned. However, if you are looking to transfer files via SSH on a Linux system, you can use the `scp` command.

**SCP Command:**

- **Description:** `scp` stands for secure copy. It is a command-line tool used to copy files securely between hosts on a network.
- **Usage:** `scp [options] [source] [destination]`
- **Options:**
  - `-r`: Recursively copy entire directories.
  - `-P port`: Specify the port to connect to on the remote host.
  - `-i identity_file`: Selects the file from which the identity (private key) for public key authentication is read.

By using the `scp` command, you can securely transfer files between Linux systems over an SSH connection.