def number_of_lannisters(file):
    x = 0
    for line in file:
        tmp = line.split()
        for word in tmp:
            if "Lannister" in word:
                x += 1
    return x

try:
    my_file = open("input.txt","r")
    print("A Lannister szo {} alkalommal talalhato a fajlban!".format(number_of_lannisters(my_file)))
    my_file.close()
except FileNotFoundError:
    print("A megadott fajl nem talalhato")