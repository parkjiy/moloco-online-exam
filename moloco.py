#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 22:45:11 2019

@author: jiyoung park
"""

import pandas as pd

data = pd.read_csv('SWE sample data - Q3 data.csv', index_col = 0)

#####
1
#####
data[data['country_id'] == 'BDV'].groupby('site_id')['user_id'].nunique()

#####
2
#####
four_df = data['2019-02-03 00:00:00':'2019-02-04 23:59:59']
fouruser = four_df.groupby(['user_id','site_id']).site_id.count()
fouruser[fouruser > 10]

#####
3
#####
lastdf = data.groupby('user_id')['site_id'].nth(-1)
lastdf.groupby(lastdf, sort = False).count()

#####
4
#####
first_visit = data.groupby('user_id')['site_id'].nth(0)
last_visit = data.groupby('user_id')['site_id'].nth(-1)
#print('This is the list of first visit: ', first_visit)
#print('This is the list of last visit: ', last_visit)
print('the number of users whose first/last visits are to the same website: ', 
      first_visit[first_visit == last_visit].count())

#####
5
#####
keys = set(data['site_id'])
values = []
for x in keys:
    c = data[data['site_id']==x].groupby('user_id').country_id.count()
    A = len(c[c > 1])
    values.append(A)
Adict = dict(zip(keys, values))
print('This is A: ', Adict)

#using dictionary for (B)
valuesb = []
for x in keys: 
    B = data[data['site_id']==x]['user_id'].nunique()
    valuesb.append(B)
Bdict = dict(zip(keys, valuesb))
print('This is B :', Bdict)

#using without dictionary for (B) 
#data.groupby('site_id')['user_id'].nunique()

new_A = {k: v for k, v in Adict.items() if v >= 1}
new_B = {key: Bdict[key] for key in new_A}
ratio = {k: new_B[k]/new_A[k] for k in new_A}
print('The ratio are: ', ratio)

