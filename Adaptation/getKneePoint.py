import pandas as pd
import numpy as np
from kneed import KneeLocator
import warnings
warnings.filterwarnings("ignore")


ele = pd.read_csv('./2014-2018daily_smooth_w9.csv', index_col=0)

low = np.arange(24)
high = np.arange(22, 35)
knee = pd.DataFrame(np.zeros((len(ele), 4)), index=list(ele.index), columns=['kneedle_cov_inc', 'kneedle_cov_dec', 'kneedle_con_inc', 'kneedle_con_dec'])
for i in range(len(ele)):
    y_low = ele.iloc[i, :24]
    y_high = ele.iloc[i, 22:]
    kneedle_cov_inc = KneeLocator(high, y_high, curve='convex', direction='increasing', online=True)
    kneedle_cov_dec = KneeLocator(low, y_low, curve='convex', direction='decreasing', online=True)
    kneedle_con_inc = KneeLocator(high, y_high, curve='concave', direction='increasing', online=True)
    kneedle_con_dec = KneeLocator(low, y_low, curve='concave', direction='decreasing', online=True)
    knee.iloc[i, 0] = kneedle_cov_inc.knee
    knee.iloc[i, 1] = kneedle_cov_dec.knee
    knee.iloc[i, 2] = kneedle_con_inc.knee
    knee.iloc[i, 3] = kneedle_con_dec.knee

res = pd.concat([ele, knee], axis=1)
print(res)
res.to_csv('./2014-2018daily_knee.csv')
