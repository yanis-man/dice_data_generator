import random
import matplotlib.pyplot as plt

min_v = 1
max_v = 6

data = [0 for x in range(0,6)]

shots = int(input("number of shots : "))
for i in range(5):
    for i in range(shot):
        data[random.randint(min_v, max_v)-1] += 1
names = [x+1 for x in range(0,6)]   
plt.bar(names, data)
plt.show()