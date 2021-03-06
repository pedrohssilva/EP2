# EP2
# DesSoft
import random

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
    naipes = ["♦", "♥", "♣", "♠"]
    for naipe in naipes:
        if naipe in carta:
            return naipe
    
def extrai_valor(carta):
    
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    for valor in valores:
        if valor in carta:
            return valor
        
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

def colorindo_baralho(i):
    if extrai_naipe(i) == '♥':
        return (('\033[1;34m{0}\033[m').format(i))
    elif extrai_naipe(i) == '♦':
        return (('\033[1;31m{0}\033[m').format(i))
    elif extrai_naipe(i) == '♠':
        return (('\033[1;35m{0}\033[m').format(i))
    elif extrai_naipe(i) == '♣':
        return (('\033[1;92m{0}\033[m').format(i))


print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('Paciência Acordeão')
print('==================') 
print('')
print('Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha.')
print('')
print('Existem apenas dois movimentos possíveis:') 
print('')
print('1. Empilhar uma carta sobre a carta imediatamente anterior;') 
print('2. Empilhar uma carta sobre a terceira carta anterior. ')
print('')
print('Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida: ')
print('')
print('1. As duas cartas possuem o mesmo valor ou') 
print('2. As duas cartas possuem o mesmo naipe.')
print('')
print('Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada. ')
print('')
a = input('Aperte [Enter] para iniciar o jogo...')

cartas = cria_baralho()
random.shuffle(cartas)
numero_cartas = len(cartas)
print('')
print('O estado atual do baralho é:')
i = 0
for numero in range(1, numero_cartas+1):
    print("{0}. {1}". format(numero, colorindo_baralho(cartas[i])))
    i += 1
print('')

quer_jogar = True
while quer_jogar:
    while numero_cartas>1:
        escolheu_certo = True
        while escolheu_certo:
            numero_cartas = len(cartas)
            carta_escolhida = input('Escolha uma carta (digite um número entre 1 e {0}): '.format(numero_cartas))
            
            while carta_escolhida.isnumeric() == False or int(carta_escolhida) > numero_cartas or int(carta_escolhida) < 1:
                carta_escolhida = input('Você digitou um termo inválido. Escolha uma carta (digite um número entre 1 e {0}): '.format(numero_cartas))

            carta_escolhida = int(carta_escolhida)
            

            tem_movimento = lista_movimentos_possiveis(cartas, carta_escolhida-1)

            if len(tem_movimento) == 1:
                if tem_movimento[0] == 1:
                    empilha(cartas, carta_escolhida-1, carta_escolhida-2)
                if tem_movimento[0] == 3:
                    empilha(cartas, carta_escolhida-1, carta_escolhida-4)
                escolheu_certo = False

            if len(tem_movimento) == 0:
                print('A carta {0} não pode ser movida. Por favor, digite um número entre 1 e {1}'.format(colorindo_baralho(cartas[carta_escolhida-1]), numero_cartas))  
            
            if len(tem_movimento) == 2:
                print('1. {0}'. format(colorindo_baralho(cartas[carta_escolhida-4])))
                print('2. {0}'. format(colorindo_baralho(cartas[carta_escolhida-2])))
                carta_baixo = int(input('Sobre qual carta você quer empilhar o {0}? '.format(colorindo_baralho(cartas[carta_escolhida-1]))))
                if carta_baixo == 1:
                    empilha(cartas, carta_escolhida-1, carta_escolhida - 4)
                    escolheu_certo = False
                if carta_baixo == 2:
                    empilha(cartas, carta_escolhida-1, carta_escolhida - 2)
                    escolheu_certo = False

        numero_cartas = len(cartas)
        
        movimento = possui_movimentos_possiveis(cartas)
        if movimento == False:
            print('Você perdeu!')
            numero_cartas -= 1000
        
        if movimento == True:
            print('')
            print('O estado atual do baralho é:')
            i = 0
            for numero in range(1, numero_cartas+1):
                print("{0}. {1}". format(numero, colorindo_baralho(cartas[i])))
                i += 1 
            
    if numero_cartas == 1:    
        print('Parabéns você ganhou!')

    print('')
    jogar_novamente = input('Se quiser jogar novamente, digite sim: ')

    if jogar_novamente == 'sim':

        quer_jogar = True
        escolheu_certo = False

        cartas = cria_baralho()
        random.shuffle(cartas)
        numero_cartas = len(cartas)
        print('')
        print('O estado atual do baralho é:')
        i = 0
        for numero in range(1, numero_cartas+1):
            print("{0}. {1}". format(numero, colorindo_baralho(cartas[i])))
            i += 1
        print('')

    else:
        quer_jogar = False