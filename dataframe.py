#!/usr/bin/env python
import pandas as pd
import numpy as np

appNum = 10
featMatCols = ['c1', 'c2', 'c3']
df_app = pd.DataFrame(index=np.arange(0, appNum), columns=featMatCols)
print "raw"
print df_app

print "add values in the df"
v = 0.
for row in xrange(0, appNum):
    for col in featMatCols:
        v += 0.1
        df_app.loc[row, col] = v 

print df_app

# store df to csv
df_app.to_csv('df_app.csv', index=False, encoding='utf-8')
