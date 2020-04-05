primes = set(range(2,5001))
p = 2

def is_prime(p):
    oszto = 0
    for i in range(1, (p // 2) + 1):
        if p % i == 0:
            oszto += 1
    if oszto == 1:
        return True
    return False

while p < 5000:
    while not is_prime(p) and p < 5000:
        p += 1
    k = p + p
    while k <= 5000:
        if k in primes:
            primes.remove(k)
        k = k + p
    p += 1

print(primes)