nome = input('Informe seu nome: ')
idade = input('Informe sua idade: ')
print('='*30)
print(f'Meu nome é {nome}, tenho {idade} anos')

print(nome,idade, end='...\n')
print(nome,idade, sep='#', end='...\n')
print(nome,idade, sep='#')