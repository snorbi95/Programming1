def lnko(a,b):
    if b < a:
        a, b = b, a
    div = 1
    for i in range(2, a + 1):
        if a % i == 0 and b % i == 0:
            div = i
    return div


sor = input("Kerek ket szamot:")
a,b = sor.split()
print(lnko(int(a),int(b)))