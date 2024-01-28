import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# 创建Basemap对象，指定投影和区域
m = Basemap(projection='merc', llcrnrlat=-60, urcrnrlat=85, llcrnrlon=-180, urcrnrlon=180, resolution='c')

# 绘制海岸线和国界
m.drawcoastlines()
m.drawcountries()

# 添加标签和标题
plt.title('世界地图示例')

# 显示地图
plt.show()
