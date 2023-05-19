import numpy as np

Zero = np.loadtxt('data/carros-zero-km.txt')
anos = np.loadtxt('data/carros-anos.txt')
valor = np.loadtxt('data/carros-valor.txt')

carros = np.column_stack((valor, anos, Zero)).T

print(carros[2])
print(carros)