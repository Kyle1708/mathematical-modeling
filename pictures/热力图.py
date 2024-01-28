import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 创建示例数据，这里使用随机生成的数据
np.random.seed(42)
data = np.random.rand(10, 10)  # 创建一个10x10的随机数据矩阵

# 创建热力图
sns.heatmap(data, annot=True, cmap='viridis')

# 添加标签和标题
plt.xlabel('X轴')
plt.ylabel('Y轴')
plt.title('热力图示例（更多数据点）')

plt.show()
