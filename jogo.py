from entrada import obter_chute_valido

def jogar_jogo(numero_secreto, max_tentativas):
    tentativas_restantes = max_tentativas

    print(f'\nVocê tem {tentativas_restantes} tentativas para adivinhar o número.')

    for i in range(max_tentativas):
        chute = obter_chute_valido()

        if chute < numero_secreto:
            print('O número secreto é maior')
        elif chute > numero_secreto:
            print('O número secreto é menor')
        else:
            print(f'*********** Parabéns! Você acertou em {i + 1} tentativa(s)! ***********')
            break

        tentativas_restantes -= 1
        if tentativas_restantes > 0:
            print(f'Tentativas restantes: {tentativas_restantes}')
        else:
            print('Suas tentativas esgotaram, você perdeu!')
            print(f'O número secreto era: {numero_secreto}')
