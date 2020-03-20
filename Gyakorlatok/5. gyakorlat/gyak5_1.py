import numpy as np

def is_sorted(a):
    if a[0] < a[1]:
        for i in range(1,a.size):
            if a[i - 1] > a[i]:
                return "Hamis"
        return "Igaz"
    elif a[0] > a[1]:
        for i in range(1, a.size):
            if a[i - 1] < a[i]:
                return "Hamis"
        return "Igaz"

# a = np.arange(1,10)
a = np.random.randint(1,50,size=10)
print(is_sorted(a))