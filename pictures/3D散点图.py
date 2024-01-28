import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 创建示例数据
n = 100  # 数据点数量
x = np.random.rand(n)
y = np.random.rand(n)
z = np.random.rand(n)

# 创建4x4的子图
fig, axes = plt.subplots(4, 4, figsize=(12, 12), subplot_kw={'projection': '3d'})

# 在每个子图中绘制3D散点图
for i in range(4):
    for j in range(4):
        ax = axes[i, j]
        ax.scatter(x, y, z, c='b', marker='o')
        ax.set_xlabel('X轴')
        ax.set_ylabel('Y轴')
        ax.set_zlabel('Z轴')
        ax.set_title(f'Subplot {i+1}-{j+1}')

# 调整子图之间的间距
plt.tight_layout()

plt.show()
