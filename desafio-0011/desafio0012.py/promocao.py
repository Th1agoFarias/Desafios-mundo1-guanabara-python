pro = 'PROMOÇÃO'
print('{:=^50}'.format(pro))
n1 = float(input('Digite o preço do produto: '))
n2 = float(input('Quantos porcentos de descontos '))
n3= n1*n2/100
des = n1-n3
print(f'Valor: {n1} \nDesconto: {n2} \nPreço com desconto: {des}')
print('='*50)