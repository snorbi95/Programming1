import matplotlib.pyplot as plt
import numpy as np

def histogram(mtx):
    h = np.zeros(20)
    for i in range(20):
        h[i] = np.sum(mtx == i)
    return h

mtx = np.random.randint(0,20,(100,100))
h = histogram(mtx)

plt.bar(range(20),h)
plt.show()
