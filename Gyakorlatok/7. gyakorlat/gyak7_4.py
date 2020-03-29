
def dobokocka_szotar():
    dict = {}
    for i in range(1,7):
        for j in range(1,7):
            if (i + j) not in dict:
                dict[i + j] = [(i,j)]
            else:
                dict[i + j].append((i,j))
    return dict

dict = dobokocka_szotar()
length = 0
for key,value in dict.items():
    length += len(value)
    print("A {} osszeg elerheto: {}"\
          .format(key,value))
print(length)