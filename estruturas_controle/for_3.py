# Dicionario

produto = {'nome': 'Caneta BIC', 'preco': 14.99, 'importada': True,
           'estoque': 793}

for chave in produto.keys():
    print(chave)
print(chave)

for valor in produto.values():
    print(valor)
print(valor)

for chave, valor in produto.items():
    print(chave, '=', valor)

print(chave, valor)