import os

try:
    import psutil
except ImportError as e:
    print(f"Import Error: {e}")
    raise SystemExit(1)

def get_system_resources():
    resource_dict = {}

    # CPU usage
    try:
        resource_dict["CPU_usage"] = psutil.cpu_percent(interval=1)
    except Exception as e:
        print(f"CPU usage error: {e}")
        raise SystemExit(1)

    # Memory usage
    try:
        mem_info = psutil.virtual_memory()
        resource_dict["Memory_usage"] = mem_info.percent
    except Exception as e:
        print(f"Memory usage error: {e}")
        raise SystemExit(1)

    # Disk usage
    try:
        disk_info = psutil.disk_usage('/')
        resource_dict["Disk_usage"] = disk_info.percent
    except Exception as e:
        print(f"Disk usage error: {e}")
        raise SystemExit(1)

    return resource_dict

if __name__ == "__main__":
    resources = get_system_resources()
    for key, value in resources.items():
        print(f"{key}: {value}%")
