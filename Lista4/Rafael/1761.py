total = 0


while True:
    valorCompra = float(input())
    total += valorCompra
    if valorCompra == 0:
        valorPago = float(input(''))
        break
print('Total da compra: R$%.2f' %total)
print('Valor pago: R$%.2f'%valorPago)
troco = valorPago - total
print('Troco: R$%.2f'%troco)
#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1761