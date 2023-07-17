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

## Contributing

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue on the GitHub repository.

## License

This script is licensed under the MIT License.

## Disclaimer

Please note that this script is provided as-is and without any warranty. Use it at your own risk.
