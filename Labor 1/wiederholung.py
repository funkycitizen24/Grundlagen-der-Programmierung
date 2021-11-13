def wiederholung(lista):
    lista1 = []
    for i in lista:
        if i not in lista1:
            lista1.append(i)
    return lista1

def main():
    lista= [11, 10, 11, 33, 33, 33, 33, 11, 10]
    print(wiederholung(lista))

main()
