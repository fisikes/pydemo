# import numpy as np
from typing import List

import pandas as pd

# 读取dat
f = open("age_met/all_stat_z_log.dat")
lines = f.readlines()
index = 1

# dat数据
dat_list = []

for line in lines:
    if index > 2:  # 跳过第一二行
        l: List[str] = line.split()
        dat_list.append(l)
    index = index + 1
f.close()

dat_df = pd.DataFrame(dat_list, columns=['plate', 'mjd', 'fiberid', 'd4', 'e5', 'f6', 'g7', 'h8', 'i9', 'j10'])
# print(dat_df)

# 读取csv
df_csv = pd.read_csv('age_met/spec.csv')

# for dat in dat_list:
#     match_num = df_csv[df_csv.plate == dat[0] & df_csv.mjd == dat[1] & df_csv.fiberid == dat[2]]
#     print(match_num)

result = df_csv.join(dat_df, on=['plate', 'mjd', 'fiberid'], how='inner')
