def leiaInt(msg):
    while True:
        try:
            i = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;3;31mERRO: Por favor, digite um número inteiro válido.\033[0;0;0m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[1;3;33mUsuário preferiu não digitar esse número.\033[0;0;0m\n')
            return 0
        else:
            return i

def leiaFloat(msg):
    while True:
        try:
            r = float(input(msg))
        except (TypeError, ValueError):
            print('\033[1;3;31mERRO: Por favor, digite um número real válido.\033[0;0;0m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[1;3;33mUsuário preferiu não digitar esse número.\033[0;0;0m\n')
            return 0
        else:
            return r

li = leiaInt('Digite um número inteiro: ')
lr = leiaFloat('Digite um número real: ')

print(f'\033[1;3;34mO valor inteiro foi {li} e o real foi {lr}.\033[0;0;0m')