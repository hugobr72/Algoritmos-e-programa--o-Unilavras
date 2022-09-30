#https://www.beecrowd.com.br/judge/pt/custom-runs/code/395642

nome = str(input(''))
hora_extras = float(input(''))

salario_minimo = 1192.40
valor_hora = 10
salario_hora_extra = hora_extras * valor_hora
salario_bruto = salario_hora_extra + (3 * salario_minimo)

if salario_bruto > 2000:
    inss = salario_bruto * 0.12 
else:
    inss = salario_bruto * 0.05
    
if salario_bruto > 2500:
    imposto_renda = salario_bruto * 0.20
else:
    imposto_renda = 0

descontos = inss + imposto_renda
salario_liquido = salario_bruto - descontos

print("Nome: %s" %(nome));
print("Salário bruto: R$%.2f" %(salario_bruto))
print("Salário líquido: R$%.2f" %(salario_liquido))
