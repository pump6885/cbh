import pandas as pd
import numpy as np
import scipy
import time
import warnings
warnings.filterwarnings("ignore")

start = time.time()
ele = pd.read_csv('./electricity_consumption.csv', index_col='ID')
print('file read finished')
# print(ele)


s_ele = pd.DataFrame()
p = 0
for i in range(len(ele)):
    if i % 10000 == 0:
        print(i)
    try:
        y_smooth = scipy.signal.savgol_filter(ele.iloc[i, -35:], 9, 3)
        s_ele = pd.concat([s_ele, pd.DataFrame(y_smooth).transpose()], axis=0)
    except:
        s_ele = pd.concat([s_ele, pd.DataFrame([[np.NaN]*35])], axis=0)
        p += 1
        continue
print(p)
s_ele.index = list(ele.index)
print(s_ele)

s_ele.to_csv('./2014-2018daily_smooth_w9.csv')

end= time.time()
print(end-start)
