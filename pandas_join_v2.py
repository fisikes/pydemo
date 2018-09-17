import pandas as pd

csv_df_left = pd.read_csv('stars_met/spec.csv', dtype=str)
print(csv_df_left.shape)

dat_df_right = pd.read_csv('stars_met/all_stat_z_log.csv', dtype=str)
print(dat_df_right.shape)

result = pd.merge(csv_df_left,
                  dat_df_right,
                  how='inner',
                  left_on=['plate', 'mjd', 'fiberid'],
                  right_on=['_plate', '_mjd', '_fiberid'])
print(result.shape)

result.to_csv('stars_met/Result.csv', index=False)
