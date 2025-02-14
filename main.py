'''
5-Em um arquivo chamado main.py, importe a classe Carro.

6-No arquivo main.py, instancie três objetos da classe Carro com diferentes características, como marca, modelo e cor.
'''

from modelos.carro import Carro

carro_1 = Carro('Fiat', 'Toro', 'Vermelo')
carro_2 = Carro('VW', 'Golf', 'Amarelo')
carro_3 = Carro('Chevorlet', 'S10', 'Branco')

print(f'{carro_1._marca} {carro_1._modelo} - COR: {carro_1.cor}')
print(f'{carro_2._marca} {carro_2._modelo} - COR: {carro_2.cor}')
print(f'{carro_3._marca} {carro_3._modelo} - COR: {carro_3.cor}')