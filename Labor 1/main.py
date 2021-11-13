"""
1. DEF WDH EnfernenSie die Zahlen die sich wiederholen
"""
def wiederholung(lista):
    lista = [11, 10, 11, 33, 33, 33, 33, 11, 10]
    lista1 = []
    for i in lista:
        if i not in lista1:
            lista1.append(i)
    return lista1

"""
2. DEF SYMM Schreiben Sie die Anzahl vonsymmetrischenPaaren(xy)und (yx)
"""
def symm(lista):

    ct = 0
    print("Die Paaren sind:")

    for i in range(len(lista) - 1):
        a = lista[i]
        b = lista[i + 1]
        pca = a // 10                          #Erste Ziffer a
        uca = a - (a // 10 * 10)               #Letzte Ziffer a
        pcb = b // 10                          #Erste Z b
        ucb = b - (b // 10 * 10)               #Letzte Z b

        if (pca == ucb) and (pcb == uca):      #Falls erste a = letzte b und andersrum
                print(a, b)
                ct = ct + 1

    print("Die Anzahl der symm Paaren ist:")

    return ct

"""
3. DEF KONKAT Generieren Sie die größtemöglicheZahl, die aus der Konkatenationder Elemente der Liste gebildet ist.
"""
def konkat(lista):

    lista1 = []
    for i in range(len(lista)):                  #Wir machen eine Kopie pas cu pas
        lista1.append(lista[i])

    for k in range(len(lista)):
        for i in range(len(lista) - 1):
            j = i + 1
            if lista1[i] < lista1[j]:            #Wir sortieren die liste von grosste Zahl zu der kleinsten
                a = lista1[j]
                lista1[j] = lista1[i]
                lista1[i] = a

    b = 0
    for i in range(len(lista1)):
        b = b * 100 + lista1[i]                 #Die Liste wird in einer Zahl konkateniert

    print("Die grosste Zahl ist:")
    return b

"""
4. DEF VERSCH Verschlüsseln  Sie  die  Elemente  der  Liste,  indem  Sie dasersteElement  
als  Schlüssel benützen und ie Methode selbst wählen(+, *, XOR)
"""
def schlussel(lista):

    lista1 = []
    for i in range(len(lista)):                  #Kopie
        lista1.append(lista[i])

    a = lista1[0]

    print("Geben sie eine Zahl zwischen 1 und 4 ")
    print("1=Addition, 2=Subtraktion, 3=Multiplikation, 4=Division.")

    x = int(input("x = "))

    if x == 1:
        for i in range(1, len(lista1)):
            lista1[i] = lista1[i] + a
    if x == 2:
        for i in range(1, len(lista1)):
            lista1[i] = lista1[i] - a
    if x == 3:
        for i in range(1, len(lista1)):
            lista1[i] = lista1[i] * a

    if x == 4:
        for i in range(1, len(lista1)):
            lista1[i] = lista1[i] // a


    return lista1

"""
5. Filtern Sie die Zahlen, die eine bestimmte Beziehung zwischen Zahlen haben, 
die in einem String angegeben wird.(z.B:“x=y*3”, “x/y=2“, ...)
"""
def filtern(lista):

    print("Die Zahlen, der Form x/y=2, sind:")
    ct = 0
    for i in range(len(lista)):
        a = lista[i]
        pca = a // 10
        uca = a - (a // 10 * 10)
        if pca // uca == 2:
            print(a)
            ct = ct + 1

    print("Die Anzahl dieser Zahlen ist:")
    return ct

"""
6.domino teilfolge
"""
def domino(lista):

    lista1 = []

    for i in range(len(lista) - 1):
        j = i + 1
        a = lista[i]
        b = lista[j]
        uca = a - (a // 10 * 10)
        pcb = b // 10

        if uca == pcb:                          #Wir uberprufen ob die letzte Ziffer einer Zahl
                                                #gleich ist mit der ersten Ziffer der nachsten ist
            print(lista[i])
            print(lista[j])
            lista1.append(i)

    return lista1

"""
7. Finden Sie den kleinsten gemeinsamen Vielfachen zwischen Index from und to, welche gegeben sind.
"""
def cmmdc(a,b, lista):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
def cmmmc(a, b, lista):
    d = cmmdc(a, b, lista)
    print('cmmmc este: ')
    return lista[a]*lista[b]//d

def main():
    lista = [85, 58, 23, 32, 23, 31, 18, 85, 18, 81, 23, 33, 22, 85, 53, 33, 32, 23, 17, 63, 84, 42]
    print("Die Liste ist:")
    print(lista)
    print("Wahlen Sie eine Ubung von 1 zu 7")
    x = int(input("x = "))

    if x == 1:
        print(wiederholung(lista))

    if x == 2:
        print(symm(lista))

    if x == 3:
        print(konkat(lista))

    if x == 4:
        print(schlussel(lista))

    if x == 5:
        print(filtern(lista))

    if x == 6:
        print(domino(lista))

    if x == 7:
        print(cmmmc(2,4,lista))

main()
