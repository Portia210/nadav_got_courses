from SshToServer import SshToServer
import pandas as pd

def get_remote_log_counts(ssh):
    """Get log counts from remote server and return as integers"""
    output, error = ssh.runRemoteCommand("python3 server_side_22.py")
    
    if error:
        print("Error from remote server:", error)
        return None
        
    # Parse the comma-separated values into integers
    try:
        info, warning, error = map(int, output.split(','))
        return info, warning, error
    except ValueError as e:
        print(f"Error parsing output: {output}")
        print(f"Error details: {e}")
        return None

def main():
    ssh = SshToServer(r"C:\Users\hp\Documents\סיכומים נדב גוטהייט\my_key_pair.pem", "13.220.23.193", "ubuntu")
    # Get the counts
    result = get_remote_log_counts(ssh)
    
    if result:
        info_count, warning_count, error_count = result
        
        # Create DataFrame
        df = pd.DataFrame({
            'Log Level': ['Info', 'Warning', 'Error'],
            'Count': [info_count, warning_count, error_count]
        })
        
        # Set Log Level as index and display
        df.set_index('Log Level', inplace=True)
        print("\nLog Counts:")
        print(df)

if __name__ == "__main__":
    main()

