import csv
from typing import List
import time

# 读取dat
f = open("all_stat_z_log.dat")
lines = f.readlines()
index = 1

data_list = []

for line in lines:

    if index > 2:  # 跳过第一二行
        l: List[str] = line.split()
        data_list.append(l)

    index = index + 1

f.close()

# 读取csv
csv_file = csv.reader(open("spec.csv"))
rows = [row for row in csv_file]

results = []  # 存放输出内容
for stu in rows:
    for l in data_list:
        if l[0] == stu[3] and l[1] == stu[4] and l[2] == stu[5]:
            result = l + stu
            results.append(result)
            print(result)
            continue

# 写入结果
file_name = time.strftime("%Y%m%d%H%M%S", time.localtime())
with open(str(file_name)+".csv", mode="w", newline='') as csvfile:
    writer = csv.writer(csvfile)

    # 先写入columns_name
    writer.writerow(
        ["specid", "ra,dec", "plate", "mjd", "fiberid", "z", "zErr", "snMedian_r", "d4000_n", "d4000_n_err"] +
        ["dat_1", "dat_2", "dat_3", "dat_4", "dat_5", "dat_6", "dat_7", "dat_8", "dat_9", "dat_10"]
    )
    # 写入多行用writerows
    writer.writerows(results)
