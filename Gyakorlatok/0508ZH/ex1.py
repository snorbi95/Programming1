
n = int(input("Kerek egy számot: ")) # n bekerese

def count_mgh(szo):
    mgh = "aeiou" # maganhangzok definialasa
    count = 0 #szamlalo definialasa
    for ch in szo: #szo betunkenti iteralasa -> pl: alma esetén -> 'a', 'l','m','a' elemeket vizsgalja sorban a ciklus
        if ch in mgh: # ha az adott betű benne van a maganhangzok kozott
            count += 1 #szamlalo novelelse
    return count #visszateres a szamlaloval

lista1, lista2 = [],[] # ures listak definialasa
szo = input("Kerem a kovetkezo szot: ") #szo bekerese
while szo != '0': #amig a szo nem '0' (string típus!)
    count = count_mgh(szo) #a count valtozo vegye fel a fv. erteket (mgh-k szama)
    if count > n: #ha a mgh. szama nagyobb mint n
        lista1.append(szo + str(count)) #elso listba rakjuk (szo + mgh.szam)
    else:
        lista2.append(szo + str(count)) #masodik listaba rakjuk (szo + mgh.szam)
    szo = input("Kerem a kovetkezo szot: ") #kovetkezo szo bekerese

print(lista1) #eredmenyek kiiratasa
print(lista2)