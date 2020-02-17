def elso_harom_betu(szo):
    if len(szo) < 3:
        return szo
    else:
        return szo[:3]

szo = input("Kerek egy szot:")
print(elso_harom_betu(szo))