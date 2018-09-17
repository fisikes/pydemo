import csv
from typing import List

f = open("stars_met/all_stat_z_log.dat")
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

# 写入结果
with open("stars_met/all_stat_z_log.csv", mode="w", newline='') as csvfile:
    writer = csv.writer(csvfile)

    # 先写入columns_name
    writer.writerow(
        ["_plate", "_mjd", "_fiberid", "dat_4", "dat_5", "dat_6", "dat_7", "dat_8", "dat_9", "dat_10"]
    )
    # 写入多行用writerows
    writer.writerows(data_list)
