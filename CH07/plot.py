import matplotlib.pyplot as plt
import numpy as np

# 折線圖
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

# 點狀圖
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()

# 長條圖
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
# plt.show()
plt.savefig('123.png') # 存成圖檔