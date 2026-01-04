import subprocess
import os

def terminate_process(process_name):

    " Terminate all processes with the given name."

    cmd = f"taskkill /F /IM {process_name}" if os.name == "nt" else f"pkill -f {process_name}"

    process = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 

    if process.returncode == 0:
        print(f"Successfully terminated all processes named '{process_name}'.")
    
    else:
        print(f"Failed to terminate processes named {process_name}")

def main():

    " Main function for terminating the Sims 3 Launcher process if running."


    process_name = "Sims3LauncherW.exe" # You can change this to any process name, but for my needs it's the Sims 3 Launcher.
    terminate_process(process_name)

main()