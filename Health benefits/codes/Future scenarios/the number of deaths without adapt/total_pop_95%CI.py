import os
import pandas as pd
import numpy as np

#   95%CI the number of deaths without adaptation under 4 scenarios #
folder_path = '/Users/cbhbook/Desktop/code/Health benefits/data/future'
output_path = '/Users/cbhbook/Desktop'


rr_kan = pd.read_csv(os.path.join(folder_path, 'RR_total_pop_CI.csv'), index_col=0)
print(rr_kan)
# ssp1——ssp1-2.6,  ssp2——ssp2-4.5,  ssp4——ssp3-7.0,    ssp5——ssp5-8.5
ssp_scenarios = ['ssp1', 'ssp2', 'ssp4', 'ssp5']

target_years = [2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100]

for ssp in ssp_scenarios:
    
    days_df = pd.read_csv(os.path.join(folder_path, f'{ssp}_days_count.csv'), index_col=0)
    pop_wealth_df = pd.read_csv(os.path.join(folder_path, f'{ssp}_csj.csv'), index_col=0)
    # print(pop_wealth_df)

    ssp_results = []
    
    for year in target_years:
        days = days_df.loc[year].values  
        pop = pop_wealth_df.loc[year, 'csj']  
        
        total_deaths_per_simulation = []
        
        for j in range(200):
            total_death = 0  
            
            for temp in range(34):  
                rr = rr_kan.iloc[temp, j]  
                # print(rr)
                death = pop * (1 - 1 / rr) * 6.494 / 1000  
                total_death += death * days[temp]  

            
            annual_death = total_death / 365 
            total_deaths_per_simulation.append(annual_death)

        
        ll_95 = np.percentile(total_deaths_per_simulation, 2.5)
        ul_95 = np.percentile(total_deaths_per_simulation, 97.5)

        
        ssp_results.append({
            'year': year,
            f'{ssp}_death_non_ele_95%ll': ll_95,
            f'{ssp}_death_non_ele_95%ul': ul_95,
            **{f'{ssp}_death_non_ele_{i}': total_deaths_per_simulation[i] for i in range(200)}
        })



    ssp_results_df = pd.DataFrame(ssp_results)



    ssp_results_df.to_csv(os.path.join(output_path, f'{ssp}_CI_death_non_ele.csv'), index=False)
