def fibonacci(quantidade):
    resultado = [0, 1]
    for number in range(0, quantidade-2):
        resultado.append(sum(resultado[-2:]))
    return resultado


for fib in fibonacci(20):
    print(fib, end=', ')
