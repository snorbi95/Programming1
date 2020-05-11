import numpy as np

n = int(input("Kerem a vektor meretet: ")) #adatok bekerese
low = int(input("Intervallum eleje: "))
high = int(input("Intervallum vege: "))

vec = np.random.randint(low,high,size = n) #random np vektor letrehozasa
avg = np.average(vec) #atlag kiszamitasa
print("A létrhezozott vektor: {}".format(vec))
vec[np.abs(vec - avg) > 5] += high #a vektor azon ertekeinek modositasa amelyek teljesitik a feltetelt
print("A vektor átlaga: {}".format(avg))
print("A modisitott vektor: {}".format(vec))