def domino(lista):
    num = 0
    max = 0
    anzahl = 0
    for i in range(0, len(lista)-1):
            a = lista[i]%10
            b = lista[i+1]/10
            if a == b:
                num = num + 1
            else:
                if num > max:               #num ist der anzahl der elementen in der groessten teilfolge
                    max = num
                    anzahl = i - num        #hier beginnt die groesste teilfolge
                    num = 0                 #wir suchen eine andere teifolge
                else:
                    num = 0

def main():
