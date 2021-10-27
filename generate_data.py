import os

result_config_folder = "oltpbench/config/capstone/haonan_tpcc_restart_experiment/"

os.system("PGPASSWORD=tpcc dropdb -U tpcc -h 192.168.1.149 tpcc")
os.system("PGPASSWORD=tpcc createdb -U tpcc -O tpcc -h 192.168.1.149 tpcc")
os.system("PGPASSWORD=tpcc psql -U tpcc -f tpcc.sql -h 192.168.1.149 tpcc")

for i in range(0, 250):
    print(f"oltpbenchmark experiment {i}\n")
    os.system(f"./oltpbenchmark -b tpcc -c config/capstone/haonan_tpcc_restart_experiment_2_500_datapoints/{i}.xml --execute=true -s 5 -o tpcc_gather_all_data_restart_exp_2_500_{i}")
    os.system("sshpass -p ChangeMe2021 ssh -t haonan@192.168.1.149 \"cd /home/haonan/ottertune/client/controller ; /opt/gradle/gradle-5.1/bin/gradle run\"")
    os.system(f"sshpass -p ChangeMe2021 scp -r haonan@192.168.1.149:/home/haonan/ottertune/client/controller/output ../metric_output/tpcc_gather_all_data_restart_exp_2_500_{i}_before")
    os.system("PGPASSWORD=tpcc dropdb -U tpcc -h 192.168.1.149 tpcc")
    os.system("PGPASSWORD=tpcc createdb -U tpcc -O tpcc -h 192.168.1.149 tpcc")
    os.system("PGPASSWORD=tpcc psql -U tpcc -f tpcc.sql -h 192.168.1.149 tpcc")
    os.system("sshpass -p ChangeMe2021 ssh -t haonan@192.168.1.149 \"cd /home/haonan/ottertune/client/controller ; /opt/gradle/gradle-5.1/bin/gradle run\"")
    os.system(f"sshpass -p ChangeMe2021 scp -r haonan@192.168.1.149:/home/haonan/ottertune/client/controller/output ../metric_output/tpcc_gather_all_data_restart_exp_2_500_{i}_after")