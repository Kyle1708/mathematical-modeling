import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# 示例数据
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0, 0.1, 0, 0)  # 突出显示某一块

# 创建环型图
fig, ax = plt.subplots()

# 绘制环型图
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=140,
    pctdistance=0.85,
    explode=explode
)

# 自定义渐变填充的颜色
cmap = LinearSegmentedColormap.from_list('custom', ['gold', 'darkorange', 'red'])
gradient = np.linspace(0, 1, 256).reshape(1, -1)
gradient = np.vstack((gradient, gradient))

# 创建渐变填充
ax.imshow(gradient, cmap=cmap, extent=(-0.7, 0.7, -0.7, 0.7), aspect='auto', zorder=0)

# 设置环的边框宽度和颜色
for w in wedges:
    w.set_linewidth(2)
    w.set_edgecolor('gray')

# 添加标题
plt.title('带渐变填充的环形图示例')

ax.axis('equal')

plt.show()


