# Breve introdução ás f-strings // f: formatação

nome = 'Kethelen Parra'
altura = 1.76
peso = 90.0
imc = peso / altura ** 2

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

