import ex108_func

p = float(input('Digite um valor: R$'))
t = float(input('Digite a taxa: %'))

print(f'O valor R${ex108_func.moeda(p)} aumentado em {t}% é R${ex108_func.moeda(ex108_func.aumentar(p, t))}')
print(f'O valor R${ex108_func.moeda(p)} diminuído em {t}% é R${ex108_func.moeda(ex108_func.diminuir(p, t))}')
print(f'O dobro de R${ex108_func.moeda(p)} é R${ex108_func.moeda(ex108_func.dobro(p))}')
print(f'A metade de R${ex108_func.moeda(p)} é R${ex108_func.moeda(ex108_func.metade(p))}')
