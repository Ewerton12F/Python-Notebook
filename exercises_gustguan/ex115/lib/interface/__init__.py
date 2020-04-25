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
            
def linha(tam = 40):
    return '-' * 40

def titulo(txt):
    print(linha())
    print(txt.upper().center(40))
    print(linha())

def menu():
    titulo('menu principal')
    global L
    L = [1, 2, 3]
    count = 0
    global lista
    lista = ['Cadastrar uma pessoa', 'Ver pessoas cadastradas', 'Sair do sistema']

    for y in lista:
        print(f'\033[1;3;33m{L[count]}\033[0;0;0m - \033[1;3;34m{y}\033[0;0;0m')
        count += 1
    print(linha())

def opc(x):
    menu()
    while True:
        x = leiaInt('\033[3;33mSua opção:\033[0;0m ')
        if x == L[0]:
            titulo('opção 1')
            menu()
        elif x == L[1]:
            titulo('opção 2')
            menu()
        elif x == L[2]:
            titulo('Saindo do sistema... Até logo!')
            break
        else:
            print(f'\033[1;3;31m{x} não encontrado nas opções.\033[0;0;0m')
            