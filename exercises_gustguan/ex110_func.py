def aumentar(preco = 0, taxa = 0, formato = False):
    res = preco + (preco * taxa / 100)
    return res if formato is False else moeda(res)

def diminuir(preco = 0, taxa = 0, formato = False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)

def dobro(preco = 0, formato = False):
    res = preco * 2
    return res if not formato else moeda(res)

def metade(preco = 0, formato = False):
    res = preco / 2
    return res if not formato else moeda(res)

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

def resumo(preco = 0, taxa = 0, formato = False):
    print('-' * 33)
    print('RESUMO DO VALOR'.center(33))
    print('-' * 33)

    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxa:.0f}% de aumento: \t{aumentar(preco, taxa, True)}')
    print(f'{taxa:.0f}% de redução: \t{diminuir(preco, taxa, True)}')
    print('-' * 33)
