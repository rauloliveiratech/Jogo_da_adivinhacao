import random

def obter_chute_valido():
    while True:
        try:
            chute = int(input('Chute um número: '))
            return chute
        except ValueError:
            print('Entrada inválida. Insira um número válido.')

def jogar_jogo(dificuldade, max_tentativas):
    numero_secreto = dificuldade()
    tentativas_restantes = max_tentativas

    print(f'\nVocê tem {tentativas_restantes} tentativas para adivinhar o número.')

    for i in range(max_tentativas):
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
    mensagens_dificuldade = {
        1: 'Fácil',
        2: 'Médio',
        3: 'Difícil'
    }
    
    print('''
*************************
***Jogo da adivinhação***
*************************

Selecione um nível de dificuldade, digite o número correspondente :
1 - Fácil
2 - Médio
3 - Difícil
    ''')
    
    while True:
        try:
            dif = int(input())
            if dif in mensagens_dificuldade:
                print(f'\nVocê selecionou a dificuldade {mensagens_dificuldade[dif]}')
                break
            else:
                print('Opção inválida. Escolha 1 para Fácil, 2 para Médio ou 3 para Difícil.')
        except ValueError:
            print('Entrada inválida. Insira um número válido.')

    if dif == 1:
        numero_secreto = random.randint(0, 25)
        max_tentativas = 8
    elif dif == 2:
        numero_secreto = random.randint(0, 75)
        max_tentativas = 6
    elif dif == 3:
        numero_secreto = random.randint(0, 100)
        max_tentativas = 4
    return numero_secreto, max_tentativas

def jogar_novamente():
    resposta = input('Deseja jogar novamente? (s/n): ')
    return resposta.lower() == 's'

while True:
    numero_secreto, max_tentativas = dificuldade()
    jogar_jogo(numero_secreto, max_tentativas)
    if not jogar_novamente():
        break
