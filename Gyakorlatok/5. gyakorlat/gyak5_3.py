import numpy as np

def sor_oszlop_osszegek(m):
    row_sum = m.sum(axis = 0)
    col_sum = m.sum(axis = 1)
    tmp = row_sum[0]
    for i in range(m.shape[0]):
        if tmp != row_sum[i] or tmp != col_sum[i]:
            return False
    return True


# m = np.random.randint(1,50,(3,3))
m = np.ones((3,3))
print(m)
print(sor_oszlop_osszegek(m))