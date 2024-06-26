import psutil
def closeall():
# Define the process name to keep running
    process_to_keep = "C:\\Users\\Admin\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"

    # Get all running processes
    running_processes = list(psutil.process_iter())

    # Iterate over each process and terminate it, except the one to keep open
    for process in running_processes:
        try:
            if process.name().lower() == process_to_keep.lower():
                continue  # Skip the process to keep open
            process.terminate()
        except Exception as e:
            print(f"Error terminating process {process.pid}: {e}")