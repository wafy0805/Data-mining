import matplotlib.pyplot as plt

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

waters = ('Alexander Peartree','Anna Lee C.Iijima','Anne Krebiehl MW','Carrie Dykes','Christina Pickard','Fiona Adams','Jeff Jenssen','Jim Gordan','Joe Czerwinski','Kerin O','Lauren Buzzeo','Matt Kettmann','Michael Schachner','Mike DeSimone','Paul Gregutt','Roger Voss','Sean P.Sullivan','Susan Kostrzewa','Virginie Boone')
buy_number = [314,4415,3685,139,6,27,491,4177,5147,10776,1835,6332,15134,514,9532,25514,4966,1085,9537]
plt.xticks(rotation = 270)
plt.bar(waters, buy_number)
plt.title('taster_name频数分布')

plt.show()
