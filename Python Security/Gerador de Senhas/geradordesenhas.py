import random
import string

tamanho = int(input("Digite o tamanho da senha desejada: "))

chars = string.ascii_letters + string.digits + '!@#$%&*()-=+'

rnd = random.SystemRandom()

print("-"*20)
print("Senha gerada:")
print(''.join(rnd.choice(chars) for i in range(tamanho)))