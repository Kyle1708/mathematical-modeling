import numpy as np
import matplotlib.pyplot as plt

# 创建示例数据
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# 创建堆叠面积图
fig, ax = plt.subplots()

ax.fill_between(x, y1, label='sin(x)', alpha=0.5)
ax.fill_between(x, y1, y1+y2, label='cos(x)', alpha=0.5)
ax.fill_between(x, y1+y2, y1+y2+y3, label='tan(x)', alpha=0.5)

# 添加标签和图例
ax.set_xlabel('X轴')
ax.set_ylabel('Y轴')
ax.set_title('堆叠面积图示例')
ax.legend()

plt.show()
