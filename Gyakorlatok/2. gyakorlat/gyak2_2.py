try:
    file = open("input.txt","r")
    for line in file:
        print(line, end = "")
except FileNotFoundError:
    print("A megadott fajl nem talalhato")
finally:
    file.close()
