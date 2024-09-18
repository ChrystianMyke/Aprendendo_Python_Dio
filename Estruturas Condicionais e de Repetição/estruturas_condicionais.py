MAIOR_IDADE = 18
IDADE_ESPECIAL = 17
print('='*45)
idade = int(input('Informe Sua Idade: '))

if idade >= MAIOR_IDADE:
    print('Maior de idade, pode tirar sua CNH!!')
    
if idade < MAIOR_IDADE:
    print('Ainda não pode tirar sua CNH!!')
    
print('='*45)

if idade >= MAIOR_IDADE:
    print('Maior de idade, pode tirar sua CNH!!')
else:
    print('Ainda não pode tirar sua CNH!!')
    
print('='*45)
    
if idade >= MAIOR_IDADE:
    print('Maior de idade, pode tirar sua CNH!!')   
elif idade == IDADE_ESPECIAL:
    print('Pode fazer aulas teóricas, mas não pode realizar aulas práticas!!')
else:
    print('Ainda não pode tirar sua CNH!!')
print('='*45)

