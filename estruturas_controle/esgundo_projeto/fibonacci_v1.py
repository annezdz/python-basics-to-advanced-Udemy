def fibonacci():
    penultimo = 0
    ultimo = 1
    print(f'{penultimo}, {ultimo}', end=',')
    while True:
        proximo = penultimo + ultimo
        print(proximo, end=',')
        penultimo = ultimo
        ultimo = proximo

fibonacci()