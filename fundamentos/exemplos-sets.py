a = {1, 2, 3}
print(type(a))
a = set('coder')
print(a)
print(3 in a)
print(4 not in a)
print({1, 2, 3} == {3, 2, 1, 3})

c = {1, 2}
d = {2, 3}
print(c.union(d))
print(c.intersection(d))
print(c <= d)
print({1, 2, 3} - {2})

nome, idade = 'Ana', 30
print('Nome: %s  - Idade: %.2f' % (nome, idade))

print('Nome: {0}  Idade: {1}'.format(nome, idade))

print(f'Nome: {nome}  Idade: {idade}')
