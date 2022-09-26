anoFim = int(input(''))

salarioInicio = 1000
salario = salarioInicio 
porcentual = 1.015
if anoFim > 2005:
    for c in range(2005,anoFim):
        c +=1
        if c == 2006:
            salario = salario * 1.015
        else:
            porcentual = porcentual + 0.01
            salario = salario * porcentual
    print('Salário atual: R$%.2f' %salario)
else:
    print('O ano informado deverá ser > 2005!')