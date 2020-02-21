while True:
    try:
        x = input("Kerek egy szamot:")
        x = int(x)
        print(x)
        break
    except ValueError:
        print("A megadott érték nem szám!")