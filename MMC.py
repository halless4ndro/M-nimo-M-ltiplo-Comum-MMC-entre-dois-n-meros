# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 16:33:24 2020

Algoritmo calcula o mínimo múltiplo
comum entre dois números informados
pelo usuário.

@author: Hallessandro
"""

x=int(input("Digite um número inteiro positivo "))
y=int(input("Digite um número inteiro positivo "))

if x==0 or y==0:
  print("O mínimo múltiplo comum é zero")
elif x==1:
  print(f"O mínimo múltiplo comum é {y}")
elif y==1:
  print(f"O mínimo múltiplo comum é {x}")
else:
    
  # Cria-se uma lista com os múltiplos de x:
  multiplicador=1
  total=0
  multiplos_x=[]
  while total<x*y:
    multiplos_x.append(x*multiplicador)
    total=x*multiplicador
    multiplicador+=1

  # Cria-se uma lista com os múltiplos de y:
  multiplicador=1
  total=0
  multiplos_y=[]
  while total<x*y:
    multiplos_y.append(y*multiplicador)
    total=y*multiplicador
    multiplicador+=1  

  # Cria-se um conjunto interseção das duas listas calculadas
  multiplos_comuns=set(multiplos_x).intersection(multiplos_y)

  # O menor valor do conjunto intesecção é o MMC dos valores informados pelo usuário
  print(f"O mínimo múltiplo comum entre {x} e {y} é {min(multiplos_comuns)}")

