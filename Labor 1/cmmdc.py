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
    lista = [4, 5, 6, 7, 8]
    print(cmmmc(1, 3, lista))

main()
