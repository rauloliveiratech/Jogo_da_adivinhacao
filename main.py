import random

def dificuldade(dif):
    if dif == 1:
        numero_secreto = random.randint(0, 25)
        print('\nEscolha um número de 1 a 25\nVocê tem 5 tentativas')
    elif dif == 2:
        numero_secreto = random.randint(0, 75)
        print('\nEscolha um número de 1 a 75\nVocê tem 5 tentativas')
    elif dif == 3:
        numero_secreto = random.randint(0, 100)
        print('\nEscolha um número de 1 a 100\nVocê tem 5 tentativas')
    return numero_secreto

print('''
*************************
***Jogo da adivinhação***
*************************

Selecione um nível de dificuldade, digite o número correspondente :
1 - Fácil
2 - Médio
3 - Dificil
      
''')
dificuldade_selecionada = int(input())
numero_secreto = dificuldade(dificuldade_selecionada)

try:
    for i in range(5):
        while True:
            try:
                chute = int(input('Chute um número: '))
                break  # Se a conversão para int funcionar, saia do loop de entrada
            except ValueError:
                print('Entrada inválida. Insira um número válido.')

        if chute < numero_secreto:
            print('\nO número secreto é maior')
        elif chute > numero_secreto:
            print('\nO número secreto é menor')
        else:
            print('Você acertou!')
            break
    else:
        print('\nSuas tentativas esgotaram, você perdeu!')

except ValueError:
    print('\nO valor recebido não é válido')

print('\nO número secreto era:', numero_secreto)
