import ex109_func

p = float(input('Digite um valor: R$'))
t = float(input('Digite a taxa: %'))

print(f'O valor R${ex109_func.moeda(p)} aumentado em {t}% é R${ex109_func.aumentar(p, t, True)}')
print(f'O valor R${ex109_func.moeda(p)} diminuído em {t}% é R${ex109_func.diminuir(p, t, True)}')
print(f'O dobro de R${ex109_func.moeda(p)} é R${ex109_func.dobro(p, True)}')
print(f'A metade de R${ex109_func.moeda(p)} é R${ex109_func.metade(p,True)}')
