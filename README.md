# System Resource Monitor Script

This script is designed to monitor system resource usage and retrieve information such as CPU usage, memory usage, and disk usage on a Linux system.

## Prerequisites

Before using this script, ensure that you have the following:

- Python 3.x installed on your system.
- The `psutil` module installed. You can install it using `pip install psutil`.

## Usage

1. Clone the repository or download the `system_resource_monitor.py` script to your local machine.

2. Open a terminal and navigate to the directory where the script is located.

3. Run the script using the following command:

   ```shell
   python system_resource_monitor.py

# System Resource Monitor Script

This script is designed to monitor system resource usage and retrieve information such as CPU usage, memory usage, and disk usage on a Linux system.

## Usage

The script will retrieve the system resource information and display it in the following format:

```
CPU_usage: <value>%
Memory_usage: <value>%
Disk_usage: <value>%
```

Replace `<value>` with the actual usage percentage for each resource.

## Error Handling

If any errors occur during the retrieval of resource information, the script will display an error message and exit with a non-zero status.

# Detailed Analysis of the Python System Resources Monitor Script

This script is written in Python, a high-level interpreted programming language known for its readability and ease of use. This script's purpose is to monitor various system resources, including CPU usage, memory usage, and disk usage. It utilizes the `psutil` (process and system utilities) library to access and retrieve this information.

## Part 1: Importing Modules

```python
import os

try:
    import psutil
except ImportError as e:
    print(f"Import Error: {e}")
    raise SystemExit(1)
```
This part of the script imports the necessary Python modules:

- **os**: This is a built-in Python module that interacts with the operating system (OS). The OS module provides a way to use system-dependent functionality such as reading or writing to the environment, manipulating paths, managing files, and more.

- **psutil**: This is a third-party Python library that allows you to retrieve information on running processes and system utilization, such as CPU, memory, disks, network, and sensors. The library is an abstraction layer over platform-specific or lower-level OS APIs and is thus compatible across different operating systems.

The `try`/`except` block is used to handle situations where the psutil library may not be installed in the system's Python environment. If this library isn't found (which raises an `ImportError`), the script prints the error message and then terminates itself by raising a `SystemExit` exception with a status code of 1, indicating an error or abnormal program termination.

## Part 2: The get_system_resources() Function

```python
def get_system_resources():
    resource_dict = {}

    try:
        resource_dict["CPU_usage"] = psutil.cpu_percent(interval=1)
    except Exception as e:
        print(f"CPU usage error: {e}")
        raise SystemExit(1)

    try:
        mem_info = psutil.virtual_memory()
        resource_dict["Memory_usage"] = mem_info.percent
    except Exception as e:
        print(f"Memory usage error: {e}")
        raise SystemExit(1)

    try:
        disk_info = psutil.disk_usage('/')
        resource_dict["Disk_usage"] = disk_info.percent
    except Exception as e:
        print(f"Disk usage error: {e}")
        raise SystemExit(1)

    return resource_dict
```
The `get_system_resources()` function collects data about system resource usage and returns this data as a dictionary. It specifically collects data about:

- **CPU Usage**: `psutil.cpu_percent(interval=1)` is used to measure the CPU usage. This function returns a floating point number representing the current system-wide CPU utilization as a percentage. By specifying `interval=1`, we ask the function to calculate the CPU usage over the past one second. This is a blocking call for the duration of the interval.

- **Memory Usage**: `psutil.virtual_memory()` is used to get memory usage details. This function returns an object with various properties, including total memory, available memory, used memory, and memory percentage used, amongst others. Here, we're specifically interested in `percent`, which represents the memory usage percentage.

- **Disk Usage**: `psutil.disk_usage('/')` is used to get disk usage. This function takes a path as an argument and returns an object with total, used, and free space, along with the percentage of used disk space. The root path ('/') is used here to represent the entire disk.

Each of these sections is wrapped in a `try`/`except` block to handle any exceptions that might be thrown while attempting to retrieve these details. If any operation fails, the script prints an error message specific to that operation and exits with a status code of 1.

## Part 3: Main Execution

```python
if __name__ == "__main__":
    resources = get_system_resources()
    for key, value in resources.items():
        print(f"{key}: {value}%")
```

This part of the script is the main execution block. The `if __name__ == "__main__":` check is a common Python idiom. In Python, `__name__` is a built-in variable which evaluates to the name of the current module. When the script is run as a standalone file, `__name__` equals `"__main__"`. This check makes sure the following code block is executed only when the script is run directly, and not when it's imported as a module in another script.

In this block, the script calls `get_system_resources()`, which returns a dictionary of system resources usage. This dictionary is iterated over, and each key-value pair (representing a resource and its usage) is printed to the standard output. The output would provide a user-readable report on the current usage of CPU, memory, and disk resources.

In summary, this script is a simple yet powerful system resource monitor that leverages the psutil library's capabilities to monitor CPU, memory, and disk usage. It's written to be robust, handling situations where psutil may not be installed, and handling any exceptions that might be thrown while trying to gather system resource usage data.



## Contributing

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue on the GitHub repository.

## License

This script is licensed under the MIT License.

## Disclaimer

Please note that this script is provided as-is and without any warranty. Use it at your own risk.


