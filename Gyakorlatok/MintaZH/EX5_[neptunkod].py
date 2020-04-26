import numpy as np
import matplotlib.pyplot as plt

def fv1(x):
    return (3 * x + 2)**2

def fv2(x):
    return (3 * x - 2) / x

vec = np.arange(-25,26)

plt.subplot(1,2,1)
plt.plot(range(len(vec)),fv1(vec),'g')
plt.title("Elso fuggveny")
plt.subplot(1,2,2)
plt.plot(range(len(vec)),fv2(vec),'r')
plt.title("Masodik fuggveny")
plt.show()