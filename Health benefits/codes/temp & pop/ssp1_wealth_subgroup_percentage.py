import pandas as pd
df = pd.read_csv('/Users/cbhbook/Desktop/code/Health benefits/data/future/Income_freq_SSPs.csv')
# print(df)
bins = [0, 9731, 17470, 26740, 40520, float('inf')]   # bins denotes the quintile interval cutoffs for per capita disposable income in each wealth subgroup
labels = [1, 2, 3, 4, 5]

income_cols = [
    'ssp1_income2030', 'ssp1_income2040', 'ssp1_income2050', 'ssp1_income2060',
    'ssp1_income2070', 'ssp1_income2080', 'ssp1_income2090', 'ssp1_income2100'
]
cat_cols = [
    'ssp1_cat_2030', 'ssp1_cat_2040', 'ssp1_cat_2050', 'ssp1_cat_2060',
    'ssp1_cat_2070', 'ssp1_cat_2080', 'ssp1_cat_2090', 'ssp1_cat_2100'
]
percentages = {}
for income_col, cat_col in zip(income_cols, cat_cols):
    df[cat_col] = pd.cut(df[income_col], bins=bins, labels=labels, right=True)
    df.loc[df[income_col] == 0, cat_col] = 1
    counts = df.groupby(cat_col, observed=False)['freqs'].sum()
    total = counts.sum()
    percentage = (counts / total) * 100
    percentages[cat_col] = percentage

    percentage_df = pd.DataFrame(percentages)

    output_path = '/Users/cbhbook/Desktop/ssp1_percentage.csv'
    percentage_df.to_csv(output_path, index=True)
