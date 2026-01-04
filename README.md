# Terminate Windows Process by Name

This Python script terminates a running Windows process by name using `subprocess` and the `taskkill` command.

When run, the specified process is immediately terminated. If the process is not running, an error message is displayed.

The script is currently configured to terminate the **Sims 3 Launcher**, which I used as a simple automation example. The process name can be changed to target any other Windows process.

**Note:** Some processes may require administrator privileges. 
