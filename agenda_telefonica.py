import pandas as pd
import os
import sys

dict_contatos = [
    ['João Silva', '(11) 91234-5678'],
    ['Maria Oliveira', '(21) 98765-4321'],
    ['Carlos Pereira', '(31) 99876-5432'],
    ['Ana Souza', '(41) 92345-6789'],
    ['Paulo Santos', '(51) 93456-7890'],
    ['Juliana Costa', '(61) 94567-8901'],
    ['Ricardo Almeida', '(71) 95678-9012'],
    ['Fernanda Lima', '(81) 96789-0123'],
    ['Bruno Ferreira', '(91) 97890-1234'],
    ['Camila Rodrigues', '(19) 98901-2345']
]


def head():
    print('-'*48)
    print('-'*15+' LISTA TELEFÔNICA '+'-'*15)
    print('-'*48+'\n')


def menu():
    print("[1] ADICIONAR CONTATO")
    print("[2] REMOVER CONTATO")
    print("[3] ALTERAR CONTATO")
    print("[4] LISTAR CONTATOS")
    print("[5] LISTAR CONTATOS POR NOME")
    print("[6] SAIR")
    print('\nÉ RECOMENDADO LISTAR OS CONTATOS PRIMEIRO ANTES DE QUALQUER ALTERAÇÃO\n')


def add_contato(df_contatos):
    res1 = 'n'
    res2 = 'n'

    while res1.lower() == 'n':
        os.system('cls')
        head()
        nome = input('DIGITE O NOME: ')
        print(f'ESTE NOME ESTÁ CORRETO: {nome}')
        res1 = input('DIGITE s/n: ')

    while res2.lower() == 'n':
        os.system('cls')
        head()
        num = input('DIGITE O NÚMERO DE TELEFONE COM DDD E SEM FORMATAÇÃO (EX: 85900000000): ')
        numero_formatado = f'({num[0]+num[1]}) {num[2]+num[3]+num[4]+num[5]+num[6]}-{num[7]+num[8]+num[9]+num[10]}'
        print('CERTIFIQUE-SE DE QUE O TELEFONE POSSUI EXATOS 11 DÍGITOS')
        print(f'ESTE NÚMERO ESTÁ CORRETO: {numero_formatado}')
        res2 = input('DIGITE s/n: ')
    
    os.system('cls')
    head()
    print(f'NOME: {nome}')
    print(f'TELEFONE: {numero_formatado}')
    res3 = input('DIGITE s/n SE OS DADOS ACIMA ESTIVEREM CORRETOS: ')
    if res3.lower() == 'n':
        print('\nREINICIE O CÓDIGO E TENTE NOVAMENTE!')
        sys.exit()
    elif res3.lower() == 's':
        novo_contato = {'NOME':f'{nome}', 'TELEFONE': f'{numero_formatado}'}
        df_contatos.loc[len(df_contatos)] = novo_contato

        print('\nCONTATO ADICIONADO COM SUCESSO!\n')
    
    print(df_contatos)
    df_contatos.to_excel('df_contatos.xlsx', index=False)


def remover_contato(df_contatos):
    res1 = 'n'
    while res1.lower() == 'n':
        os.system('cls')
        head()
        print(df_contatos)
        rmv_cont = int(input('\nDIGITE O ÍNDICE DA LINHA A QUAL VOCÊ DESEJA REMOVER: '))
        print(f'\nLINHA ESCOLHIDA: ÍNDICE {rmv_cont}')
        print(f"NOME: {df_contatos.iloc[rmv_cont]['NOME']}")
        print(f"TELEFONE: {df_contatos.iloc[rmv_cont]['TELEFONE']}")
        res1 = input('OS DADOS ACIMA ESTÃO CORRETOS (s/n): ')
    
    df_contatos = df_contatos.drop(rmv_cont, axis=0)
    df_contatos.reset_index(drop=True, inplace=True)
    print(f'\nCONTATO REMOVIDO COM SUCESSO!\n')

    print(df_contatos)
    df_contatos.to_excel('df_contatos.xlsx', index=False)


