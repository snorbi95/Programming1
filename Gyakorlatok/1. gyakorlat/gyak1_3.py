from math import sqrt, pow

x = input("x:")
y = input("y:")
x1, y1 = x.split()
x2, y2 = y.split()

print(sqrt(pow(int(x1) - int(x2), 2) + pow(int(y1) - int(y2), 2)))