#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1734

n = int(input(""))
fatorial = 1
contador = 1


while contador <= n:
  fatorial = fatorial * contador
  print(fatorial)
  contador = contador + 1
print("%i!" %(n), "= %i" %(fatorial))
