peso90 = 0
soma = 0
media = 0

for c in range(0,4):
    idade = int(input(''))
    peso = float(input(''))
    if peso > 90:
        peso90 += 1
    soma += idade
    c +=1
media = soma/4
print('Qtd pessoas > 90 Kg: %i'%peso90)
print('Idade média: %.2f' %media)
#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1760