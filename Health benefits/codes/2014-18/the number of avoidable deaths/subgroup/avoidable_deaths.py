

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random

"""
1. Read the files of RR and adaptation pproportion for each wealth subgroup separately
2. Concatenate two files with code
3. Calculatee mortality rate
"""

####  the avoidable deaths  ########
rr = pd.read_excel('/Users/cbhbook/Desktop/code/Health benefits/data/RR_subgroup.xlsx', sheet_name='Sheet1')
adaptation = pd.read_excel('/Users/cbhbook/Desktop/code/Health benefits/data/adapt_subgroup.xlsx', sheet_name='Sheet1')
print(rr)
ls = [1000, 1500, 2000, 2500, 3000]
for i in ls:
    res = pd.DataFrame()   
    flag = 'grid'+str(i)   # Generates a string flag corresponding to the current grid value, such as 'grid1000'
    sub_a = adaptation.loc[adaptation['grid']==flag, :] 
    sub_a.set_index('temp', inplace=True)   
    print(sub_a)
    for w in range(5):
        sub_rr = rr.loc[rr['wealth'] ==w, :]   
        sub_rr.set_index('temp', inplace=True)  
        df = pd.concat([sub_a, sub_rr], axis=1) 
        # print(df)
        for k in range(35):
            if df.loc[k, 'RR_wealth'] < 1:
                res.loc[k, 'death' + str(w)] = 0
            else:
                res.loc[k, 'death' + str(w)] = df.loc[k, 'w' + str(w)] * (
                    (df.loc[k, 'RR_wealth'] - 1)/(df.loc[k, 'RR_wealth'])) * 6494 * 229.0282
        res['death' + str(w)] = res['death' + str(w)].fillna(0).round().astype(int)
    print(res)
    res.to_csv('/Users/cbhbook/Desktop/death_avoid_' + flag + '.csv')
