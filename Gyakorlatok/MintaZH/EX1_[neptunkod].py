

def beszur(szo):
    mgh = 'aeiou'
    count = 1
    new_str = ''
    for ch in szo:
        if ch in mgh:
            new_str += ch + str(count)
        else:
            new_str += ch
        count += 1
    return new_str

lista = []
while True:
    szo = input("Kerek egy szot: ")
    if szo == 'end':
        break
    lista.append(beszur(szo))

print("Modositott stringek: {}".format(lista))