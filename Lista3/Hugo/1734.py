n = int(input(""))
fatorial = 1
contador = 1


while contador <= n:
  fatorial = fatorial * contador
  print(fatorial)
  contador = contador + 1
print("%i!" %(n), "= %i" %(fatorial))
#https://www.beecrowd.com.br/judge/pt/custom-runs/code/395528