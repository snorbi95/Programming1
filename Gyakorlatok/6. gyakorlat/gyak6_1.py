import matplotlib.pyplot as plt
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.power(np.e,-x))

def sigmoid_derivate(x):
    return sigmoid(x) * (1 - sigmoid(x))

x = np.arange(-3,3,0.01)
y = sigmoid(x)
dy = sigmoid_derivate(x)

plt.plot(x,y,'g-',label="sigmoid")
plt.plot(x,dy,'r-',label="sigmoid derivate")
plt.xlabel("X értékek")
plt.ylabel('Y értékek')
plt.title("Sigmoid függvény")
plt.legend()
plt.show()