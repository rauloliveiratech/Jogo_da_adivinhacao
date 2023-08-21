import random

def obter_chute_valido():
    while True:
        try:
            chute = int(input('Chute um número: '))
            return chute
        except ValueError:
            print('Entrada inválida. Insira um número válido.')

def jogar_jogo(dificuldade):
    numero_secreto = dificuldade()
    tentativas_restantes = 5

    print(f'\nVocê tem {tentativas_restantes} tentativas para adivinhar o número.')

    for i in range(5):
        chute = obter_chute_valido()

        if chute < numero_secreto:
            print('O número secreto é maior')
        elif chute > numero_secreto:
            print('O número secreto é menor')
        else:
            print(f'Parabéns! Você acertou em {i + 1} tentativa(s)!')
            break

        tentativas_restantes -= 1
        if tentativas_restantes > 0:
            print(f'Tentativas restantes: {tentativas_restantes}')
        else:
            print('Suas tentativas esgotaram, você perdeu!')
            print(f'O número secreto era: {numero_secreto}')

def dificuldade():
    print('''
*************************
***Jogo da adivinhação***
*************************

Selecione um nível de dificuldade, digite o número correspondente :
1 - Fácil
2 - Médio
3 - Difícil
    ''')
    
    dif = int(input())
    
    if dif == 1:
        numero_secreto = random.randint(0, 25)
        print('\nEscolha um número de 1 a 25')
    elif dif == 2:
        numero_secreto = random.randint(0, 75)
        print('\nEscolha um número de 1 a 75')
    elif dif == 3:
        numero_secreto = random.randint(0, 100)
        print('\nEscolha um número de 1 a 100')
    return numero_secreto

jogar_jogo(dificuldade)
