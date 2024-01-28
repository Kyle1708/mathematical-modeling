import matplotlib.pyplot as plt
import numpy as np

# 创建示例数据
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# 创建箱线图
fig, ax = plt.subplots()

# 使用boxplot函数绘制箱线图
ax.boxplot(data, vert=False, labels=['数据集1', '数据集2', '数据集3'])

# 添加标签和标题
ax.set_xlabel('数值')
ax.set_title('箱线图示例')

plt.show()
