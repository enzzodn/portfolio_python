import random
import os
os.system('cls')

def head():
    print('===========================================================')
    print('================== PALAVRAS EMBARALHADAS ==================')
    print('===========================================================\n')
    
head()
print('---------- MENU DE OPCOES ----------\n')
print('     [1] COMIDA')
print('     [2] LUGAR')
print('     [3] PROFISSAO')
print('     [4] MATERIAL ESCOLAR\n')
escolha = int(input('DIGITE O MENU DE SUA PREFERENCIA: '))
os.system('cls')

if escolha == 1:
    palavras = ['GOIABA', 'MORANGO', 'MELANCIA', 'RABANETE', 'TAMARINDO',]
    tema = 'COMIDA'
elif escolha == 2:
    palavras = ['ORLANDO', 'FLORIDA', 'BRASIL', 'LUXEMBURGO', 'MEXICO']
    tema = 'LUGAR'
elif escolha == 3:
    palavras = ['PROFESSOR', 'PROGRAMADOR', 'AGRICULTOR', 'ADVOGADO', 'ATLETA']
    tema = 'PROFISSAO'
elif escolha == 4:
    palavras = ['CANETA', 'BORRACHA', 'CADERNO', 'APOSTILA', 'MOCHILA']
    tema = 'MATERIAL ESCOLAR'
else:
    print('\nREINICIE O JOGO E DIGITE UM VALOR VALIDO PARA O MENU!!!\n')
    quit()
palavra = random.choice(palavras)
lista_palavra = list(palavra)
random.shuffle(lista_palavra)
palavra_embaralhada = ''.join(lista_palavra)
for i in range(3):
    head()
    print(f'VOCE ESCOLHEU O TEMA: {tema}\n')
    print(f'\/\/\/\/\/\/ {palavra_embaralhada} \/\/\/\/\/\/')
    print(f'VOCE TESTOU {i}/3 TENTATIVAS')
    plvr = input('\nDIGITE A PALAVRA QUE VOCE ACHA CORRESPONDENTE: ')
    os.system('cls')
    if plvr.upper() == palavra:
        head()
        print(f'\nPARABENS VOCE ACERTOU! A PALAVRA ERA: / {palavra} \\')
        break
if plvr.upper() != palavra:
    head()
    print(f'\nVOCE ERROU! A PALAVRA ERA: / {palavra} \\')