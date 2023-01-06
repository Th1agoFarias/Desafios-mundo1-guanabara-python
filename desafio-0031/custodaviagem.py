'''distancia = float(input('Qual é a distância da sua viagem ? '))
print(f'Você está pretes a começar uma viagem de {distancia} Km')
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'E o preço da passagem será de R${distancia*0.45:.2f}')'''

distancia = float(input('Qual é a distância da sua viagem ? '))
print(f'Você está pretes a começar uma viagem de {distancia} Km')
if distancia <=200:
    preco = distancia * 0.50
    print(f'E o preço da passagem será de R${distancia*0.50:.2f}')
else:
    preco = distancia * 0.45
    print(f'E o preço da passagem será de R${distancia*0.45:.2f}')


