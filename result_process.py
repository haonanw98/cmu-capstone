import numpy as np

log_file = "oltpbench/results/outputfile.18.res"

dic = {
        "time" : 0,
        "throughput": 1,
        "p99_latency": 9
        }

start = 15
end = 32
loop_num = 36 # 3min


if __name__ == "__main__":
    thp = []
    total_throughput = 0
    skip = False
    with open(log_file, "r") as f:
        i = 0 # curr pos in the 18 rows loop
        for line in f.read().splitlines():
            if not skip:
                skip = True
                continue
            raw_result = line.split(",")
            throughput = float(raw_result[dic["throughput"]])
            if i >= start and i <= end:
                total_throughput += throughput
            if i == loop_num - 1:
                thp.append(total_throughput / (end - start + 1))
                i = 0
                total_throughput = 0

            i += 1
    np.save("exp25_thp_4.npy", np.array(thp))

'''
result_folder = "oltpbench/results/tpcc_restart_exp_1_{}.res"
distribution_file = "distribution/tpcc/tpcc_distribution.txt"
if __name__ == "__main__":
    thp = []
    for i in range(0, 25):
        result_file = f"oltpbench/results/tpcc_restart_exp2_{i}.res"
        total_throughput = 0
        skip = False
        with open(result_file, "r") as f:
            i = 0 # curr pos in the 18 rows loop
            for line in f.read().splitlines():
                if not skip:
                    skip = True
                    continue
                raw_result = line.split(",")
                throughput = float(raw_result[dic["p99_latency"]])
                if i >= start and i <= end:
                    total_throughput += throughput
                if i == loop_num - 1:
                    thp.append(total_throughput / (end - start + 1))
                    i = 0
                    total_throughput = 0

                i += 1
    print(thp)
    np.save("exp_2_p99.npy", np.array(thp))     
'''


