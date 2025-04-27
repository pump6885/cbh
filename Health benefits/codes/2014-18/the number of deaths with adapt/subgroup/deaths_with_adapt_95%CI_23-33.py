import numpy as np
import pandas as pd
import glob
import os

folder_path = '/Users/cbhbook/Desktop/code/Health benefits/data/adapt_Monte Carlo'
new_path = '/Users/cbhbook/Desktop'
os.makedirs(new_path, exist_ok=True)
os.chdir('/Users/cbhbook/Desktop/code/Health benefits/data')
ar = pd.read_csv('./AR_95%CI_subgroup.csv')
inc_files = glob.glob(os.path.join(folder_path, 'inc*.csv'))  
for inc_file in inc_files:    
    print(f'Processing file: {inc_file}')
    flag = inc_file.split('wealth')[-1].split('.')[0]
    res = pd.DataFrame()
    df = pd.read_csv(inc_file)     
    df['wealth'] = df['wealth'] * 5 -1
    df = df[~df['temp'].isin(['No knee'])]
    for w in range(5):
        sub_ar = ar.loc[((ar['temp'] >= 23) & (ar['wealth'] == w)), :].copy()
        sub_ar.index = list(np.arange(len(sub_ar)))  
        wealth = sub_ar['wealth']
        temp = sub_ar['temp']
        sub_ar = sub_ar.iloc[:, -200:]
        sub_ar.columns = list(np.arange(200))

        adap = df.loc[(df['wealth'] == w), :].copy()
        adap = adap.iloc[:, -200:]
        adap.index = list(np.arange(len(adap)))
        adap.columns = list(np.arange(200))

       
        if adap.shape[0] > sub_ar.shape[0]:
            adap = adap.reindex(sub_ar.index)
        elif sub_ar.shape[0] > adap.shape[0]:
            sub_ar = sub_ar.reindex(adap.index)

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
        print(death)
        res = pd.concat([res, death], axis=0)
    res.to_csv('/Users/cbhbook/Desktop/95CI_inc_after_ele_grid'+flag+'.csv')




