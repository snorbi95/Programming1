import numpy as np

def count_negative_and_zeros(m):
    list = []
    for j in range(m.shape[1]): #oszlopfolytonos bejaras
        zeros = 0 #minden oszlop megkezdesekor nullazzuk a szamlalot
        negative = 0
        for i in range(m.shape[0]): #oslopok elemenkenti bejarasa
            if m[i,j] == 0:
                zeros += 1
            elif m[i,j] < 0:
                negative += 1
        if negative >= zeros * 2 and zeros > 0:
            list.append(j) #oszlopindex eltarolasa
    return list

sor = input("Kerem a matrix mereteit: ")
n, m = sor.split()

m = np.random.randint(-1,1,(int(n),int(m)))
print(m)
print(count_negative_and_zeros(m))