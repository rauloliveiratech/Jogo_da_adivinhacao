import random

print('*************************')
print('***Jogo da adivinhação***')
print('*************************')

print('\nEscolha um número de 1 a 100\nVocê tem 5 tentativas')
numero_secreto = random.randint(0, 100)

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
