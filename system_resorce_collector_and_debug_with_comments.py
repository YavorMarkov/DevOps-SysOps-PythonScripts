import os  # Built-in Python module to interact with the operating system.

# Attempting to import the 'psutil' module. This module provides an API to monitor system resources.
try:
    import psutil
except ImportError as e:  # Exception handling for ImportError, which is raised when the import fails.
    print(f"Import Error: {e}")  # Printing the error message.
    raise SystemExit(1)  # Terminating the script due to the import error.

def get_system_resources():
    resource_dict = {}  # Initializing a dictionary to store system resource usage information.

    # CPU usage
    try:
        resource_dict["CPU_usage"] = psutil.cpu_percent(interval=1)  # Getting CPU usage percentage.
    except Exception as e:  # Exception handling for any error that occurs while getting CPU usage.
        print(f"CPU usage error: {e}")  # Printing the error message.
        raise SystemExit(1)  # Terminating the script due to the error.

    # Memory usage
    try:
        mem_info = psutil.virtual_memory()  # Getting virtual memory usage details.
        resource_dict["Memory_usage"] = mem_info.percent  # Getting memory usage percentage.
    except Exception as e:  # Exception handling for any error that occurs while getting memory usage.
        print(f"Memory usage error: {e}")  # Printing the error message.
        raise SystemExit(1)  # Terminating the script due to the error.

    # Disk usage
    try:
        disk_info = psutil.disk_usage('/')  # Getting disk usage details.
        resource_dict["Disk_usage"] = disk_info.percent  # Getting disk usage percentage.
    except Exception as e:  # Exception handling for any error that occurs while getting disk usage.
        print(f"Disk usage error: {e}")  # Printing the error message.
        raise SystemExit(1)  # Terminating the script due to the error.

    return resource_dict  # Returning the dictionary containing system resource usage information.

# Checking if the script is being run directly (not being imported as a module).
if __name__ == "__main__":
    resources = get_system_resources()  # Getting system resources usage information.
    for key, value in resources.items():  # Iterating over the items in the resources dictionary.
        print(f"{key}: {value}%")  # Printing the resource usage information.
