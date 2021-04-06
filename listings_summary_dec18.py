import matplotlib.pyplot as plt
import numpy as np
import csv
from functools import reduce

with open('listings_summary_dec18.csv',"rt", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    tang_array = [row[9] for row in reader]
tang_array.pop(0)
print(tang_array)
arr = list(map(int,tang_array))

fig = plt.figure(figsize=(8, 6))
plt.boxplot(arr, notch=False, sym='o', vert=True)


plt.title('box plot')
plt.xlabel('x')
plt.show()