import matplotlib.pyplot as plt
import numpy as np

# 定义双曲面的参数
a = 1.0
b = 2.0

# 创建网格点
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# 计算双曲面的z值
Z = (X**2 / a**2) - (Y**2 / b**2)

# 创建3D图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制双曲面
surf = ax.plot_surface(X, Y, Z, cmap='viridis')

# 添加坐标轴标签
ax.set_xlabel('X轴')
ax.set_ylabel('Y轴')
ax.set_zlabel('Z轴')

# 添加标题
plt.title('双曲面函数图')

# 添加颜色条
fig.colorbar(surf)

plt.show()
