import matplotlib.pyplot as plt

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

waters = ('Aparthotel', 'Apartment', 'Barn', 'Bed and breakfast', 'Boat','Boutique hotel','Bungalow','Cabin','Camper/RV','Campsite','Casa particular','Castle','Chalet','Condominium','Cottage','Earth house',' Farm stay','Guest suite','Guesthouse','Hostel','Hotel','House','Hut','Loft','Minsu(Taiwan)','Nature lodge','Other','Resort','Serviced apartment','Tent','Tiny house','Townhouse','Train','Treehouse','Villa')
buy_number = [12, 12649, 5, 263, 8,44,157,46,16,10,1,4,4,544,157,10,43,260,276,32,11,5967,3,191,1,8,49,6,500,9,25,1434,1,3,326]
plt.xticks(rotation = 270)
plt.bar(waters, buy_number)
plt.title('property_type频数分布')

plt.show()
