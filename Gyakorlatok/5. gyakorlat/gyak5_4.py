import numpy as np

def oszthato_indexek(m):
    list = []
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            if m[i,j] % (i + 1) == 0 and m[i,j] % (j + 1) == 0:
                list.append((m[i,j],i+1,j+1))
    return list

m = np.random.randint(1,50,(3,4))
print(oszthato_indexek(m))