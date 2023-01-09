pessoa = {'nome': 'Prof(a).Ana', 'idade': 38, 'cursos': ['Inglês', 'Português']}

print(type(pessoa))
print(pessoa)
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cursos'][1])
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa.get('idade'))
print(pessoa.get('teste'))
print(pessoa.get('teste', []))

pessoa = {'nome': 'Prof(a).Dudu', 'idade': 50,
          'cursos': ['Angular', 'React', 'Vue']}
print(pessoa)
pessoa['cursos'].append('JS')
print(pessoa)
pessoa.pop('idade')
print(pessoa)
pessoa.update({'idade':55, 'Sexo': 'M'})
print(pessoa)

del pessoa['cursos']
print(pessoa)
pessoa.clear()
print(pessoa)