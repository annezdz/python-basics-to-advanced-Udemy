nome = 'Saulo Pedro'
print(nome)
print(nome[0])
print('Dias D\'Avila' == "Dias D'Avila")

texto = 'Texto entre aspas simples... ""'
doc = """ Exemplo de...
          texto com múltiplas... 
          linhas."""
print(doc)

nome = 'Ana Paula'
print(nome[0])
print(nome[6])
print(nome[-3])
print(nome[4:])
print(nome[-5:])
print(nome[:3])
print(nome[2:5])

numeros = '123456789'
print(numeros[::])
print(numeros[::2])
print(numeros[1::2])
# Invertendo uma string
print(numeros[::-1])


frase = 'Python é uma linguagem excelente'

print('py' in frase)
print('ing' in frase)
print('ing' not in frase)
print(len(frase))
print(frase.upper())

a = '123'
b = ' de Oliveira 4'
print(a + b)
print(a.__add__(b))
print(len(a))
print(a.__len__())

print('1' in a)
print(a.__contains__('1'))