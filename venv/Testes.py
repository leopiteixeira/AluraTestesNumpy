import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 10)

Zero = np.loadtxt('data/carros-zero-km.txt')
anos = np.loadtxt('data/carros-anos.txt')
valores = np.loadtxt('data/carros-valor.txt')

carros = np.column_stack((valores, anos, Zero)).T

# print(carros[2])
# print(carros)

#Criando o dataframe
dataset = pd.read_csv('data/db.csv', sep=';')

#Selecionando os carros com Motor 4.0 Turbo e fazendo a Media de preços
datasetM4 = dataset.query('Motor == "Motor 4.0 Turbo"')
mediaValoresM4 = np.array([i[1].Valor for i in datasetM4.iterrows()]).mean()

#Selecionando os carros com Motor 1.8 16v e fazendo a Media de preços
datasetM18 = dataset.query('Motor == "Motor 1.8 16v"')
mediaValoresM18 = np.array([i[1].Valor for i in datasetM18.iterrows()]).mean()

#Imprimindo no console
print(f'Media de Preço dos carros com Motor 4.0 Turbo: {mediaValoresM4:.2f}R$')
print(f'Media de Preço dos carros com Motor 1.8 16v: {mediaValoresM18:.2f}R$')
print(f'diferença de preço entre Motor 4.0 Turbo X Motor 1.8 16v: {mediaValoresM4-mediaValoresM18:.2f}R$')

