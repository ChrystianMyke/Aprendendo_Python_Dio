# Treinando Pep 8
# ctrl + alt + l organização de códigos
"""
  Isso é uma docstring  
"""


import sys
import pandas
import numpy 
import matplotlib.pyplot

from pandas import array
# Quebra de linhas para múltiplos imports
from pandas import (
  read_csv,
  DataFrame,
  Series,
  HDFStore
)


# Constantes
CONSTANT = 100


# Classe
class JuridicPerson:
  # Classes começam por letras maiúsculas
  def __init__(self, message):
    self.name = None
    self.inicio = message
  pass

  # Nome é separado por underline
  def set_name(self, name):
    """
    Este método tem como objetivo setar o nome do onjeto instanciado pela classe.
    
    :param name: o nome definido pelo usuário
    :return: retorna um nome via print
    """
    self.name = name
    print('O nome é: ', name)

variáveis = 0
x =1
y=2

var = 1 
var = 2

lista = [1,2,3,4,5,6,7,8,9] # errado com relação a espaçamento e disposição

matriz = [
  1, 2, 3,
  4, 5, 6,
  7, 8, 9
]

matriz = [
  1, 2, 3,
  4, 5, 6,
  7, 8, 9
  ]

number_one = 1


# Errado
def retornofuncaoargs(
  arg_one, arg_two, 
  arg_three, arg_four):
  # Comentário de uma linha
  return (arg_one + arg_two) / (arg_three + arg_four)

# Certo
def retorno_funcao_args(arg_one, arg_two, 
                        arg_three, arg_four):
  pass


# Certo
def retorno_funcao_args(arg_one, 
                        arg_two, 
                        arg_three, 
                        arg_four):
  pass

def print_hi_with_message(name):
  pass

# Wrong
def printhiwithname(x, y, z):
  t = (x+y)/z
  pass

# Correct
def media_aluno(nota1, nota2, divisor):
  t = (nota1+nota2)/divisor
  pass

def funcao_ficticia(*args):
  pass

media_aluno(5,9,2)
media_aluno(7, 5, 3)
vetor = []

funcao_ficticia(vetor[2,3,4], {'key':2})
funcao_ficticia(vetor[2 ,3 ,4], {'key': 2})

# Correta
if x == 4: print (x,y); x,y=y,x

if x == 4:
  print(x, y)
  x, y = y, x

# Mais sobre espaçamento
foo = (0,)  # Correto
bar=(0, )  # Errado

# Wrong
def print_hi(name):
  # Use a breakpoint in the code line below to debug your script
  print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint