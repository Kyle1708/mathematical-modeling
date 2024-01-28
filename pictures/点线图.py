import matplotlib.pyplot as plt
import numpy as np

# 创建示例数据
x = np.linspace(0, 10, 100)  # X轴数据
y = np.sin(x)  # 对应的Y轴数据，这里以正弦函数为例

# 创建点线图
plt.plot(x, y, marker='o', linestyle='-', color='b', label='数据点')

# 添加标签和标题
plt.xlabel('X轴')
plt.ylabel('Y轴')
plt.title('点线图示例')

# 添加网格线
plt.grid(True)

# 添加图例
plt.legend()

plt.show()
