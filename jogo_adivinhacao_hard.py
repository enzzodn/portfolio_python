from random import randint
import os
import time

def head():
    print('\n<=====/ JOGO DOS 4 DÍGITOS \=====>\n')
n1 = randint(0,9)
n2 = randint(0,9)
n3 = randint(0,9)
n4 = randint(0,9)
num = n1, n2, n3, n4
vez = 1

os.system('cls')
head()

# print(num)
print('\nDICA: TODOS OS NÚMEROS VÃO DE 0000 ATÉ 9999')
tent = input('DIGITE UM NÚMERO DE 4 DÍGITOS: ')
if len(tent) != 4:
    print('DIGITE UM NÚMERO VÁLIDO')
    quit()
tt = tuple(map(int, tent))

while tt != num:
    #---------- DIGITO 1 ----------
    if tt[0] == num[0]:
        def dica1():
            print('POSIÇÃO 1: NÚMERO <== CERTO ==> NA POSIÇÃO <== CERTA ==>')
    elif (tt[0] == num[1]) or (tt[0] == num[2]) or (tt[0] == num[3]):
        def dica1():
            print('POSIÇÃO 1: NÚMERO <== CERTO ==> NA POSIÇÃO <== ERRADA ==>')
    else:
        def dica1():
            print('POSIÇÃO 1: NÚMERO <== ERRADO ==> NA POSIÇÃO <== ERRADA ==>')

    #---------- DIGITO 2 ----------
    if tt[1] == num[1]:
        def dica2():
            print('POSIÇÃO 2: NÚMERO <== CERTO ==> NA POSIÇÃO <== CERTA ==>')
    elif (tt[1] == num[0]) or (tt[1] == num[2]) or (tt[1] == num[3]):
        def dica2():
            print('POSIÇÃO 2: NÚMERO <== CERTO ==> NA POSIÇÃO <== ERRADA ==>')
    else:
        def dica2():
            print('POSIÇÃO 2: NÚMERO <== ERRADO ==> NA POSIÇÃO <== ERRADA ==>')

    #---------- DIGITO 3 ----------
    if tt[2] == num[2]:
        def dica3():
            print('POSIÇÃO 3: NÚMERO <== CERTO ==> NA POSIÇÃO <== CERTA ==>')
    elif (tt[2] == num[0]) or (tt[2] == num[1]) or (tt[2] == num[3]):
        def dica3():
            print('POSIÇÃO 3: NÚMERO <== CERTO ==> NA POSIÇÃO <== ERRADA ==>')
    else:
        def dica3():
            print('POSIÇÃO 3: NÚMERO <== ERRADO ==> NA POSIÇÃO <== ERRADA ==>')

    #---------- DIGITO 4 ----------
    if tt[3] == num[3]:
        def dica4():
            print('POSIÇÃO 4: NÚMERO <== CERTO ==> NA POSIÇÃO <== CERTA ==>')
    elif (tt[3] == num[0]) or (tt[3] == num[1]) or (tt[3] == num[2]):
        def dica4():
            print('POSIÇÃO 4: NÚMERO <== CERTO ==> NA POSIÇÃO <== ERRADA ==>')
    else:
        def dica4():
            print('POSIÇÃO 4: NÚMERO <== ERRADO ==> NA POSIÇÃO <== ERRADA ==>')
    
    time.sleep(1)

    os.system('cls')
    head()

    
    print(f'ANOTAÇÕES DA RODADA {vez}:')
    print(f'SEU NÚMERO: {tt}\n')
    dica1()
    dica2()
    dica3()
    dica4()

    # print(num)
    print('\nDICA: TODOS OS NÚMEROS VÃO DE 0000 ATÉ 9999')
    tent = input('DIGITE UM NÚMERO DE 4 DÍGITOS: ')
    if len(tent) != 4:
        print('DIGITE UM NÚMERO VÁLIDO')
        time.sleep(1)
    tt = tuple(map(int, tent))

    vez += 1

os.system('cls')
head()
print('----- PARABÉNS VOCÊ ACERTOU!! -----')
print(f'JOGOU {vez} RODADAS')
print(f'O NÚMERO ERA: {num}')