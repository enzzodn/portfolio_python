import random as rd

dict_info = {
    'letras':['a','b','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
    'numeros':['0','1','2','3','4','5','6','7','8','9'],
    'caract_esp':['!','@','#','$','%','&','*','?']
}

c_rd = dict_info["letras"]
n_rd = dict_info["numeros"]
c_esp_rd = dict_info["caract_esp"]

# SENHA POSSUI 9 CARCTERES => 1 LETRA MAIÚSCULA; 5 LETRAS MINÚSCULAS; 1 CARACTERE ESPECIAL E 2 NÚMEROS.
senha = [rd.choice(c_rd).upper(), rd.choice(c_rd), rd.choice(c_rd), rd.choice(c_rd), rd.choice(c_rd), rd.choice(c_rd), rd.choice(c_esp_rd), rd.choice(n_rd), rd.choice(n_rd)]
rd.shuffle(senha)
senha = ''.join(senha)

print('PARA UMA SENHA FORTE É NECESSÁRIO ALGUNS ELEMENTOS:\n')
print('     -> LETRAS MAIÚSCULAS E MINÚSCULAS')
print('     -> NÚMEROS')
print('     -> CARACTERES ESPECIAIS (EX.: !, @, $, %)')

print(f'\nPENSANDO NISSO, ESSA É SUA NOVA SENHA DE 9 CARACTERES: {senha}')