import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

mean = [0, 0, 0]
cov = [[1, 0, 0],
       [0, 1, 0],
       [0, 0, 1]]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x, y, z = np.random.multivariate_normal(mean, cov, 5000).T
plt.scatter(x, y, z)
plt.axis('equal')
plt.show()