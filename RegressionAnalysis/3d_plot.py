import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd

df = pd.read_csv('appl_1980_2014.csv')

cols = df.iloc[:, 1:4].values

x1 = cols[:,0]
x2 = cols[:,1]
x3 = cols[:,2]

ax = plt.axes(projection='3d')
#ax.plot3D(x1,x2,x3)
ax.scatter(x1,x2,x3)
plt.show()

