from random import randint
import os
import time

def head():
    print('\n<=====/ JOGO DA ADVINHAÇÃO \=====>\n')

os.system('cls')
head()
num = randint(0,100)
res = int(input('DIGITE UM NÚMERO ENTRE 0 E 100: '))

while res != num:
    if res < num:
        print('\nO NÚMERO É --MAIOR-- QUE O NÚMERO DIGITADO\n')
        time.sleep(3)
    elif res > num:
        print('\nO NÚMERO É --MENOR-- QUE O NÚMERO DIGITADO\n')
        time.sleep(3)
    os.system('cls')
    head()
    res = int(input('DIGITE UM NÚMERO: '))
if res == num:
    os.system('cls')
    head()
    print(f'\nVOCÊ GANHOU -- O NÚMERO ERA: {num}\n')