# [ exressão for item in list if condicional]

dobros = [i * 2 for i in range(11)]
print(dobros)

# Sem list comprehension forma 1'
dobros = []
for i in range(11):
    dobros.append(i * 2)
print(dobros)