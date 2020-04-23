import ex107_func

p = float(input('Digite um valor: R$'))
t = float(input('Digite a taxa: %'))

print(f'O valor R${p:.2f} aumentado em {t}% é R${ex107_func.aumentar(p, t):.2f}')
print(f'O valor R${p:.2f} diminuído em {t}% é R${ex107_func.diminuir(p, t):.2f}')
print(f'O dobro de R${p:.2f} é R${ex107_func.dobro(p):.2f}')
print(f'A metade de R${p:.2f} é R${ex107_func.metade(p):.2f}')
