# author:丑牛
# datetime:2020/7/2 17:18
import matplotlib.pyplot as plt
population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,
                   110,120,121,122,130,111,115,112,80,75,
                   65,54,44,43,42,48]
x=range(0,len(population_ages))
plt.scatter(x,population_ages,label='frist label',s=20)
help(plt.scatter)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()