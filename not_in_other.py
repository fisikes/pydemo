import pandas

df1 = pandas.DataFrame(data={'col1': [1, 2, 3, 4, 5], 'col2': [10, 11, 12, 13, 14]})
df2 = pandas.DataFrame(data={'col1': [1, 2, 3], 'col2': [10, 11, 12]})

common = df1.merge(df2, on=['col1', 'col2'])
print(common)
other = df1[(~df1.col1.isin(common.col1)) & (~df1.col2.isin(common.col2))]
print(other)