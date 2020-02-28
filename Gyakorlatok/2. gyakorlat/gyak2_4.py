def betu_csere():
    my_file = open("input.txt","r")
    out_file = open("output.txt","w")
    for line in my_file:
        new_str = ""
        for ch in line: #a sort karakterenként dolgozzuk fel
            if ch.islower(): #karakterek megforditasa
                new_str += ch.upper()
            elif ch.isupper():
                new_str += ch.lower()
            else: #ha nem betű karakterről van szó
                new_str += ch
        print(new_str,file=out_file,end = "")
    my_file.close()
    out_file.close()

try:
    betu_csere()
except FileNotFoundError:
    print("Fajl nem talalhato")
