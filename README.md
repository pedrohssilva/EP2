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
