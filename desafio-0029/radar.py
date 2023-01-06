print('*** RADAR ***')

velocidade = float(input('Insira a velocidade:'))

if velocidade > 80:
  multa = (velocidade - 80) * 7
  print(f'Você foi multado ! Valor da MULTA ! {multa:7.2f}!')
if velocidade < 80:
  print('Você está na velocidade está correta !')    