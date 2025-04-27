import numpy as np
import pandas as pd
import glob
import os
# print(os.getcwd()) 

folder_path = '/Users/cbhbook/Desktop/code/Health benefits/data/adapt_Monte Carlo'
new_path = '/Users/cbhbook/Desktop'
os.makedirs(new_path, exist_ok=True)
os.chdir('/Users/cbhbook/Desktop/code/Health benefits/data')
ar = pd.read_csv('./AR_95%CI_subgroup.csv')
dec_files = glob.glob(os.path.join(folder_path, 'dec*.csv')) 
for dec_file in dec_files:     
    print(f'Processing file: {dec_file}')
    flag = dec_file.split('wealth')[-1].split('.')[0]
    res = pd.DataFrame()
    df = pd.read_csv(dec_file)    
    df['wealth'] = df['wealth'] * 5 -1
    df = df[~df['temp'].isin(['No knee'])]
    for w in range(5):
        sub_ar = ar.loc[((ar['temp']<22) & (ar['wealth']==w)), :]
        sub_ar.index = list(np.arange(len(sub_ar)))
        wealth = sub_ar['wealth']
        temp = sub_ar['temp']
        sub_ar = sub_ar.iloc[:, -200:]
        sub_ar.columns = list(np.arange(200))
        adap = df.loc[(df['wealth'] == w), :]
        adap = adap.iloc[:, -200:]
        adap.index = list(np.arange(len(adap)))
        adap.columns = list(np.arange(200))
        for j in range(200):
            ind = sub_ar[sub_ar[j] < 0].index.tolist()
            adap.loc[ind, j] = 0
           
            death = pd.DataFrame(
                np.where(sub_ar < 0, sub_ar * 6494 * 229.0282, (1 - adap) * sub_ar * 6494 * 229.0282),
                columns=sub_ar.columns
            )
        death['CI2.5%'] = death.loc[:, list(np.arange(200))].quantile(0.025, axis=1)
        death['CI97.5%'] = death.loc[:, list(np.arange(200))].quantile(0.975, axis=1)
        death = pd.concat([temp, wealth, death], axis=1)

        res = pd.concat([res, death], axis=0)
    res.index = list(np.arange(len(res)))
    res.to_csv('/Users/cbhbook/Desktop/95CI_0-21_after_ele_grid'+flag+'.csv')


