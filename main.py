import random

print('*************************')
print('***Jogo da adivinhacao***')
print('*************************')

print('\nEscolha um número de 1 a 100\nVocê tem 5 tentativas')
numero_secreto = random.randint(0,100+1)

for i in range (0,5):
    chute = int(input('Chute um número: '))
    if chute < numero_secreto:
        print('\nO numero secreto é maior')
    elif chute > numero_secreto:
        print('\nO numero secreto é menor')
    elif chute == numero_secreto:
        print(' Você acertou !')
        break
print('\nSuas tentativas esgotaram, você perdeu !')
print ('O número secreto é', numero_secreto)