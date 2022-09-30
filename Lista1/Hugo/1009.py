#https://www.beecrowd.com.br/judge/pt/problems/view/1009

nome = str(input(''))
salarioFixo = float(input(''))
vendas = float(input(''))
bonus = vendas * 0.15
total = salarioFixo + bonus
print('TOTAL = R$ %.2f'%(total))
