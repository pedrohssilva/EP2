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
