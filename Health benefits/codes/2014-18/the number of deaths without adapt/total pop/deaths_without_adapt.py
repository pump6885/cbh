import pandas as pd
import numpy as np
import glob
import os

##################
# 1. the number of deaths without adapt
folder_path = '/Users/cbhbook/Desktop/code/Health benefits/data'
RR_total =pd.read_excel( '/Users/cbhbook/Desktop/code/Health benefits/data/RR_total.xlsx')
# print(RR_total)

death_total = pd.DataFrame()
RR_K.set_index('Temp', inplace=True)
death_total['death'] =(RR_total['RR'] - 1) / RR_total['RR'] * 6494 * 229.0282
print(death_total)
death_total.index.name = 'Temp'

output_path = os.path.join(folder_path, 'death_total.csv')
death_total.to_csv(output_path)

#####  95% CI    ########
RR_CI =pd.read_csv('/Users/cbhbook/Desktop/code/Health benefits/data/RR_total_95%CI.csv')

for i in range(200):
    rr_column = f'RR_total{i}'
    death_column = f'death_kan{i}'
    RR_CI[death_column] = (RR_CI[rr_column] - 1) / RR_CI[rr_column] * 6494 * 229.0282

# the number of death percentile 2.5% percentile 97.5%
death_columns = [f'death_kan{i}' for i in range(200)]
RR_CI['death_2.5%'] = RR_CI[death_columns].quantile(0.025, axis=1)
RR_CI['death_97.5%'] = RR_CI[death_columns].quantile(0.975, axis=1)


output_path = os.path.join(folder_path, 'death_kan_ci.csv')
RR_CI.to_csv(output_path, index=False)