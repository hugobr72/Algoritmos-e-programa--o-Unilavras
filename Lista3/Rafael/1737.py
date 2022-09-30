#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1737

somaNum = 0

qtdNum = int(input())

if qtdNum <= 0:
   print('Informe uma quantidade > 0!')
   
else:
    while qtdNum > 0:
         digN = float(input())
         somaNum = somaNum + digN
    
         qtdNum = qtdNum - 1

    print('Soma dos números informados: %.2f' %(somaNum))