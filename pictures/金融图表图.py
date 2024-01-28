import matplotlib.pyplot as plt
import pandas as pd

# 创建示例数据（模拟股票价格走势）
data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'Price': [100, 105, 110, 108, 112]
}

# 将数据转换为Pandas DataFrame
df = pd.DataFrame(data)

# 将日期列转换为日期时间类型
df['Date'] = pd.to_datetime(df['Date'])

# 创建金融图表
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Price'], marker='o', linestyle='-')

# 添加标签和标题
plt.xlabel('日期')
plt.ylabel('股票价格')
plt.title('股票价格走势图')

# 旋转x轴的日期标签，使其更易读
plt.xticks(rotation=45)

plt.grid(True)

plt.show()
