import psutil
def closeall():# wherever this function is called it will close all running processes except jarvis
    process_to_keep = "C:\\Users\\Admin\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk" 
    #change the above path to the path of application where the code will be running

    running_processes = list(psutil.process_iter())
   
    for process in running_processes:
        try:
            if process.name().lower() == process_to_keep.lower():
                continue  
            process.terminate()
        except Exception as e:
            print(f"Error terminating process {process.pid}: {e}")
