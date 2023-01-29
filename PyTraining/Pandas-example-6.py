#Plotting with Pandas

import pandas as pd
import matplotlib.pyplot as plt


data_frame = pd.read_csv('data.csv')

# data_frame.plot()

# Data_frame.plot(kind = 'scatter', x='Duration', y = 'Calories')

data_frame["Maxpulse"].plot(kind= 'hist')

plt.show()

