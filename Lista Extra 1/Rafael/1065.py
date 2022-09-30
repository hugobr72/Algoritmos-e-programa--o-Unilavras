#https://www.beecrowd.com.br/judge/pt/runs/code/30082929

cont = 0
for c in range(0,5):
    valor = int(input())
    if valor % 2 == 0:
        cont += 1
print('{} valores pares'.format(cont))
