#https://www.beecrowd.com.br/judge/pt/custom-runs/code/392811

cliente = int(input())
valor_cliente = float(input())

if cliente == 1:
    valor_cliente = valor_cliente
    print('Valor total a ser pago: R$%.2f' %(valor_cliente))
elif cliente == 2:
    valor_cliente = valor_cliente * 0.87
    print('Valor total a ser pago: R$%.2f' %(valor_cliente))
elif cliente == 3:
    valor_cliente = valor_cliente * 0.93
    print('Valor total a ser pago: R$%.2f' %(valor_cliente))
else:
    print('OPÇÃO INVÁLIDA!')
