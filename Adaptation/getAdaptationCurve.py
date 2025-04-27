import pandas as pd
import numpy as np
import random
import warnings

warnings.filterwarnings("ignore")


"""
1. Mark users who have not identified inflection points as 'No knee'
2. Statistical analysis of tipping points
"""
df = pd.read_csv('./2014-2018daily_knee.csv', index_col=0)
df['kneedle_covcon_dec'] = df[['kneedle_con_dec', 'kneedle_cov_dec']].min(axis=1)
print(df)
df["kneedle_cov_inc"].fillna("No knee", inplace = True)
df["kneedle_covcon_dec"].fillna("No knee", inplace = True)
res_inc = pd.DataFrame()
res_dec = pd.DataFrame()
inc = df.loc[:, ['kneedle_cov_inc', 'kneedle_covcon_dec']].groupby(['kneedle_cov_inc']).count().unstack()
dec = df.loc[:, ['kneedle_cov_inc', 'kneedle_covcon_dec']].groupby(['kneedle_covcon_dec']).count().unstack()
inc2 = inc.copy(deep=True)
for i in range(1, len(inc)-1):
    inc2.iloc[i] = inc2.iloc[i] + inc2.iloc[i-1]
res_inc = pd.concat([res_inc, inc2['kneedle_covcon_dec'].div(inc.sum())], axis=1)
dec2 = dec.copy(deep=True)
for i in range(2, len(dec)):
    dec2.iloc[len(dec)-i-1] = dec2.iloc[len(dec)-i-1] + dec2.iloc[len(dec)-i]
res_dec = pd.concat([res_dec, dec2['kneedle_cov_inc'].div(dec.sum())], axis=1)    
res_inc.to_csv('./inc_knee_total.csv')
res_dec.to_csv('./dec_knee_total.csv')



"""
Using Monte Carlo method to obtain the confidence interval of the adaptation curve
"""
L = list(df.index)
res_inc = pd.DataFrame()
res_dec = pd.DataFrame()
for s in range(200):
    print(s)
    random.seed(s)
    x = random.sample(L, k=int(len(df)*0.8))
    sub_df = df.loc[x, :]
    inc = sub_df.loc[:, ['kneedle_cov_inc', 'kneedle_covcon_dec']].groupby(['kneedle_cov_inc']).count().unstack()
    dec = sub_df.loc[:, ['kneedle_cov_inc', 'kneedle_covcon_dec']].groupby(['kneedle_covcon_dec']).count().unstack()
    inc2 = inc.copy(deep=True)
    for i in range(1, len(inc)-1):
        inc2.iloc[i] = inc2.iloc[i] + inc2.iloc[i-1]
    res_inc = pd.concat([res_inc, inc2['kneedle_covcon_dec'].div(inc.sum())], axis=1)        
    dec2 = dec.copy(deep=True)
    for i in range(2, len(dec)):
        dec2.iloc[len(dec)-i-1] = dec2.iloc[len(dec)-i-1] + dec2.iloc[len(dec)-i]
    res_dec = pd.concat([res_dec, dec2['kneedle_cov_inc'].div(dec.sum())], axis=1)
res_inc = pd.concat([res_inc, res_inc.quantile(0.025, axis=1), res_inc.quantile(0.975, axis=1)], axis=1)
res_inc.columns = list(np.arange(200)) + ['CI 2.5%', 'CI 97.5%']
res_dec = pd.concat([res_dec, res_dec.quantile(0.025, axis=1), res_dec.quantile(0.975, axis=1)], axis=1)
res_dec.columns = list(np.arange(200)) + ['CI 2.5%', 'CI 97.5%']
print(res_inc)
res_inc.to_csv('./inc_knee_mcv2.csv')
res_dec.to_csv('./dec_knee_mcv2.csv')

