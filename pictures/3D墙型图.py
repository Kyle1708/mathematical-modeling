import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# 生成示例数据
category = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
values = np.random.randint(1, 50, (len(months), len(category)))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 设置每个bar的位置和宽度
xpos, ypos = np.meshgrid(np.arange(values.shape[0]), np.arange(values.shape[1]))
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros(values.size)
dx = 0.5 * np.ones_like(zpos)
dy = dx.copy()
dz = values.flatten()

# 设置颜色
colors = plt.cm.jet(np.linspace(0, 1, len(category)))

for c in range(len(category)):
    ax.bar3d(xpos[c::len(category)], ypos[c::len(category)], zpos[c::len(category)],
             dx[c::len(category)], dy[c::len(category)], dz[c::len(category)],
             color=colors[c])

# 设置坐标轴标签
ax.w_xaxis.set_ticklabels(months)
ax.w_yaxis.set_ticklabels(category)
ax.set_xlabel('Month')
ax.set_ylabel('Category')
ax.set_zlabel('Value')

# 设置图例
patch_list = []
for index, c in enumerate(category):
    patch_list.append(plt.Line2D([0], [0], linestyle="none", marker="s", markersize=10, markerfacecolor=colors[index]))
ax.legend(patch_list, category, numpoints=1)

plt.show()
