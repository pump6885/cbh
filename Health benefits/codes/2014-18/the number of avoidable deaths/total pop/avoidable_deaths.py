import pandas as pd
import numpy as np
import glob
import os


####  the avoidable deaths for total population  ########
folder_path = '/Users/cbhbook/Desktop'
avoid_a =pd.read_csv('/Users/cbhbook/Desktop/code/Health benefits/data/adapt_RR_total.csv')
# print(after_a)

avoid_death = pd.DataFrame()
avoid_a.set_index('Temp', inplace=True)
avoid_death['after_death'] = avoid_a['Adapt'] * (avoid_a['RR_KAN'] - 1) / avoid_a['RR_KAN'] * 6494 * 229.0282
# print(after_death)
avoid_death.index.name = 'Temp'

output_path = os.path.join(folder_path, 'avoid_death_total.csv')
avoid_death.to_csv(output_path)


#####   95%CI  ######
RR_CI =pd.read_csv('/Users/cbhbook/Desktop/code/Health benefits/data/RR_total_95%CI.csv')
adapt_200 =pd.read_csv('/Users/cbhbook/Desktop/code/Health benefits/data/adapt_95%CI.csv')

# print(RR_CI)
# print(adapt_200)

df = pd.DataFrame()
df['Temp'] = RR_CI['Temp']


for i in range(200):
    rr_column = f'RR_kan{i}'
    a_column = f'a{i}'
    avoid_death_column = f'avoid_death{i}'
    df[avoid_death_column] = adapt_200[a_column] * (RR_CI[rr_column] - 1) / RR_CI[rr_column] * 6494 * 229.0282

#  Percentile2.5% and  Percentile97.5% 
avoid_death_columns = [f'avoid_death{i}' for i in range(200)]
df['avoid_death_2.5%'] = df[avoid_death_columns].quantile(0.025, axis=1)
df['avoid_death_97.5%'] = df[avoid_death_columns].quantile(0.975, axis=1)


output_path = os.path.join(folder_path, 'avoid_death_ci.csv')
df.to_csv(output_path, index=False)
