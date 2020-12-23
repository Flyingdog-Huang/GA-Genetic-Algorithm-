import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# fig = plt.figure()
# ax = Axes3D(fig)
#
# x = np.arange(0, 11, 0.01)  # np.random.randint(20,size=10) 形如： array([4, 1, 4, 3, 8, 2, 8, 5, 8, 19])
# y = np.arange(-5, 6, 0.01)
#
# X, Y = np.meshgrid(x, y)  # [important] 创建网格 np.meshgrid(xnums,ynums)
#
# Z = np.power((np.power(X, 2) + Y - 11), 2) + np.power((X + np.power(Y, 2) - 7), 2)
# plt.xlabel('x')
# plt.ylabel('y')
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
# plt.savefig('fig.png', bbox_inches='tight')  # 替换 plt.show()plt.show()

x = np.arange(-5, 6, 0.01)
y = (x - 2) ** 2 + (x ** 2 - 4) ** 2
plt.plot(x, y)
plt.show()