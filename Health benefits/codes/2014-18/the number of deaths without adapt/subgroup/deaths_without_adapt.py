import pandas as pd
import numpy as np
import glob
import os

###  without adaptation  the number of deaths = MR * (RR-1)/RR * POP
###  the number of deaths for subgroups without adaptations  ###
folder_path = '/Users/cbhbook/Desktop'
rr = pd.read_excel('/Users/cbhbook/Desktop/code/Health benefits/data/RR_subgroup.xlsx')
# print(rr)
for w in range(5):
    mr_subgroup = pd.DataFrame()
    sub_rr = rr.loc[rr['wealth'] == w, :]
    sub_rr.set_index('temp', inplace=True)
    mr_subgroup['death' + str(w)] = ((sub_rr['RR_wealth'] - 1) / sub_rr['RR_wealth']) * 6494 * 229.0282
    mr_subgroup['death' + str(w)] = mr_subgroup['death' + str(w)].fillna(0).round().astype(int)
    mr_subgroup.to_csv(f'/Users/cbhbook/Desktop/deaths_without_a_subgroup_{w}.csv')


#####  95%CI    ########
RR_CI =pd.read_csv('/Users/cbhbook/Desktop/code/Health benefits/data/RR_95%CI_subgroup.csv')
print(RR_CI)
for w in range(5):
    mr_subgroup = pd.DataFrame()
    sub_RR_CI = RR_CI.loc[RR_CI['wealth'] == w, :]
    sub_RR_CI.set_index('temp', inplace=True)
    for i in range(200):
       rr_column = f'RR{i}'
       death_column = f'death{i}'
       RR_CI[death_column] = (RR_CI[rr_column] - 1) / RR_CI[rr_column] * 6494 * 229.0282

death_columns = [f'death{i}' for i in range(200)]
RR_CI['death_2.5%'] = RR_CI[death_columns].quantile(0.025, axis=1)
RR_CI['death_97.5%'] = RR_CI[death_columns].quantile(0.975, axis=1)

output_path = os.path.join(folder_path, 'death_without_a_ci.csv')
RR_CI.to_csv(output_path, index=False)