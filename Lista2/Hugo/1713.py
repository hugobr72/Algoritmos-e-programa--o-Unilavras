#https://www.beecrowd.com.br/judge/pt/custom-runs/code/391877

ganhoPorHora = float(input())
horas = float(input())
salarioBruto = ganhoPorHora * horas
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
impostoRenda = salarioBruto * 0.11
salarioLiquido = salarioBruto - (inss  + sindicato + impostoRenda)
print('Salário bruto: %.2f' %(salarioBruto))
print('Imposto: %.2f' %(impostoRenda))
print('INSS: %.2f' %(inss))
print('Sindicato: %.2f' %(sindicato))
print('Líquido: %.2f' %(salarioLiquido))
