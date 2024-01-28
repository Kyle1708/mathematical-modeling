import matplotlib.pyplot as plt

# 示例数据
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

# 创建饼图
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# 添加标题
plt.title('饼图示例')

plt.axis('equal')  # 使饼图保持圆形

plt.show()
