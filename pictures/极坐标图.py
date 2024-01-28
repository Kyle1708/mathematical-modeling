import matplotlib.pyplot as plt
import numpy as np

# 创建示例数据
theta = np.linspace(0, 2 * np.pi, 100)  # 极角范围
r = 1.5 * np.cos(3 * theta)  # 极径，这里以余弦函数为例

# 创建极坐标图
plt.figure(figsize=(6, 6))
ax = plt.subplot(111, projection='polar')

# 绘制极坐标线条
ax.plot(theta, r, label='数据线')

# 添加标签和标题
ax.set_rlabel_position(90)  # 设置极坐标刻度标签位置
plt.title('极坐标图示例')

plt.legend()

plt.show()
