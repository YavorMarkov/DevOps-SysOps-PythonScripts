def get_system_resources():
    resource_dict = {}

    # CPU usage
    resource_dict["CPU_usage"] = psutil.cpu_percent(interval=1)

    # Memory usage
    mem_info = psutil.virtual_memory()
    resource_dict["Memory_usage"] = mem_info.percent

    # Disk usage
    disk_info = psutil.disk_usage('/')
    resource_dict["Disk_usage"] = disk_info.percent

    return resource_dict

if __name__ == "__main__":
    resources = get_system_resources()
    for key, value in resources.items():
        print(f"{key}: {value}%")