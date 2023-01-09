lista = []
print(len(lista))
lista.append(1)
lista.append(4)
print(len(lista))
print(lista)
lista.append('Ana')
lista.append('Dudu')
print(len(lista))
print(lista)
lista.remove(4)
print(lista)
lista.reverse()
print(lista)

lista1 = [1, 5, 'Rebeca', 'Guilherme', 3.14, 'Dudu', 999]
print(lista1.index('Guilherme'))

print(lista1[2])

print(1 in lista1)
print('Rebeca' in lista1)
print('Pedro' not in lista1)
print(lista1[-1])

print(lista1[1:3])
print(lista1[1:-1])
print(lista1[::-1])
print(lista)
del lista[0]
print(lista)

tupla = ('um',)
print(tupla[0])


cores = ('verde', 'amarelo', 'azul', 'branco', 'azul')
print(cores[0])
print(cores[-1])
print(cores[1:])
print(cores.index('amarelo'))
print(cores.count('azul'))
print(len(cores))
