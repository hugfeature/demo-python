# author:丑牛
# datetime:2020/7/2 16:55
import matplotlib.pyplot as plt

y1 = [1, 2, 5, 40, 30, 60, 70, 12, 55, 25]
x1 = range(0, 10)
plt.plot(x1, y1, label='Frist line', linewidth=3, color='r', marker='o', markerfacecolor='blue', markersize=12)
plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()

