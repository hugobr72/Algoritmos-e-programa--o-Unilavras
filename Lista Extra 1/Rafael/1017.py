#https://www.beecrowd.com.br/judge/pt/runs/code/30082842

tempoGasto = int(input())
velocidadeMedia = int(input())
distancia = tempoGasto * velocidadeMedia
gasolinaGasta = distancia / 12
print('%.3f' % gasolinaGasta)

