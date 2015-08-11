#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm

# read input file into data frame
df = pd.read_csv('./stats/player_regular_season.csv')
# calculate efficiency for each player each season
df['eff'] = ((df.pts+df.reb+df.asts+df.stl+df.blk)-((df.fga-df.fgm)+(df.fta-df.ftm)+df.turnover)) / df.gp
# list the top 5 efficiencies
df[['lastname','firstname','eff']].sort(columns='eff',ascending=False).head(6)

"""#df = pd.read_csv('./stats/some.txt', header=None, delim_whitespace=True)
#df.to_csv('test.csv') 

df.head()
df.tail(3)
df.index
df.columns
df.describe()
df.T #transpose
df.sort_index(axis=1, ascending=False)
df.sort(columns='pts', ascending=False)
df[ ['firstname','lastname'] ]
df[0:3]
df.loc[0:3, ['firstname','lastname'] ] # = df.iloc[0:4, 2:4]
df[df.pts > 2500]
df[df.firstname == 'Kobe'] # = df[df.firstname.isin(['Kobe'])]

df.dropna(how='any') # np.nan is NaN in pandas
df.fillna(value=5)
pd.isnull(df)

df.mean() # for each column
df.mean(1) # for each row

df['pts'].apply(np.cumsum, axis=0) #or 1)
df['pts'].apply(lambda x: x.max() - x.min())
df['lastname'].value_counts()
df['lastname'].str.lower()

pieces = [df[:3], df[3:7], df[7:]]
pd.concat(pieces) # Concatenating (append columns)
df.append(s, ignore_index=True) # append to last row

pd.merge(left, right, on='key') # join

df[['firstname','lastname','pts']].groupby(['firstname','lastname']).sum() # grouping

df['firstname'].astype("category") # change to categorical type
df["grade"].cat.categories = ["very good", "good", "very bad"] # rename categories

plt.figure(); df.plot(); plt.legend(loc='best') # plot all columns"""

