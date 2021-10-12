import os

result_config_folder = "oltpbench/config/capstone/haonan_tpcc_restart_experiment/"

for i in range(0, 250):
    print(f"oltpbenchmark experiment {i}\n")
    os.system(f"./oltpbenchmark -b tpcc -c config/capstone/haonan_tpcc_restart_experiment_2_500_datapoints/{i}.xml --execute=true -s 5 -o tpcc_restart_exp_2_500_{i}")
    os.system("PGPASSWORD=tpcc dropdb -U tpcc -h 192.168.1.149 tpcc")
    os.system("PGPASSWORD=tpcc createdb -U tpcc -O tpcc -h 192.168.1.149 tpcc")
    os.system("PGPASSWORD=tpcc psql -U tpcc -f tpcc.sql -h 192.168.1.149 tpcc")