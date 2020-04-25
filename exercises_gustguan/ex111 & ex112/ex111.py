import moeda
import dado

p = dado.leiaDinheiro('Digite o preço: R$')
t = float(input('Digite a taxa: %'))

moeda.resumo(p, t)