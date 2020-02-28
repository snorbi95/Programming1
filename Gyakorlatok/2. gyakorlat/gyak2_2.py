try:
    file = open("input.txt","r") #fajl megnyitas
    for line in file: # soronként végighaladunk a fájlon
        print(line, end = "") #kiiras
except FileNotFoundError:
    print("A megadott fajl nem talalhato")
finally:
    file.close()
