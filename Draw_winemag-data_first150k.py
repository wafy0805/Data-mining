import matplotlib.pyplot as plt

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

waters = ('California Other','Central Coast','Central Valley','Columbia Valley','Finger Lakes','Long Island','Mendocino/Lake Countries','Napa','Napa-Sonoma','New York Other','North Coast','Oregon Other','Sierra Foothills','Sonoma','South Coast','Southern Oregon','Washington Other','Willamette Valley')
buy_number = [3516,13057,1115,9157,1510,771,2389,8801,1645,147,632,661,1660,11258,198,662,593,3181]
plt.xticks(rotation = 270)
plt.bar(waters, buy_number)
plt.title('region_2频数分布')

plt.show()
