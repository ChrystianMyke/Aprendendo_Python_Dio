import re
import json
from urllib.request import urlopen

url = 'http://ipinfo.io/json'

resposta = urlopen(url)
dados = json.load(resposta)
ip = dados['ip']
org = dados['org']
cidade = dados['city']
pais = dados['country']
regiao = dados['region']

print('Detalhes do IP Externo\n')
print('IP: {4}\nRegião: {1}\nPaís: {2}\nCidade: {3}\nOrg: {0}'.format(org, regiao, pais, cidade, ip))