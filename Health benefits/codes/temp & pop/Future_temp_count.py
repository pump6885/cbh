import pandas as pd
import numpy as np

csv_file_path = '/Users/cbhbook/Desktop/code/Health benefits/data/future/yangtze_delta_temp_weighted.csv'
df = pd.read_csv(csv_file_path)


if 'temp_n' in df.columns:
    # # Create new temperature bins, including below 1 Celsius degree, 0 to 33 degrees, 33 to 34 Celsius degrees, and 34 Celsius degrees and above

    bins = [-np.inf, 1, *np.arange(2, 34, 1), 34, np.inf]  # -np.inf denotes the temperature below 0 Celsius degree

    labels = ['<1'] + [f"{i}-{i + 1}" for i in range(1, 33)] + ['33-34', '34+']

    df['temp_bin'] = pd.cut(df['temp_n'], bins=bins, right=False, labels=labels)

    ssp_categories = ['ssp126', 'ssp245', 'ssp370', 'ssp585']

    for ssp in ssp_categories:

        ssp_df = df[df['ssp'] == ssp]

        year_temp_counts = pd.DataFrame()

        years = np.arange(2030, 2101, 10)

        for year in years:
            year_df = ssp_df[ssp_df['year'] == year]

            temp_bin_counts = year_df.groupby('temp_bin', observed=False).size()

            temp_bin_counts_df = temp_bin_counts.reset_index(name=f'{year}_days')

            if year_temp_counts.empty:
                year_temp_counts = temp_bin_counts_df
            else:
                year_temp_counts = year_temp_counts.merge(temp_bin_counts_df, on='temp_bin', how='outer')


        year_temp_counts.set_index('temp_bin', inplace=True)
        year_temp_counts = year_temp_counts.transpose()


        output_file_path = f'/Users/cbhbook/Desktop/{ssp}_days_count.csv'
        year_temp_counts.to_csv(output_file_path)

        print(year_temp_counts)
