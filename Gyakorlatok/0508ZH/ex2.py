import sys #sys konyvtar importalas

n = sys.argv[1] #argumentumok valtozohoz rendelese
file_name = sys.argv[2]

in_file = open("input.txt","r") #bemeneti faj megnyitasa
out_file = open(file_name,"w") #kimeneti fajl megnyitas (parameter az argumentum valtozoba mentve)

def count(num): #szamjegyek osszege
    sum = 0 #summa definialas
    while num != 0: #amig a num nem 0
        sum += num % 10 #maradekos osztas eredmenye hozzaadasa
        num = num // 10 #egesz osztassal leosztjuk a szamot
    return sum #osszeg visszateritese

for line in in_file: #fajl feldolgozasa soronként
    nums = line.split(";") #sorok feldarabolasa a valasztojel szerint
    for num in nums: #a letrejott lista elemein iteralas
        if (count(int(num)) + int(n)) % 10 == 0: # ha teljesul a feltetel (szamjegyek osszeget a fv. generalja)
            print(num,file=out_file) #kiiratas a fajlba


in_file.close() #fajlbezaras!!!
out_file.close()