def alterar_contato(df_contatos):
    res1 = 'n'
    while res1.lower() == 'n':
        os.system('cls')
        head()
        print(df_contatos)
        rmv_cont = int(input('\nDIGITE O ÍNDICE DA LINHA A QUAL VOCÊ DESEJA ALTERAR: '))
        print(f'\nLINHA ESCOLHIDA: ÍNDICE {rmv_cont}')
        print(f"NOME: {df_contatos.loc[rmv_cont, 'NOME']}")
        print(f"TELEFONE: {df_contatos.loc[rmv_cont, 'TELEFONE']}")
        res1 = input('OS DADOS QUE VOCÊ ESCOLHEU PARA ALTERAR ACIMA ESTÃO CORRETOS (s/n): ')
    
    alt = int(input('VOCÊ QUER ALTERAR NOME OU CONTATO? (NOME : 1) (TELEFONE : 2): '))
    if alt == 1:
        res_nome = 'n'
        while res_nome.lower() == 'n':
            os.system('cls')
            head()
            print(df_contatos)
            print('')
            novo_nome = input('DIGITE O NOME: ')
            print(f'ESTE NOME ESTÁ CORRETO: {novo_nome}')
            res_nome = input('DIGITE s/n: ')

        df_contatos.loc[rmv_cont, 'NOME'] = novo_nome
        print('\nNOME ALTERADO COM SUCESSO!\n')
        print(df_contatos)

    elif alt == 2:
        res_telefone = 'n'
        while res_telefone == 'n':
            os.system('cls')
            head()
            print(df_contatos)
            novo_telefone = input('\nDIGITE O NÚMERO DE TELEFONE COM DDD E SEM FORMATAÇÃO (EX: 85900000000): ')
            numero_formatado = f'({novo_telefone[0]+novo_telefone[1]}) {novo_telefone[2]+novo_telefone[3]+novo_telefone[4]+novo_telefone[5]+novo_telefone[6]}-{novo_telefone[7]+novo_telefone[8]+novo_telefone[8]+novo_telefone[9]}'
            df_contatos.loc[rmv_cont, 'TELEFONE'] = numero_formatado
            print(f'ESTE NÚMERO ESTÁ CORRETO: {numero_formatado}')
            res_telefone = input('DIGITE s/n: ')

        print('\nTELEFONE ALTERADO COM SUCESSO!\n')
        print(df_contatos)
        
    df_contatos.to_excel('df_contatos.xlsx', index=False)


def listar_contatos(df_contatos):
    os.system('cls')
    head()
    print(df_contatos)


def listar_contatos_nome(df_contatos):
    os.system('cls')
    head()
    print(df_contatos.sort_values(by='NOME'))


# -------------------------------------


while True:

    try:
        df_contatos = pd.read_excel('df_contatos.xlsx')
    except:
        df_contatos = pd.DataFrame(dict_contatos, columns=['NOME', 'TELEFONE'])

    os.system('cls')
    head()
    menu()

    res = int(input('DIGITE A OPÇÃO DESEJADA: '))

    if res == 1:
        add_contato(df_contatos)
    elif res == 2:
        remover_contato(df_contatos)
    elif res == 3:
        alterar_contato(df_contatos)
    elif res == 4:
        listar_contatos(df_contatos)
    elif res == 5:
        listar_contatos_nome(df_contatos)
    elif res == 6:
        os.system('cls')
        sys.exit()
    else:
        print('REINICIE O PROGRAMA E DIGITE UM NÚMERO CORRESPONDENTE VÁLIDO.')
        sys.exit()

    print('')
    choose = int(input('DESEJA VOLTAR AO MENU PRINCIPAL? (VOLTAR : 1) (SAIR : 2): '))
    if choose == 1:
        print('')
    elif choose == 2:
        os.system('cls')
        sys.exit()