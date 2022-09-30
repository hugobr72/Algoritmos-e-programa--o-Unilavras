#https://www.beecrowd.com.br/judge/pt/custom-runs/code/395633

valor = int(input(''))

fatorial = 1
cont = valor
if valor > 0:
    while cont > 1:
        fatorial *= cont
        cont -= 1
else:
    fatorial = 0

print('%i! = %i' %(valor, fatorial))