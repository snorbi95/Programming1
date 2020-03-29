import string

def count_words(my_file):
    dict = {}
    for line in my_file:
        new_line = ""
        for ch in line:
            if ch not in string.punctuation:
                new_line += ch
        words = new_line.split()
        for word in words:
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1
    return dict

my_file = open("input.txt","r")
dict = count_words(my_file)
for key,value in dict.items():
    print("{} elofordulasainak szama: {}".format(key,value))
my_file.close()