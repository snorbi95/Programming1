import numpy as np

def is_sorted(a):
    if a[0] < a[1]: #ha novekvo sorozattal indul a vektor
        for i in range(1,a.size): #vegig iteralas
            if a[i - 1] > a[i]: # ha nem teljesul a novekvo sorrend
                return "Hamis"
        return "Igaz" #a vegig novekvo, igaz
    elif a[0] > a[1]: # ha csokkeno sor
        for i in range(1, a.size):
            if a[i - 1] < a[i]: #ha nem teljesul a csokkeno sor
                return "Hamis"
        return "Igaz" # ha vegig csokkeno, igaz

# a = np.arange(1,10)
a = np.random.randint(1,50,size=10)
print(is_sorted(a))