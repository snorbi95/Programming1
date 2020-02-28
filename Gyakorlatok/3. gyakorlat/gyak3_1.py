import sys, random

def lista_feltoltes(args):
    list1 = []
    list2 = [] #eredmeny listak inicializalasa
    num_l = 0 #lista sorszam inicializalas
    for arg in args: #az argumenumokn sorban végig megyünk
        if arg == "L:": #ha egy lista kezdetét találjuk
            num_l += 1 #növeljük a sorszámot
        else: #ellenben, ha listán beül járunk
            if num_l == 1: #megnézzük, hogy mely sorszámnál tartunk
                list1.append(arg)
            elif num_l == 2:
                list2.append(arg)

    return list1, list2

list1, list2 = lista_feltoltes(sys.argv[1:])

def osszead_n_ig(args):
    n = int(args[0])
    file_name = args[1] #az argumentumok letarloasa valtozokba
    out_file = open(file_name, "w") #fajl megnyitas
    sum = 0 #osszeg init
    for i in range(1,n+1): #n-ig iteráltunk
        if i != n: # ha nem járunk még n-nél
            sum += i #össegzés
            print("{}+".format(i),end="",file=out_file)
        else: # ha n-nél járunk
            sum += i #összegzés, és eredmény kiiratás
            print("{}={}".format(i,sum),end="",file=out_file)

    out_file.close()

def kiir_datum(args):
    num = int(args[0])
    file_name = args[1]

    out_file = open(file_name, "w")
    year = num // (60 * 60 * 24 * 365)
    num = num % (60 * 60 * 24 * 365)

    month = num // (60 * 60 * 24 * 30)
    num = num % (60 * 60 * 24 * 30)

    day = num // (60 * 60 * 24)
    num = num % (60 * 60 * 24)

    hour = num // (60 * 60)
    num = num % (60 * 60)

    minute = num // 60
    num = num % 60
    sec = num
    print("The current date is {}. {}. {}. {}:{}:{}".format(year,month,day,hour, minute, sec), file=out_file)
    out_file.close()

def string_sum(arg):
    sum = 0 #a stringben szereplő számok összegét itt taroljuk
    tmp = "" #itt taroljuk majd az aktuális számot a stringben
    for ch in arg: #karakterenként végigiteráljuk a stringet
        if ch.isdigit(): #ha az adott karakter szám
            tmp += ch #azt rakjuk bele a tmp-be
        elif tmp: #ha nem szám a ch, akkor megnezzuk, hogy a tmp-ben van-e elem
            sum += int(tmp) #az eddigi tmp-ben lévő számot az összeghez adjuk
            tmp = "" #ürítjük a tmp változót
    if tmp: #ha a string végén szám van, akkor a tmp nem üres
        sum += int(tmp)
    print("{} string osszege: {}".format(arg, sum))

def sum_random(args):
    n = int(args[0])
    file_name = args[1]
    sum = 0
    out_file = open(file_name,"w")
    for i in range(n):
        num = random.randint(1,100)
        sum += num
        print(num, file=out_file)
    print("Szamok osszege: {}".format(sum), file=out_file)
    out_file.close()


#1. feladat
# res_list = []
# for item in list1:
#     if item not in list2:
#         res_list.append(item)
# print(res_list)

#2. feladat
# osszead_n_ig(sys.argv[1:])

#3. feladat
# kiir_datum(sys.argv[1:])

#4. feladat
# string_sum(sys.argv[1])

#5. feladat
# sum_random(sys.argv[1:])