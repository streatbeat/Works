import psutil

print("physical cores: ", psutil.cpu_count(logical=False))
print("Total cores: ", psutil.cpu_count(logical=True))

cpufreq = psutil.cpu_freq()
print(f"Max Frequency: {cpufreq.max:.0f}MHz")
print(f"Mix Frequency: {cpufreq.min:.0f}MHz")
print(f"Current Frequency: {cpufreq.current:.2f}MHz")

print("CPU Usage per Core: ")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Core {i}: {percentage}%")
print(f"total CPU Usage: {psutil.cpu_percent()}%")