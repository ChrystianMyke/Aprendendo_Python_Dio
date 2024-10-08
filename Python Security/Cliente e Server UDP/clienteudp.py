import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('CLiente socket criado com sucesso!')

host = 'localhost'
porta = 5433
mensagem = 'Olá servidor'

try:
  print('Cliente: ' + mensagem)
  s.sendto(mensagem.encode(), (host, 5433))
  
  dados, servidor = s.recvfrom(4096)
  dados = dados.decode()
  print('Cliente: ' + dados)
finally:
  print('Encerrando conexão com o servidor...')
  s.close()