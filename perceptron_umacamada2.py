"""
Created on Thu Mar 15 13:15:04 2018

@author: Maikon

perceptron de uma cada.
"""
#perceptron de uma camada

import numpy as np

#entradas positivas
entradas = np.array([1, 7, 5])
pesos = np.array([0.8, 0.1, 0])

#entradas negativas
entradas1 = np.array([-1, 7, 5])
pesos1 = np.array([0.8, 0.1, 0])

def soma(entrada, peso):
    #forma correta e mais performatica 
    return entrada.dot(peso) #dot - produto escalar

def stepFunction(soma):
    if(soma >= 1):
        return 1
    
    return 0


resultado1 = stepFunction(soma(entradas, pesos)) #neoronio sera ativado
resultado2 = stepFunction(soma(entradas1, pesos1)) #neoronio nao sera ativado


##exemplo treinamento classificacao com pesos pre-definidos 
entradas_parafusos = np.array([1, 2])
pesos_parafusos = np.array([0.21, 0.22]) #pesos por enquanto são aleatorios

resultado_parafuso = stepFunction(soma(entradas_parafusos, pesos_parafusos))

if(resultado_parafuso >= 1):
    print('Classe B')
else:
    print('Classe A')

