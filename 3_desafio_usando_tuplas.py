
"""Crie um programa que vai gerar cinco números aleatórios e 
colocar em uma tupla. Depois disso, mostre a listagem de
números gerados e tambem indique o menor e o maior valor que 
estão na tupla"""



import random
numeros = (random.randint(1, 100), random.randint(1, 100), 
random.randint(1, 100), random.randint(1, 100),
random.randint(1, 100))

print(numeros)
print(f" O menor valor é: {min(numeros)}")
print(f"O maior valor é: {max(numeros)}")

