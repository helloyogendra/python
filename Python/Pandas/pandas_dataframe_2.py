import os
import sys

import pandas as pd
import numpy as np

import datetime as dt


clear = lambda : os.system('cls')
clear()

# 1
# 1.1
# DataFrame
# Data Extraction - set_index()  and reset_index()
#
def dataframe_1():
    file = "Data\\jamesbond.csv"
    bond = pd.read_csv(file)