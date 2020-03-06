import numpy as np

def vektor_fordit(a):
    b = np.zeros_like(a) #letreehozunk a nullakkal feltoltott vektort (ugyanolyan méretű, mint az a vektor)
    for i in range(a.size): #iretálunk 0,1...az a vektor végéig
        b[i] = a[a.size - i - 1] #a b vektor elejét feltöltjük az a vektor végéről kezdve
    print("A: {}".format(a))
    print("B: {}".format(b))

def vektor_rendezo(a):
    for i in range(a.size - 1): #vegigiteralunk a vektoron az utolsó elötti elemig
        for j in range(i + 1, a.size): #az aktualis i inextől a vektor végéig iterálunk
            if a[i] > a[j]: #ha az i indexen nagyobb elem van, mint a következő indexek valamelyikén
                a[i], a[j] = a[j], a[i] # csere
    return a

#1. feladat
# a = np.arange(10,50) #[10,11...,49] vektor létrehozás
# vektor_fordit(a)

#2. feladat
# b = np.random.randint(1,50,size = 10) #tiz elemű random vektor 1 és 50 közötti értékekkel
# min_max_values = b[(b == b.min()) | (b == b.max())] #azon értékek kigyűgytése egy új vektorba, amelyek min, vagy maxok
# print(b)
# print(min_max_values)
# min_max_indices = np.where((b == b.min()) | (b == b.max())) # min, vagy max értékek helyének megkeresése
# print(min_max_indices)

#3. feladat
# c = np.random.randint(1,100,size = 30)
# c[c == c.max()] = -1 # a maximum érték felűlírása -1-re
# print(c)

#4. feladat
# d = np.random.randint(1,100,size = 30)
# print(d)
# sorted = vektor_rendezo(d)
# print(sorted)

#5. feladat
# e = np.arange(-5,15)
# e[(e > 3) & (e < 8)] *= -1 #3 és 8 közötti értékek negálása
# print(e)

#6. feladat
# f = np.random.randint(1,50,size = 10)
# print(f)
# num = int(input("Kerek egy szamot:"))
# dist = np.abs(num - f) #a vektor összes elemének a bekért számtól való távolsága eltárolása egy új vektorba
# print(dist)
# min_helyek = np.where(dist == dist.min()) #a legkisebb távolságú elem helyének megkeresése
# print(f[min_helyek]) #a talált helyen lévő érték kiiratása

#7. feladat
g = np.random.randint(-50,50,size = 30)
print(g)
pos = g[g > 0]
print(pos)
neg = g[g < 0]
print(neg)
zeros = g[g == 0]
print(zeros)
print("pozitiv: {}, negativ: {}, nullak: {}".format(pos.size,neg.size,zeros.size))