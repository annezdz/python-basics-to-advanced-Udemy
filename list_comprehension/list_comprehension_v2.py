# [ exressão for item in list if condicional]

dobros_dos_pares = [i * 2 for i in range(11) if i % 2 == 0]
print(dobros_dos_pares)

# Sem list comprehension forma 1'
dobros_dos_pares = []
for i in range(11):
    if i % 2 == 0:
        dobros_dos_pares.append(i * 2)
print(dobros_dos_pares)
