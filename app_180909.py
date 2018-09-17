import csv
from typing import List
import time

# 读取dat
f = open("age_met/all_stat_z_log.dat")
lines = f.readlines()
index = 1

# 存放dat数据
data_list = []

for line in lines:

    if index > 2:  # 跳过第一二行
        dat: List[str] = line.split()
        data_list.append(dat)

    index = index + 1

f.close()

# 读取csv
csv_file = csv.reader(open("age_met/spec.csv"))
rows = [row for row in csv_file]

results = []  # 存放输出内容
for stu in rows:
    for dat in data_list:
        if dat[0] == stu[3] and dat[1] == stu[4] and dat[2] == stu[5]:
            result = dat + stu
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
