import string

def find_longest_words(my_file):
    out_file = open("longestWords.txt","w")
    max_hossz = 0
    lhosszabb_szavak = []
    jelek = [",.!-"]
    for line in my_file:
        new_str = ""
        for ch in line:
            if ch not in string.punctuation:
                new_str += ch
        tmp = new_str.split()
        for word in tmp:
            if len(word) > max_hossz:
                lhosszabb_szavak = []
                max_hossz = len(word)
                lhosszabb_szavak.append(word)
            elif len(word) == max_hossz:
                lhosszabb_szavak.append(word)

    print("A leghosszab szo {} karakterbol all.".format(max_hossz),file=out_file)
    for szavak in lhosszabb_szavak:
        print(szavak,file=out_file)

    out_file.close()

try:
    my_file = open("input.txt","r")
    find_longest_words(my_file)
    my_file.close()
except FileNotFoundError:
    print("hiba")