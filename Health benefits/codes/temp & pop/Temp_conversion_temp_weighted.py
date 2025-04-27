import pandas as pd
####  first  temperature Celsius degree  #####

file_path = '/Users/cbhbook/Desktop/code/Health benefits/data/future/yangtze_delta_bcc_tas.csv'
df = pd.read_csv(file_path)

df['temp'] = df['tas'] - 273.15
csv_file_path = '/Users/cbhbook/Desktop/code/Health benefits/data/future/yangtze_delta_bcc_tas.csv'
df.to_csv(csv_file_path, index=False)

####  second  Yangzte Rivier Delta daily temperature  ######

df = pd.read_csv('/Users/cbhbook/Desktop/code/Health benefits/data/future/yangtze_delta_bcc_tas.csv')
print(df)

weights = {
    "上海市": 0.017837047,
    "江苏省": 0.301598019,
    "浙江省": 0.286405582,
    "安徽省": 0.394159352
}

df['weighted_temp'] = df['temp'] * df['province'].map(weights)
temp_n_df = df.groupby(['date', 'ssp'])['weighted_temp'].sum().reset_index()


temp_n_df.rename(columns={'weighted_temp': 'temp_n'}, inplace=True)


temp_n_df.to_csv("yangtze_delta_temp_weighted.csv", index=False)


#####  third   date:yyyy-mm-dd convert to year mm-dd  ######

df = pd.read_csv('/Users/cbhbook/Desktop/code/Health benefits/data/future/yangtze_delta_temp_weighted.csv')


df['year'] = pd.to_datetime(df['date']).dt.year
df['day_month'] = pd.to_datetime(df['date']).dt.strftime('%m-%d')


df.to_csv("yangtze_delta_temp_weighted.csv", index=False)

###  fourth  order#####
df = pd.read_csv('/Users/cbhbook/Desktop/code/Health benefits/data/future/yangtze_delta_temp_weighted.csv')
df = df.sort_values(by=['date', 'ssp'])
print(df)
df.to_csv("yangtze_delta_temp_weighted.csv", index=False)