n = input("kerek egy szamot:")

#1. megoldás
sum = 0
for ch in n:
    sum += int(ch)

print(sum)

sum = 0

n = int(n)
#2. megoldás
while n > 0:
    sum += n % 10
    n = n // 10

print(sum)