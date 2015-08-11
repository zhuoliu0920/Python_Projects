#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm

df = pd.read_csv('body.dat', header=None, delim_whitespace=True)
df['MASS'] = df[22]/(df[23]**2)
# need to change the column21 name to 'Age'


result = sm.ols(formula="MASS ~ Age", data=df).fit()
