def number_of_lannisters(file):
    x = 0 #elofordulasok tarolasa itt tortenik meg
    for line in file:
        tmp = line.split() #felosztjuk az adott sort szavakra
        for word in tmp: #vegigiterálunk a szavakon
            if "Lannister" in word: #ha benne van a keresett szó egy szóban
                x += 1 #növeljük az előfordulások számát
    return x

try:
    my_file = open("input.txt","r")
    print("A Lannister szo {} alkalommal talalhato a fajlban!".format(number_of_lannisters(my_file)))
    my_file.close()
except FileNotFoundError:
    print("A megadott fajl nem talalhato")