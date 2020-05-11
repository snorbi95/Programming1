import numpy as np

mtx = np.random.randint(1,51,(3,4)) #random matrix letrehozas

lista = [] #eredmenylista definialas

def calc(n,i,j):
    return n / ((i + 1) * (j + 1))

for i in range(mtx.shape[0]): #matrix bejarasa
    for j in range(mtx.shape[1]):
        if calc(mtx[i,j],i,j) > 1 and calc(mtx[i,j],i,j) < 2: #ha teljesul a feltetel (kiertekeles fuggvenyben)
            lista.append((mtx[i,j],i,j)) #a listahoz hozzaadjuk a szamharmast

print(mtx)
print(lista)
