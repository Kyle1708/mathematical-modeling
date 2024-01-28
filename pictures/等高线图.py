import matplotlib.pyplot as plt
import numpy as np

# 创建示例数据
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# 创建等高线图
plt.contour(X, Y, Z, levels=20, cmap='viridis')  # levels参数控制等高线的数量

# 添加标签和标题
plt.xlabel('X轴')
plt.ylabel('Y轴')
plt.title('等高线图示例')

plt.colorbar()  # 添加颜色条

plt.show()
