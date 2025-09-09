print('|',50*'-','|')
print('|',22*'-','IMC',23*'-','|')
print('|',50*'-','|')
nome = input('| Digite o seu nome: ')
peso = float(input(f'| Qual é o seu peso {nome}: '))
altura = float(input(f'| Qual é a sua altura {nome}: '))
imc = peso / (altura ** 2)
print(f'| Seu IMC é: {imc:.2f}')
print('|',50*'-','|')

if imc < 18.5:
    print('| Abaixo do peso ','Coma mais mano =)')
elif imc <= 24.9:
    print('| Peso normal ','É isso aí, tá tudo certinho!') 
elif imc <= 29.9:
    print('| Sobrepeso ','Mano, coma menos =)')
elif imc <= 34.9:
    print('| Obesidade grau I ','Tá passando do pontoo, vai correr!') 
elif imc <= 39.9:
    print('| Obesidade grau II ','Tenta se levantar pelo menos')
elif imc >= 40.0:
    print('| Obesidade grau III (mórbita) ','Já era mano, tente novamente =(')
