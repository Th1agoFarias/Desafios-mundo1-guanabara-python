from random import choice

a1 = input('Nome do(a) primeiro(a) aluno(a): ')
a2 = input('Nome do(a) segundo(a) aluno(a): ')
a3 = input('Nome do(a) terceiro(a) aluno(a): ')
a4 = input('Nome do(a) quarto(a) aluno(a): ')
lista  = [a1, a2, a3, a4]

escolhido = choice(lista)
print(f'A aluno(a) sorteada foi: {escolhido}')