# Kanadi++
# Oficjalny moduł klasy IIe
def decToBin(liczba):
    int(liczba)
    b = []
    while liczba > 0:
        a = liczba%2
        b.append(a)
        liczba = liczba//2
    c = ""
    for n in reversed(b):
        c += str(n)
    return c
def decToHex(liczba):
    int(liczba)
    b = []
    while liczba > 0:
        a = liczba%16
        if a == 10:
            a = "A"
        if a == 11:
            a = "B"
        if a == 12:
            a = "C"
        if a == 13:
            a = "D"
        if a == 14:
            a = "E"
        if a == 15:
            a = "F"
        b.append(a)
        liczba = liczba//16
    c = ""
    for n in reversed(b):
        c += str(n)
    return c
