import pandas as pd
import os
os.system('cls')

mat = input('Digite a disciplina para por as notas: ').upper()
def head(mat):
    print('|'+'-'*15+f' BOLETIM GERAL ({mat}) '+'-'*15+'|\n')
    
os.system('cls')
head(mat)

num_alunos = int(input('Digite a quantidade de alunos da turma: '))
os.system('cls')
head(mat)

alunos = []
notas = []

for i in range(num_alunos):
    print('NOMES DOS ALUNOS:\n')
    aluno = input(f'ALUNO(A) {i+1}: ')
    if len(aluno) < 3:
        print('\n-- NOME INVALIDO, DIGITE NOVAMENTE --\n')
        continue
    nota = float(input(f'NOTA DO(A) ALUNO(A) {aluno.upper()}: '))
    if nota < 0 or nota > 10:
        print('\n-- NOTA INVALIDA, DIGITE NOVAMENTE --\n')
        continue
    print('  ')
    alunos.append(aluno)
    notas.append(nota)
    os.system('cls')
    head(mat)

print('\n--------------- TABELA ---------------\n')

for i in range(num_alunos):
    print(f'{alunos[i]} => {notas[i]}')

print('\n--------------- DATAFRAME ---------------\n')
df = pd.DataFrame({
        'ALUNO': alunos,
        'NOTA': notas
    })
print(df)

print('\n-------------------\n')
esp = input('voce quer mostrar a nota de algum aluno especifico? (s/n): ')

if esp.lower() == 's':
    os.system('cls')
    head(mat)
    print(df)

    linha = int(input('\nDigite o numero da linha correspondente ao indicie: '))
    if linha < 0 or linha > len(df)-1:
        while linha < 0 or linha > len(df)-1:
            os.system('cls')
            head(mat)
            print(df)
            print('\n-- VALOR INVALIDO, DIGITE NOVAMENTE --\n')
            linha = int(input('\nDigite o numero da linha correspondente ao indicie: '))
            os.system('cls')
    os.system('cls')
    head(mat)
    print(f'NOME: {df.iloc[linha].values[0]}')
    print(f'NOTA: {df.iloc[linha].values[1]}')

    qt = 's'
    while qt.lower() == 's':
        print('\n-------------------\n')
        qt = input('Voce quer mostrar a nota de outro aluno? (s/n): ')

        if qt.lower() == 's':
            os.system('cls')
            head(mat)
            print(df)

            linha = int(input('\nDigite o numero da linha correspondente ao indicie:  '))
            if linha < 0 or linha > len(df)-1:
                while linha < 0 or linha > len(df)-1:
                    os.system('cls')
                    head(mat)
                    print(df)
                    print('\n-- VALOR INVALIDO, DIGITE NOVAMENTE --\n')
                    linha = int(input('\nDigite o numero da linha correspondente ao indicie: '))
                    os.system('cls')
            os.system('cls')
            head(mat)
            print(f'NOME: {df.iloc[linha].values[0]}')
            print(f'NOTA: {df.iloc[linha].values[1]}')
        else:
            os.system('cls')
            break

elif esp.lower() == 'n':
    os.system('cls')
    print('   ')

head(mat)
print("\n---------- RELATORIO GERAL ----------\n")
print(df)

maior = df.sort_values('NOTA')
print('\n--------------- MENOR => MAIOR ---------------\n')
print(maior)

max = df['NOTA'].max()
min = df['NOTA'].min()
med = df['NOTA'].mean()
print(f'\nMAIOR NOTA: {max}')
print(f'MENOR NOTA: {min}')
print(f'MEDIA GERAL DA TURMA: {med:.2f}\n')