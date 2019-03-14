import time

import pandas as pd

# todo 读取文件,
# 全量数据对比, 找出增量和更新的量.
start = time.time()
df1 = pd.read_csv('fc-data/finance_summary_new.csv', dtype=str, sep='~', header=None)
print("df1: " + str(df1.shape))

df2 = pd.read_csv('fc-data/finance_summary.csv', dtype=str, sep='~', header=None)
print("df2: " + str(df2.shape))

# 主键相同
df_id_equal = df1.merge(df2, on=0, copy=False)
print("df_id_equal: " + str(df_id_equal.shape))

# 新增数据: 即主键不相同的 (df1假设为新数据)
# other = df1[(~df1.col1.isin(common.col1)) & (~df1.col2.isin(common.col2))]
df_new = df1[(~df1[0].isin(df_id_equal[0]))]
print("df_id_not_equal: " + str(df_new.shape))

# 完全相同的
common = df1.merge(df2, on=list(range(43)))
print("common: " + str(common.shape))

# 待更新数据: 主键相同, 但属性值不同的数据. 因此(df_id_equal - common) 即为需要更新的
# 0        1_x                2_x ...    41_y             42_y 43_y
df_update = df_id_equal[(~df_id_equal[0].isin(common[0]))]
print("df_update" + str(df_update.shape))

# todo 后续可以通过http client将数据发送到指定的接口, 接口将数据存储到mq.
# 输出新增数据
df_new.to_csv(path_or_buf='fc-data/new.csv',
              sep="~",
              header=None,
              index=False)
# 输出需要更新的数据 todo 如何按照下标取到数据.
df_update[0:43].to_csv(path_or_buf='fc-data/update.csv',
                 sep="~",
                 header=None,
                 index=False)

print(df_update[0:43].shape)

end = time.time()
print(end - start)
#
# result.to_csv('stars_met/Result.csv', index=False)
