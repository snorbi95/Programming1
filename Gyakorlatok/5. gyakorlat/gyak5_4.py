import numpy as np

def oszthato_indexek(m):
    list = []
    for i in range(m.shape[0]): #matrix minden elemen vegighaladunk ket for ciklussal
        for j in range(m.shape[1]):
            if m[i,j] % (i + 1) == 0 and m[i,j] % (j + 1) == 0: #muveletek matrix elemmel es az indexekkel
                list.append((m[i,j],i+1,j+1)) #lista bovites a szamharmassal
    return list

m = np.random.randint(1,50,(3,4))
print(oszthato_indexek(m))