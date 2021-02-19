# author:丑牛
# datetime:2020/7/2 17:17
import matplotlib.pyplot as plt
population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,
                   110,120,121,122,130,111,115,112,80,75,
                   65,54,44,43,42,48]
x=range(0,130,10)
plt.hist(population_ages, x, rwidth=0.8, color='r', histtype='stepfilled')

plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()

