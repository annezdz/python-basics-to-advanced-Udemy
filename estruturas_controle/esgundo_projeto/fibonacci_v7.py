def fibonacci(quantidade):
    resultado = [0, 1]
    while len(resultado) <= quantidade - 2:
        resultado.append(sum(resultado[-2:]))
    return resultado


'''
for number in fibonacci(10):
    print(number)

'''


def fibonacci_recursivo(quantidade, sequencia=(0, 1)):
    if len(sequencia) == quantidade:
        return sequencia
    return fibonacci_recursivo(quantidade, sequencia + (sum(sequencia[-2:]),))


for fib in fibonacci_recursivo(20):
    print(fib)
