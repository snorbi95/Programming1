import matplotlib.pyplot as plt
import numpy as np

def histogram(mtx):
    h = np.zeros(20) # lehetseges elemek
    for i in range(20):
        h[i] = np.sum(mtx == i) # az i-edik elem elofordulasainak szama a matrixban
    return h

mtx = np.random.randint(0,20,(100,100)) # random matrix
h = histogram(mtx)

plt.bar(range(20),h) #oszlopdiagram abrazolas
plt.show()
