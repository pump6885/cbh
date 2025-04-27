import pandas as pd
import os


#   the number of deaths with adaptation under 4 scenarios #
folder_path =  '/Users/cbhbook/Desktop/code/Health benefits/data/future'

rr_w = pd.read_excel(os.path.join(folder_path, 'RR_subgroup.xlsx'), index_col=0)
adapt_grid = pd.read_excel(os.path.join(folder_path, 'adapt_subgroup.xlsx'), index_col=1)

# ssp1——ssp1-2.6,  ssp2——ssp2-4.5,  ssp4——ssp3-7.0,  ssp5——ssp5-8.5
ssp_scenarios = ['ssp1', 'ssp2', 'ssp4', 'ssp5']

ls = [1000, 1500, 2000, 2500, 3000]


for ssp in ssp_scenarios:
    
    days_df = pd.read_csv(os.path.join(folder_path, f'{ssp}_days_count.csv'), index_col=0)
    pop_wealth_df = pd.read_csv(os.path.join(folder_path, f'{ssp}_pop_income.csv'), index_col=0)
    
    result = []
    
    for grid in ls:
        flag = 'grid' + str(grid)  
        sub_a = adapt_grid[adapt_grid['grid'] == flag]
       
        for year in days_df.index:
            days = days_df.loc[year].values  
            
            for wealth in range(5):
                pop = pop_wealth_df.loc[wealth, f'year_{year}']  
                rr_values = rr_w[rr_w['wealth'] == wealth]  
                
                total_death = 0
               # The temperature range is from 0 to 33 celsius degrees, with a total of 34 temperature values
                for temp in range(34):
                    w = sub_a[f'w{wealth}'].iloc[temp]  
                    rr = rr_values.iloc[temp]['RR']  
                    if rr < 1:  
                        w = 0  
                    death = pop * (1 - 1 / rr) * (1 - w) * 6.494 / 1000  
                    total_death += death * days[temp]
                annual_death = total_death / 365  
                result.append({
                    'grid': flag,
                    'year': year,
                    'wealth': wealth,
                    f'{ssp}_death': annual_death
                })
                
    result_df = pd.DataFrame(result)

    
    output_file = '/Users/cbhbook/Desktop/'f'{ssp}_death_try.csv'
    result_df.to_csv(output_file, index=False)

