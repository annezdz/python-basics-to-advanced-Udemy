# Criando listas a partir de uma única linha com List Comprehension

![img.png](img.png)
![img_1.png](img_1.png)


# Exemplo 2 usando List Comprehension (e não usando também)

![img_2.png](img_2.png)


# Exemplo 3 usando generators
Generator gera os dados sob demanda
![img_3.png](img_3.png)


# Comparando List Comprehension x Generator
List Comprehension gera a lista completa e o Generator gera sob demanda
![img_4.png](img_4.png)

![img_5.png](img_5.png)

![img_6.png](img_6.png)

# Simulando o switch case com Generator 

Complexo:

![img_7.png](img_7.png)

````

def get_tipo_dia(dia):
    dias = {
        (1, 7): 'Fim de semana',
        tuple(range(2, 7)): 'Dia de semana',
    }
    dia_escolhido = (tipo_dia for numero_dia, tipo_dia in dias.items() if
                     dia in numero_dia)
    return next(dia_escolhido, '***  dia inválido ***')
# Vai retornar o dia escolhido, senão retorna inválido

for dia in range(0, 9):
    print(f'Dia - {dia} é {get_tipo_dia(dia)}')


```
