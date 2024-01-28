import matplotlib.pyplot as plt
import numpy as np

# 创建示例数据
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 8, 3, 6, 4]

# 创建颜色列表，确保颜色数量与数据点数量相同
colors = ['red', 'green', 'blue', 'purple', 'orange']

# 创建二维条形图，并为每个条形指定颜色
plt.barh(categories, values, color=colors)

# 添加标签和标题
plt.xlabel('数值')
plt.ylabel('类别')
plt.title('每个柱子颜色不一样的二维条形图')

plt.show()
