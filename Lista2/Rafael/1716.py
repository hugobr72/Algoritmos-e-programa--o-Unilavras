#https://www.beecrowd.com.br/judge/pt/custom-runs/code/392796

plano = str(input(''))
salario = float(input(''))

if plano == 'A':
    salario *= 110/100
    print('Novo salário: R$%.2f' %(salario))
elif plano == 'B':
    salario *= 115/100
    print('Novo salário: R$%.2f' %(salario))
elif plano == 'C':
    salario *= 120/100
    print('Novo salário: R$%.2f' %(salario))
