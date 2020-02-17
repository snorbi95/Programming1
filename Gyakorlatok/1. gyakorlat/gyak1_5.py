def rendezett_szavak(lst):
    eredmeny_lst = list()
    for szo in lst:
        if szo not in eredmeny_lst:
            eredmeny_lst.append(szo)
    eredmeny_lst.sort()
    return eredmeny_lst

szavak = input("Kerem a szavakat:")
lst = list(szavak.split(", "))
print(rendezett_szavak(lst))