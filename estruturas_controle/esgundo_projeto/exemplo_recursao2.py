def fibonacci_recursivo(quantidade, sequencia=(0, 1)):
    return sequencia if len(sequencia) == quantidade else \
        fibonacci_recursivo(quantidade, sequencia + (sum(sequencia[-2:]),))


for fib in fibonacci_recursivo(5):
    print(fib)
