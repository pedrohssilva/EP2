# EP2
DesSoft

def cria_baralho():
    lista = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cartas = []
    for elemento in lista:
        a = elemento + "♠"
        cartas.append(a)

        b = elemento + "♦"
        cartas.append(b)

        c = elemento + "♣"
        cartas.append(c)

        d = elemento + "♥"
        cartas.append(d)

    return (cartas)

def extrai_naipe(carta):

    if "♦" in carta:
        return "♦"
    
    if "♥" in carta:
        return "♥"
    
    if "♣" in carta:
        return "♣"
    
    if "♠" in carta:
        return "♠"
    
def extrai_valor(carta):
        
    if "A" in carta:
        return "A"
    
    if "2" in carta:
        return "2"
    
    if "3" in carta:
        return "3"
    
    if "4" in carta:
        return "4"

    if "5" in carta:
        return "5"
    
    if "6" in carta:
        return "6"

    if "7" in carta:
        return "7"

    if "8" in carta:
        return "8"

    if "9" in carta:
        return "9"

    if "10" in carta:
        return "10"

    if "J" in carta:
        return "J"

    if "Q" in carta:
        return "Q"

    if "K" in carta:
        return "K"
    
def lista_movimentos_possiveis (baralho, indice):

    possiveis_movimentos = []

    if indice == 0:
        return []

    naipe = extrai_naipe(baralho[indice])

    if (indice-1) >= 0:
        naipe1 = extrai_naipe(baralho[indice-1])
        if naipe == naipe1:
            possiveis_movimentos.append(1)

    if (indice-3) >= 0:
        naipe3 = extrai_naipe(baralho[indice-3])
        if naipe == naipe3:
            possiveis_movimentos.append(3)

    numero = extrai_valor(baralho[indice])
    
    if (indice-1) >= 0:
        numero1 = extrai_valor(baralho[indice-1])
        if numero == numero1:
            possiveis_movimentos.append(1)
    
    if (indice-3) >= 0:
        numero3 = extrai_valor(baralho[indice-3])
        if numero == numero3:
            possiveis_movimentos.append(3)
    
    return possiveis_movimentos

def empilha(lista_cartas, origem, destino):

    carta_muda = lista_cartas[origem]

    del lista_cartas[origem]

    lista_cartas[destino] = carta_muda

    return lista_cartas

def possui_movimentos_possiveis(lista_cartas):
    numero_cartas = len(lista_cartas)

    for indice in range(numero_cartas):
        print(indice)
        possiveis_movimentos = lista_movimentos_possiveis(lista_cartas, indice)

        if len(possiveis_movimentos) != 0:
            return True
    else:
        return False
