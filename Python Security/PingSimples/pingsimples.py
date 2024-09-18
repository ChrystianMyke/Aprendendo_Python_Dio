import os

print("#" * 100)

ip_ou_host = input("Digite o Ip ou hoste a ser verificado: ")
print("-" * 100)
os.system('ping -n 6 {}'.format(ip_ou_host))
print("-" * 100)