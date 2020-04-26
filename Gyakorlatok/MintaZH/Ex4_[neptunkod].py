import numpy as np

n = int(input("Kerem a sorok szamat: "))
m = int(input("Kerem az oszlopok szamat: "))

low = int(input("Kerem az intervallum kezdo erteket: "))
high = int(input("Kerem az intervallum vegerteket: "))

num = int(input("Kerem a szamot: "))

mtx = np.random.randint(low,high,(n,m))

def calc(szam):
    szam = str(szam)
    sum = 0
    for ch in szam:
        sum += int(ch)
    return sum

lista = []

for j in range(mtx.shape[1]):
    count = 0
    for i in range(mtx.shape[0]):
        if calc(mtx[i,j]) > num:
            count += 1
    if count >= n / 2:
        lista.append(j + 1)

print(mtx)
print(lista)