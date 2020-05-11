import matplotlib.pyplot as plt
import numpy as np

in_file = open("input2.txt","r") #fajl megnyitasa
flag = False #egy jelzo beallitasa, amely jeloli, hogy elhagytuk-e az elso sort a fajlban
for line in in_file: #fajl feldolgozas soronkent
    nums = line.split() #a sor feldarabolasa egy listaba
    nums = [int(num) for num in nums] #lista elemeinek atalakitasa int tipusuva helyben
    if not flag: #ha az elso sorban vagyunk
        list1 = np.asarray(nums) #az elso listat toltjuk fel
    else:
        list2 = np.asarray(nums) # a masodik listat toltjuk fel
    flag = True #az elso sor vegen a jelzot igazra allitjuk

plt.plot(range(len(list1)),list1,'g', label = 'adatsor1')
plt.plot(range(len(list2)),list2,'r', label = 'adatsor2')
plt.plot(range(len(list1)),(list1 + list2)/2,'b', label ='adatsorok átlaga')
plt.title("Napi lebontás")
plt.xlabel("Napok")
plt.ylabel("Ft")
plt.legend()
plt.show()

in_file.close()