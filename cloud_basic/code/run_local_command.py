import subprocess

def run_local_command(command):
    try:
        # Run the command and capture output
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # Return stdout and stderr as strings, strip any trailing whitespace
        return result.stdout.strip(), result.stderr.strip()

    except subprocess.CalledProcessError as e:
        # When command fails (like grep with no matches), return 0 and the error
        return "0", e.stderr.strip()


