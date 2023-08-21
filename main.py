from jogo import jogar_jogo
import random
import entrada



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
        print('\n O número está entre 1 e 25')
    elif dif == 2:
        numero_secreto = random.randint(0, 75)
        max_tentativas = 6
        print('\n O número está entre 1 e 75')
    elif dif == 3:
        numero_secreto = random.randint(0, 100)
        max_tentativas = 4
        print('\n O número está entre 1 e 100')
    return numero_secreto, max_tentativas

def jogar_novamente():
    resposta = input('Deseja jogar novamente? (s/n): ')
    return resposta.lower() == 's'

if __name__ == "__main__":
    while True:
        numero_secreto, max_tentativas = dificuldade()
        jogar_jogo(numero_secreto, max_tentativas)
        if not jogar_novamente():
            break
