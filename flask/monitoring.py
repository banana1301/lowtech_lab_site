import os
import psutil
# Getting all memory using os.popen()
total_memory, used_memory, free_memory = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
mem= round((used_memory/total_memory) * 100, 2)
# Memory usage
cpuload = psutil.cpu_percent(interval=1)

print("RAM memory % used:",mem )
print("Total CPU usage:", cpuload, "%")