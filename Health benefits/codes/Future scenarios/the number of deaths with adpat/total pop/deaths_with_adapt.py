import os
import pandas as pd

#  the number of deaths with adaptation for total pop #
folder_path = '/Users/cbhbook/Desktop/code/Health benefits/data/future'
output_path = '/Users/cbhbook/Desktop'


rr_kan = pd.read_excel(os.path.join(folder_path, 'RR_total_pop.xlsx'), index_col=0)
adapt = pd.read_csv(os.path.join(folder_path, 'adapt_total_pop.csv'), index_col=0)

# ssp1——ssp1-2.6,  ssp2——ssp2-4.5,  ssp4——ssp3-7.0,  ssp5——ssp5-8.5
ssp_scenarios = ['ssp1', 'ssp2', 'ssp4', 'ssp5']


target_years = [2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100]


for ssp in ssp_scenarios:
    #
    days_df = pd.read_csv(os.path.join(folder_path, f'{ssp}_days_count.csv'), index_col=0)
    pop_wealth_df = pd.read_csv(os.path.join(folder_path, f'{ssp}_csj.csv'), index_col=0)
    # print(pop_wealth_df)

    result = []
    
    for year in target_years:
        days = days_df.loc[year].values  
        rr_values = rr_kan['RR']  

        pop = pop_wealth_df.loc[year, 'csj'] 
        # print(pop)
        total_death = 0  
        
        for temp in range(34):
            rr = rr_values.iloc[temp]  
            w = adapt['Adapt'].iloc[temp]  
            death = pop * (1 - 1 / rr) * (1 - w) * 6.494 / 1000  
            total_death += death * days[temp]  

       
        annual_death = total_death / 365  
        # print(annual_death)
        
        result.append({
            'year': year,
            f'{ssp}_after_death': annual_death  
        })

   
    result_df = pd.DataFrame(result)

 
    result_df.to_csv(os.path.join(output_path, f'{ssp}_after_death.csv'), index=False)









