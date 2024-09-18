import hashlib

file1='testA.txt'
file2='testB.txt'

f=open(file1, 'w')
f.write('Python Segurança!\n__'); f.close()

f=open(file2, 'w')
f.write('Python Segurança!!\n__'); f.close()

hash1 = hashlib.new('ripemd160')
hash1.update( open(file1, 'rb').read() )

hash2 = hashlib.new('ripemd160')
hash2.update( open(file2, 'rb').read() )

if hash1.digest() != hash2.digest():
    print(f"O arquivo: {file1} é diferente do arquivo: {file2}")
else:
    print("Os arquivos são iguais")
