import psutil
import time

if __name__ == "__main__":
    i = 0
    f = open("log1.txt", "w")
    while i < 360 * 6:
        cpu_usage = psutil.cpu_percent()
        mem_usage = psutil.virtual_memory()
        print(cpu_usage, mem_usage)
        f.write(str(cpu_usage) + " " + str(mem_usage) + "\n")
        i += 1
        time.sleep(10)
    f.close()
