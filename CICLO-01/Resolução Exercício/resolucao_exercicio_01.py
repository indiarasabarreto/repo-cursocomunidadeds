# 1. Some o valor 10 com 30 e exiba na tela:
print(10 + 30)

# 2. Some os seguintes números: 10, 300, 0.4, 10:
import numpy as np
# 10 + 300 + 0.4 + 10

print(np.sum([10, 300, 0.4, 10]))

# 3. Desenvolva comandos em Python capaz de calcular a média harmônica entre 5 números. Por exemplo: 2,3,5,6 e 9:
# média harmônica:
# n / ( 1/x1 + 1/x2 + 1/x3 + 1/x4 + 1/x5 )

x1 = int( input(( 'Digite o primeiro valor: ' )))
x2 = int( input(( 'Digite o segundo valor: ' )))
x3 = int( input(( 'Digite o terceiro valor: ' )))
x4 = int( input(( 'Digite o quarto valor: ' )))
x5 = int( input(( 'Digite o quinto valor: ' )))

n = 5

mh = n / ( 1/x1 + 1/x2 + 1/x3 + 1/x4 + 1/x5 )

print( 'O valor da Média Harmônica é: {:.2f}'.format( mh ) )

# 4. Um Cientista de Dados Jr precisa criar sequência de comandos que seja capaz de calcular a média ponderada dos valores digitados pelo usuário. O usuário é capaz de digitar 8 valores. O primeiro número tem peso 0.5, o segundo 1.0, o terceiro 1.5 até o último valor que tem peso 4, ou seja, os pesos são acrescidos de 0.5 para cada valor. Portanto, o algoritmo deve ser capaz de calcular a média ponderada dos oito valores digitados pelo usuário, cada valor com o seu respectivo peso.

# Fórmula da Média Ponderada
# ( peso_01 * valor_01 ) + ( peso_02 * valor_02 ) + ( peso_03 * valor_03 ) + ( peso_04 * valor_04) + ( peso_05 * valor_05) + ( peso_06 * valor_06 ) + ( peso_07 * valor_07 ) + ( peso_08 * valor_08 )

x1 = int(input( "Digite o primeiro valor: " ))
x2 = int(input( "Digite o segundo valor: " ))
x3 = int(input( "Digite o terceiro valor: " ))
x4 = int(input( "Digite o quarto valor: " ))
x5 = int(input( "Digite o quinto valor: " ))
x6 = int(input( "Digite o sexto valor: " ))
x7 = int(input( "Digite o sétimo valor: " ))
x8 = int(input( "Digite o oitavo valor: " ))

peso_01 = 0.5
peso_02 = 1.0
peso_03 = 1.5
peso_04 = 2.0
peso_05 = 2.5
peso_06 = 3.0
peso_07 = 3.5
peso_08 = 4.0

numerador = ((peso_01 * x1) + (peso_02 * x2) + ( peso_03 * x3 ) + ( peso_04 * x4) + ( peso_05 * x5) + ( peso_06 * x6 ) + ( peso_07 * x7 ) + ( peso_08 * x8 ) )
denominador = (peso_01 + peso_02 + peso_03 + peso_04 + peso_05 + peso_06 + peso_07 + peso_08 )

media_ponderada = numerador / denominador

print( 'O valor da Média Ponderada é: {:2f}'.format( media_ponderada ))


# 5. Um programador Jr precisa construir uma mini calculadora. Essa calculadora segue os seguintes padrões:

    # A. Se o usuário digital um valor menor ou igual a 5, a calculadora vai multiplicar esse valor por 10 e retornar o valor resultantes para o usuário.
    
    # B. Se o usuário digitar um número entre 6 e 10, a calculadora multiplica por 20 o número digitado pelo usuário
    
    # C. Se o usuário digitar um valor maior ou igual a 11, a calculadora soma 100 ao número digitado. Ajude o programador Jr a construir essa calculadora, fornecendo os comandos em Python para ele.
    
num = int(input("Digite o valor: "))
    
if num <= 5:
    resultado = num * 10
elif num <= 10:
    resultado = num * 20
else:
    resultado = num + 100

print('O valor é: {}'.format( resultado ))
    

# 6. Um programador Jr precisa criar um algoritmo que consiga fazer a comparação entre três valores e exibir qual é o maior e qual é o menor valor digitado. Ajude o programador desenvolvendo o código em Python.

num01 = int(input( "Digite valor: " ))
num02 = int(input( "Digite valor: " ))
num03 = int(input( "Digite valor: " ))

# Descobrir qual o maior valor:
maior = num01

if num02 > maior:
  maior = num02

if num03 > maior:
  maior = num03

# Descobrir qual o menor valor
menor = num01

if num02 < menor:
  menor = num02

if num03 < menor:
  menor = num03

print( 'O maior valor é: {}'.format( maior ))
print( 'O menor valor é: {}'.format( menor ))

    