from run_local_command import run_local_command

def get_log_counts():
    """Get counts of different log levels from syslog"""
    # Get counts for each type of log entry
    info_count, _ = run_local_command("grep -c 'INFO' /var/log/syslog")
    warning_count, _ = run_local_command("grep -c 'WARNING' /var/log/syslog")
    error_count, _ = run_local_command("grep -c 'ERROR' /var/log/syslog")
    
    # Return the counts as a comma-separated string
    return f"{info_count},{warning_count},{error_count}"

# This block only runs if the script is run directly (not imported)
if __name__ == "__main__":
    # When run directly, just output the counts
    print(get_log_counts(), end='')

