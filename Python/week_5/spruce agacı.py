def create_spruce():
    yukseklik = int(input("Spruce height: "))
    kutu = int(input("Box size: "))

    if kutu < yukseklik * 2 - 1:
        print("Box size is too small!")
        return

    print("-" * kutu)
    print("|" + " " * (kutu - 2) + "|")

    for i in range(yukseklik):
        yildiz = 1 + 2 * i
        bosluk = (kutu - 2 - yildiz) // 2
        print("|" + " " * bosluk + "*" * yildiz + " " * bosluk + "|")

    bosluk = (kutu - 3) // 2
    print("|" + " " * bosluk + "*" + " " * bosluk + "|")

    print("-" * kutu)

create_spruce()
