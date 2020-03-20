import numpy as np

def count_negative_and_zeros(m):
    list = []
    for j in range(m.shape[1]):
        zeros = 0
        negative = 0
        for i in range(m.shape[0]):
            if m[i,j] == 0:
                zeros += 1
            elif m[i,j] < 0:
                negative += 1
        print(negative, zeros)
        if negative >= zeros * 2 and zeros > 0:
            list.append(j)
    return list

m = np.random.randint(-1,1,(3,4))
print(m)
print(count_negative_and_zeros(m))