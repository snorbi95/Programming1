import numpy as np

def oszlop_rendezo(m,ind):
    for i in range(m.shape[0] - 1):
        for j in range(i + 1, m.shape[0]):
            if m[i, ind] > m[j, ind]:
                m[i,ind], m[j,ind] = m[j,ind], m[i,ind]

m = np.random.randint(1,50,(4,5))
print(m.shape[0])
print(m.shape[1])
print(m)
ind = int(input("Kerek egy oszlopindexet:"))
oszlop_rendezo(m,ind)
print(m)