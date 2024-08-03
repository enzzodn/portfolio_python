import os
os.system('cls')
import sys

def soma(a,b):
    sum = a+b
    return sum

def subtracao(a,b):
    sub = a-b
    return sub

def multiplicacao(a,b):
    mult = a*b
    return mult

def divisao(a,b):
    if b == 0:
        divs = 'VALOR INVALIDO -- IMPOSSIVEL DIFINIR UMA DIVISAO POR 0'
    else:
        divs = a/b
        if type(divs) == float:
            divs = round(divs,2)
    return divs

def menu():
    print('     [1] SOMA')
    print('     [2] SUBTRACAO')
    print('     [3] MULTIPLICACAO')
    print('     [4] DIVISAO\n')

def head():
    print('-'*45)
    print('-'*10+'  C A L C U L A D O R A  '+'-'*10)
    print('-'*45+'\n')

head()
menu()

oprc = int(input('DIGITE UM NUMERO DO MENU: '))
if oprc != 1 and oprc != 2 and oprc != 3 and oprc != 4:
    print('\nREINICIE A CALCULADORE E DIGITE UM NUMERO VALIDO PARA O MENU\n')
    sys.exit()

a = int(input('\nDIGITE UM NUMERO PARA (a): '))
b = int(input('DIGITE UM NUMERO PARA (b): '))

if oprc == 1:
    sum = soma(a,b)
    print(f'\n RESULTADO (SOMA): {sum}\n')

elif oprc == 2:
    sub = subtracao(a,b)
    print(f'\n RESULTADO (SUBTRACAO): {sub}\n')

elif oprc == 3:
    mult = multiplicacao(a,b)
    print(f'\n RESULTADO (MULTIPLICACAO): {mult}\n')

elif oprc == 4:
    divs = divisao(a,b)
    print(f'\n RESULTADO (DIVISAO): {divs}\n')

else:
    print('\nVALOR INVALIDO -- REINICIE A CALCULADORA\n')