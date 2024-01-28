import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 创建示例数据
data = []
categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']

for category in categories:
    category_data = np.random.normal(0, 1, 100)
    data.append(category_data)

# 创建组合小提琴图
fig, ax = plt.subplots()

# 使用Seaborn的violinplot函数绘制组合小提琴图
sns.violinplot(data=data, inner="stick", ax=ax)

# 添加标签和标题
ax.set_xticklabels(categories)
ax.set_xlabel('类别')
ax.set_ylabel('数值')
ax.set_title('组合小提琴图')

plt.show()
