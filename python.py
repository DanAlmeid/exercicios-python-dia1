import random
import math
# exercícios:
# 1 - Escreva um programa que leia o nome de um funcionário,
# seu número de horas trabalhadas, o valor que recebe por hora
# e calcula o salário desse funcionário.
# A seguir, mostre o nome e o salário do funcionário.

nome = input('digite seu nome: ')
salario_hora = float(input('Digite quanto recebe por hora: '))
horas = int(input('digite a quantidade de horas trabalhadas: '))

salario = salario_hora*horas

print(f'{nome} recebera {salario} reais')

# -----------------------------------------------------------------------------------------------------------

# 2 - crie uma função que receba uma lista de 20 valores aleatórios, retornar
# apenas o maior valor e printar em tela.

lista= []
i = 0
while i < 20:
    lista.append(random.randrange(1,100))
    i+= 1

print(max(lista,key=int))

# -----------------------------------------------------------------------------------------------------------

# 3 - crie uma lista com 10 números aleatórios,
# itere essa lista e printar em tela os
# valores que são ímpares e pares.

lista_total = []
lista_impar = []
lista_par = []
i = 0
while i<10 :
    lista_total.append(random.randrange(1,100))
    if lista_total[i] % 2 == 0:
        lista_par.append(lista_total[i])
    else:
        lista_impar.append(lista_total[i])
    i+=1
print(str(lista_total))
print(f'pares:  {str(lista_par)}')
print(f'Impares: {str(lista_impar)}')

# -----------------------------------------------------------------------------------------------------------

# 4 - Crie uma função python que cálcule uma função de 2º Grau

#   Delta = B² - 4AC
#   Bhāskara = -B +- (raiz de delta)/ 2A

a = int(input('digite o valor de a: '))
b = int(input('digite o valor de b: '))
c = int(input('digite o valor de c: '))

delta = (b**2) - (4*a*c)

x1 = (-b + math.sqrt(delta))/(2*a)
x2 = (-b - math.sqrt(delta))/(2*a)

print(f'o valor de x1 é igual a{x1} e o valor de x2 é igual a {x2}')


# 5 - Faça um programa que leia o raio de um círculo e faça duas
# funções: uma que calcule a área do círculo e outra que calcule
# o comprimento do círculo.

raio = float(input('dgite o fraio do circulo'))

def area_cirulo(raio):
    area = math.pi*(raio**2)
    print(round(area,2))

def comprimento_circulo(raio): 
    comprimento = 2*math.pi*raio
    print(round(comprimento,2))

print(area_cirulo(raio))
print(comprimento_circulo(raio))