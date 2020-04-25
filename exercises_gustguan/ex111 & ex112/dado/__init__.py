def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[3;31;47mERRO: \"{entrada}\" é um valor inválido!\033[0;0;0m')
        else:
            valido = True
            return float(entrada)