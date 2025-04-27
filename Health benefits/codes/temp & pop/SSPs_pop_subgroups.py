import pandas as pd
import numpy as np




####   SSP1  pop of each wealth subgroup   ########
ssp1_percentage = pd.read_csv('/Users/cbhbook/Desktop/code/Health benefits/data/future/ssp1_percentage.csv')
csj_pop = pd.read_csv('/Users/cbhbook/Desktop/code/Health benefits/data/future/csj_pop_ssps.csv')

print(ssp1_percentage)
print(csj_pop)

csj_pop_ssp1 = csj_pop[csj_pop['ssp'] == 'ssp1'].copy()

result_df = pd.DataFrame()
result_df['Wealth'] = ssp1_percentage['Wealth']
years = [2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100]
ssp1_columns = ['ssp1_cat_2030', 'ssp1_cat_2040', 'ssp1_cat_2050', 'ssp1_cat_2060',
                'ssp1_cat_2070', 'ssp1_cat_2080', 'ssp1_cat_2090', 'ssp1_cat_2100']

for year, ssp1_col in zip(years, ssp1_columns):
    csj_pop_ssp1_year = csj_pop_ssp1[csj_pop_ssp1['year'] == year]['长三角'].values[0]
    result_df[f'year_{year}'] = ssp1_percentage[ssp1_col] * csj_pop_ssp1_year / 100
result_df.to_csv('/Users/cbhbook/Desktop/ssp1_pop_income.csv', index=False)

####   SSP2  pop of each wealth subgroup     ########
ssp2_percentage = pd.read_csv('/Users/cbhbook/Desktop/code/Health benefits/data/future/ssp2_percentage.csv')

print(ssp2_percentage)
print(csj_pop)

csj_pop_ssp2 = csj_pop[csj_pop['ssp'] == 'ssp2'].copy()

result_df = pd.DataFrame()
result_df['Wealth'] = ssp2_percentage['Wealth']
years = [2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100]
ssp2_columns = ['ssp2_cat_2030', 'ssp2_cat_2040', 'ssp2_cat_2050', 'ssp2_cat_2060',
                'ssp2_cat_2070', 'ssp2_cat_2080', 'ssp2_cat_2090', 'ssp2_cat_2100']

for year, ssp2_col in zip(years, ssp2_columns):
    csj_pop_ssp2_year = csj_pop_ssp2[csj_pop_ssp2['year'] == year]['长三角'].values[0]
    result_df[f'year_{year}'] = ssp2_percentage[ssp2_col] * csj_pop_ssp2_year / 100
result_df.to_csv('/Users/cbhbook/Desktop/ssp2_pop_income.csv', index=False)


####   SSP4  pop of each wealth subgroup     ########
ssp4_percentage = pd.read_csv('/Users/cbhbook/Desktop/code/Health benefits/data/future/ssp4_percentage.csv')

# print(ssp4_percentage)
# print(csj_pop)

csj_pop_ssp4 = csj_pop[csj_pop['ssp'] == 'ssp4'].copy()

result_df = pd.DataFrame()
result_df['Wealth'] = ssp4_percentage['Wealth']
years = [2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100]
ssp4_columns = ['ssp4_cat_2030', 'ssp4_cat_2040', 'ssp4_cat_2050', 'ssp4_cat_2060',
                'ssp4_cat_2070', 'ssp4_cat_2080', 'ssp4_cat_2090', 'ssp4_cat_2100']

for year, ssp4_col in zip(years, ssp4_columns):
    csj_pop_ssp4_year = csj_pop_ssp4[csj_pop_ssp4['year'] == year]['长三角'].values[0]
    result_df[f'year_{year}'] = ssp4_percentage[ssp4_col] * csj_pop_ssp4_year / 100
result_df.to_csv('/Users/cbhbook/Desktop/ssp4_pop_income.csv', index=False)

####   SSP5  pop of each wealth subgroup     ########
ssp5_percentage = pd.read_csv('/Users/cbhbook/Desktop/code/Health benefits/data/future/ssp5_percentage.csv')

# print(ssp5_percentage)
# print(csj_pop)

csj_pop_ssp5 = csj_pop[csj_pop['ssp'] == 'ssp5'].copy()

result_df = pd.DataFrame()
result_df['Wealth'] = ssp5_percentage['Wealth']
years = [2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100]
ssp5_columns = ['ssp5_cat_2030', 'ssp5_cat_2040', 'ssp5_cat_2050', 'ssp5_cat_2060',
                'ssp5_cat_2070', 'ssp5_cat_2080', 'ssp5_cat_2090', 'ssp5_cat_2100']

for year, ssp5_col in zip(years, ssp5_columns):
    csj_pop_ssp5_year = csj_pop_ssp5[csj_pop_ssp5['year'] == year]['长三角'].values[0]
    result_df[f'year_{year}'] = ssp5_percentage[ssp5_col] * csj_pop_ssp5_year / 100
result_df.to_csv('/Users/cbhbook/Desktop/ssp5_pop_income.csv', index=False)

