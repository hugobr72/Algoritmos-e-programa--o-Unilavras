#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1759

anoAtual = int(input())
valInicial = 1015
valorSomado = 1015
contadorPorc = 0.015
somaPorc = 0.01

anos = anoAtual - 2006

if anoAtual < 2006:
    print("O ano informado deverá ser > 2005!")

elif anoAtual == 2006:
    print("Salário atual: R$%.2f" %(valInicial))

elif anoAtual > 2006:
    porcentagem = (0.015 + 0.01)
    Anterior = valInicial

    for x in range(anos):
        calculo = Anterior + (Anterior * porcentagem)
        Anterior = calculo
        porcentagem += 0.01
        
    print("Salário atual: R$%.2f"%(calculo))