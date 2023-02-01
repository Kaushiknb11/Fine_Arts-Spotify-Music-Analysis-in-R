
"""
DataPrep_EDA

"""

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv("/Users/kaushiknarasimha/Downloads/2016_2020/US_Accidents_June20.csv")
df1.head(5)


#Data Preparation and Cleaning

df1.columns()

df1.shape

df1.info()

df1.describe()


#State wise crash counts




