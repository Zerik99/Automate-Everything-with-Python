import psutil

# CPU usage
print(psutil.cpu_percent())
print(psutil.cpu_count(logical=False))
print(psutil.cpu_count(logical=True))

# Memory usage
print(psutil.virtual_memory())

# Disk usage
print(psutil.disk_usage("/"))
