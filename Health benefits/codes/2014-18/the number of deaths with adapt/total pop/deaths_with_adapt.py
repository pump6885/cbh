import pandas as pd
import numpy as np
import glob
import os

####  the number of deaths with adapt for total pop  ########
folder_path = '/Users/cbhbook/Desktop'
avoid_a =pd.read_csv('/Users/cbhbook/Desktop/code/Health benefits/data/adapt_RR_total.csv')
# print(after_a)

after_deaths = pd.DataFrame()
avoid_a.set_index('Temp', inplace=True)
after_deaths['after_deaths'] = (1-avoid_a['Adapt']) * (avoid_a['RR_KAN'] - 1) / avoid_a['RR_KAN'] * 6494 * 229.0282
# print(after_deaths)
after_deaths.index.name = 'Temp'

output_path = os.path.join(folder_path, 'deaths_with_adapt_total.csv')
after_mr.to_csv(output_path)


#####  95%CI   ########
RR_CI =pd.read_csv('/Users/cbhbook/Desktop/code/Health benefits/data/RR_total_95%CI.csv')
adapt_200 =pd.read_csv('/Users/cbhbook/Desktop/code/Health benefits/data/adapt_95%CI.csv')

print(RR_CI)
print(adapt_200)


df = pd.DataFrame()
df['Temp'] = RR_CI['Temp']


for i in range(200):
    rr_column = f'RR_kan{i}'
    a_column = f'a{i}'
    after_death_column = f'after_death{i}'
    df[after_death_column] = (1 - adapt_200[a_column]) * (RR_CI[rr_column] - 1) / RR_CI[rr_column] * 6494 * 229.0282


after_death_columns = [f'after_death{i}' for i in range(200)]
df['after_death_2.5%'] = df[after_death_columns].quantile(0.025, axis=1)
df['after_death_97.5%'] = df[after_death_columns].quantile(0.975, axis=1)


output_path = os.path.join(folder_path, 'after_deaths_with_adapt_ci.csv')
df.to_csv(output_path, index=False)









