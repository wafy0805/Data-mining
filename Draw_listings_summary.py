import matplotlib.pyplot as plt

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

waters = ('Banyule','Bayside','Boroondara','Brimbank','Cardinia','Casey','Darebin','Frankston','Glen Eira','Greater Dandenong','Hobsons Bay','Hume','Kingston','Knox','Manningham','Maribyrnong','Maroondah','Melbourne','Melton','Monash','Moonee Valley','Moreland','Nillumbik','Port Phillip','Stonnington','Whitehorse','Whittlesea','Wyndham','Yarra','Yarra Ranges')
buy_number = [203,375,664,108,123,153,698,177,631,147,239,170,309,175,313,436,115,7368,95,571,344,967,88,2808,1621,614,137,426,2049,771]
plt.xticks(rotation = 270)
plt.bar(waters, buy_number)
plt.title('neighbourhood频数分布')

plt.show()
