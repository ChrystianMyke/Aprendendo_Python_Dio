# Exemplo utilizando um iterável
texto = ''
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end='')
else:  # não muito comum
    print()     # adiciona uma quebra de linha
#----------------------------------------------------   


# Exemplo utilizando uma função built-in range
for numero in range(0,51,5):
    print(numero, end=' ')