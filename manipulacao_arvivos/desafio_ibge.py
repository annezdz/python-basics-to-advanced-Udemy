import csv
from urllib import request


def read_anne():
    with open('desafio-ibge.csv', encoding='utf-8') as entrada:
        for campo in csv.reader(entrada):
            print(f'{campo[3]} - {campo[8]}')


# read_anne()

def read(url):
    with request.urlopen(url) as entrada:
        print('Baixando')
        dados = entrada.read().decode('latin-1')
        print('Download Complete')
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}: {cidade[3]}')


# read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')


def read_anne_upgrade(url):
    with request.urlopen(url) as entrada:
        for campo in csv.reader(entrada.read().decode('latin-1').splitlines()):
            print(f'{campo[3]} - {campo[8]}')


read_anne_upgrade(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')