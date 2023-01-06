'''
Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras tem ao total sem considerar espaços.
- Quantas letras tem o primeiro nome.
'''

nome = str(input('Digite o seu nome completo: '))
tamanho = nome.split()

print(f'Nome com letras maiusculas: {nome.upper}')
print(f'Nome com letras minusculas: {nome.lower}')
print(f'Seu nome tem tamanho de {len(nome.strip())} letras')
print(f'O tamanho do seu primeiro nome é:{len([0])} letras')
