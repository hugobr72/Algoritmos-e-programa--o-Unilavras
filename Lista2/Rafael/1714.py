#https://www.beecrowd.com.br/judge/pt/custom-runs/code/392780

Valor_Produto = float(input(''))

if Valor_Produto < 20:
    venda = Valor_Produto * 145/100
else:
    venda = Valor_Produto * 130/100
    
print('Valor de venda: R$%.2f' %(venda))
