# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 13:15:04 2018

@author: Maikon

perceptron de uma cada.
"""

import numpy as np

#problema AND da computação
entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]]) #inputs
saidas = np.array([0, 0, 0, 1]) #como devem ser
pesos = np.array([0.0, 0.0]) #sinapses
taxaAprendizagem = 0.1 #taxa de aprendizagem da rede

def stepFunction(soma):
    if(soma >= 1):
        return 1
    
    return 0 

def calculaSaida(registro):
    soma = registro.dot(pesos) #produto escalar
    
    return stepFunction(soma)

#treina rede neural
def treinar():
    erroTotal = 1 #definido como 1 para entrar no loop
    
    while (erroTotal != 0):
        erroTotal = 0
        
        for i in range(len(saidas)):
            saidaCalculada = calculaSaida(np.asarray(entradas[i]))
            erro = abs(saidas[i] - saidaCalculada)
            erroTotal += erro
            
            #Atualiza os pesos
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro)
                print('Peso atualizado: ' + str(pesos[j]))
        print('Total de erros: ' + str(erroTotal))        
        
        
treinar()