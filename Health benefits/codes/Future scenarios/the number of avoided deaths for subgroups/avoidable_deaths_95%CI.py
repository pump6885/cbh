import pandas as pd
import numpy as np
import os

#  95%CI  the number of avoidable deaths for wealth subgroups #
folder_path = '/Users/cbhbook/Desktop/code/Health benefits/data/future'

adapt_folder_path = '/Users/cbhbook/Desktop/code/Health benefits/data/future/adapt_monte carlo'
output_path = '/Users/cbhbook/Desktop'


rr_ci_n = pd.read_csv(os.path.join(folder_path, 'RR_CI_subgroup.csv'), index_col=0)

precision_levels = [1000, 1500, 2000, 2500, 3000]

# ssp1——ssp1-2.6,  ssp2——ssp2-4.5,  ssp4——ssp3-7.0,    ssp5——ssp5-8.5
ssp_ls = [1, 2, 4, 5]
yy = [2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100]


for precision in precision_levels:
    
    new_wealth_adapt = pd.read_csv(os.path.join(adapt_folder_path, f'new_wealth{precision}_adapt.csv'), index_col=0)

    for ssp in ssp_ls:
        ssp_pop_wealth = pd.read_csv(os.path.join(folder_path, f'ssp{ssp}_pop_income.csv'))
        ssp_days = pd.read_csv(os.path.join(folder_path, f'ssp{ssp}_days_count.csv'), index_col=0)

       
        result_df = pd.DataFrame(
            columns=['year', 'wealth', f'grid{precision}_ssp{ssp}_death_95ll', f'grid{precision}_ssp{ssp}_death_95ul'] + list(np.arange(200)))

        count = 0
        
        for wealth in range(5):
            
            rr = rr_ci_n.loc[rr_ci_n['wealth'] == wealth].drop(columns='wealth')
            adapt = new_wealth_adapt.loc[new_wealth_adapt['wealth'] == wealth].drop(columns=['wealth'])
            for year in yy:  
                deaths = np.zeros((34, 200))
                for i in range(34):
                    temp_days = ssp_days.loc[year, str(i)]  
                    for j in range(200):
                        rr_value = rr.iloc[i, j]
                        adapt_value = adapt.iloc[i, j]
                        if rr_value < 1:  
                            adapt_value = 0  
                        deaths[i, j] = (rr_value - 1) / rr_value * adapt_value * (6.494 / 1000) * temp_days * \
                                       ssp_pop_wealth.loc[wealth, f'year_{year}'] / 365
                result_df.loc[count, 'year'] = year
                result_df.loc[count, 'wealth'] = wealth
                result_df.loc[count, f'grid{precision}_ssp{ssp}_death_95ll'] = np.percentile(deaths.sum(axis=0), 2.5)
                result_df.loc[count, f'grid{precision}_ssp{ssp}_death_95ul'] = np.percentile(deaths.sum(axis=0), 97.5)
                result_df.loc[count, list(np.arange(200))] = pd.DataFrame(deaths).sum(axis=0)
                count += 1
        print(result_df)
        
        result_df.to_csv(os.path.join(output_path, f'avoid_death_ssp{ssp}_grid{precision}_try.csv'), index=False)



