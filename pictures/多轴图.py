import matplotlib.pyplot as plt
import numpy as np

# 创建示例数据
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(x)

# 创建多轴图，4个子轴
fig, axes = plt.subplots(2, 2, figsize=(10, 6))

# 在每个子轴上绘制不同的图表
axes[0, 0].plot(x, y1, color='b')
axes[0, 0].set_title('正弦函数')

axes[0, 1].plot(x, y2, color='g')
axes[0, 1].set_title('余弦函数')

axes[1, 0].plot(x, y3, color='r')
axes[1, 0].set_title('正切函数')

axes[1, 1].plot(x, y4, color='purple')
axes[1, 1].set_title('指数函数')

# 调整子轴之间的间距
plt.tight_layout()

plt.show()
