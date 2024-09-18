class Pessoa:
  def __init__(self, nome=None , idade=None):
    self.nome = nome
    self.idade = idade
    
  @classmethod
  def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
    idade = 2024 - ano
    return Pessoa(nome, idade)
  
  @staticmethod
  def e_maior_idade(idade):
    return idade >= 18
  
#p = Pessoa("Chrystian", 20)
#print(p.nome, p.idade)

p = Pessoa.criar_apartir_data_nascimento(2003, 10, 29, "Chrystian")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(21))