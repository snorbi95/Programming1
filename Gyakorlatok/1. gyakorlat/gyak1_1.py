def main():
    n = int(input("Kerek egy szamot:"))
    while n != 0:
        if n % 2 == 0:
            print("Páros!")
        else:
            print("Páratlan!")
        n = int(input("Kerek egy szamot:"))

main()

# while True:
#     n = int(input())
#     if n != 'end':
#         break