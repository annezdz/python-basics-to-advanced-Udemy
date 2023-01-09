'''print(True)
print(False)
print(1.2 + 1)
print('Teste')
print("Teste")

print([1, 2, 3])
print({'nome': 'Pedro', 'idade': 22})
print(None)

a = 10
b = 5.2
print(a + b)

a = "Agora sou uma String"
print(a)
print(b)
'''
print(2 + 3)
print(4 - 7)
print(2 * 5.3)
print(9.4 / 3)
print(9.4 // 3)
print(10 % 3)

# Desafio Operadores

salario = 3450.45
despesas = 2456.2

percentual_comprometimento = (despesas * 100.00) // salario
print(percentual_comprometimento, "%")

a = 1
a += 1
print(a)

a = 1
a -= 1
print(a)

a = 1
a *= 1
print(a)

a = 1
a /= 1
print(a)

a = 1
a %= 1
print(a)

a = 1
a **= 1
print(a)

a = 20
a //= 2.2
print(a)

# 1
esta_chovendo = True
print('Hoje estou com as roupas ' + ('secas.', 'molhadas.')[esta_chovendo])

# 2
print(
    'Hoje estou com as roupas ' + ('molhadas.' if esta_chovendo else 'secas. '))

# Operadores de Membro

lista = [1, 2, 3, 'Ana', 'Carla']
print(2 in lista)
print('Ana' not in lista)
'''
x = 3
y = x
z = 3
print(x is y)
print(y is z)
print(x is not z)

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]

print(lista_a is lista_b)
print(lista_b is lista_c)
print(lista_a is not lista_c)
'''
print(type(1))

a = 2
b = '3'
print(type(a))
print(type(b))

print(a + int(b))

a = 5
b = 2.5

print(type(a / b))
print(type(a - b))
print(type(a + b))

print(b.is_integer())
