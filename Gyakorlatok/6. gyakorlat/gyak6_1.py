import matplotlib.pyplot as plt
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.power(np.e,-x))

def sigmoid_derivate(x):
    return sigmoid(x) * (1 - sigmoid(x))

x = np.arange(-3,3,0.01)
y = sigmoid(x) #az egesz vektor atadhato a fv-nek
dy = sigmoid_derivate(x)

plt.plot(x,y,'g-',label="sigmoid")
plt.plot(x,dy,'r-',label="sigmoid derivate")
plt.xlabel("X értékek") #x tengely cime
plt.ylabel('Y értékek') #y tengely cime
plt.title("Sigmoid függvény") #az egesz abra cime
plt.legend() #jelmagyarazat bekapcsolasa
plt.show()