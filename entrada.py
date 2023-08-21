def obter_chute_valido():
    while True:
        try:
            chute = int(input('Chute um número: '))
            return chute
        except ValueError:
            print('Entrada inválida. Insira um número válido.')
