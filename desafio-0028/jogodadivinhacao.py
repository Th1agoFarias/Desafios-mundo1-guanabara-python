'''tempo=int(input('Qauantos ano tem seu carro ?'))
if tempo <=3:
    print('Carro Novo')
else:
    print('Carro Velho')
print('---FIM---')'''

from random import randint
from time import sleep
computador = randint(0,5) # Faz o computador: "Pensar"
print('*' * 20)
print('Oh, eu vou pensar em número entre 0 e 5. Tenta adivinhar aí, mané !')
print('*' * 20)
jogador = int(input('E aí, meu cria, em que número eu pensei ?'))  #Jogador tenta adivinhar 
print('Processando...')
sleep(5)
if jogador == computador:
    print('Parabéns, Zé Mané !')
else:
    print(f'Errou zé ruela ! Eu pensei nesse número aqui oh: {computador} eu não nesse {jogador}  ')    