import matplotlib.pyplot as plt
import numpy as np

# 创建示例数据
np.random.seed(42)
data = [np.random.rand(50) for _ in range(16)]

# 创建4x4的宫格
fig, axes = plt.subplots(4, 4, figsize=(12, 12))

# 遍历每个子图并绘制散点图
for i, ax in enumerate(axes.flat):
    ax.scatter(data[i], data[(i+1) % 16], alpha=0.6)  # 使用alpha参数调整点的透明度
    ax.set_xlabel('X轴')
    ax.set_ylabel('Y轴')
    ax.set_title(f'子图 {i+1}')

# 调整子图之间的间距
plt.tight_layout()

# 添加整体标题
plt.suptitle('4x4散点图宫格示例', fontsize=16)

plt.show()
