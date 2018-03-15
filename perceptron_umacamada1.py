"""
Created on Thu Mar 15 13:15:04 2018

@author: Maikon

perceptron de uma cada.
"""

#perceptron de uma camada

#entradas positivas
entradas = [1, 7, 5]
pesos = [0.8, 0.1, 0]

#entradas negativas
entradas1 = [-1, 7, 5]
pesos1 = [0.8, 0.1, 0]

def soma(entrada, peso):
    soma = 0;
    
    #nao e a melhor forma de efetuar o calculo, pode deixar a rede lenta
    for i in range(entrada.length):
        soma += entrada[i] * peso[i]
    
    
    return soma
        
#resultado = soma(entradas, pesos)

def stepFunction(soma):
    if(soma >= 1):
        return 1
    
    return 0


resultado1 = stepFunction(soma(entradas, pesos)) #neoronio sera ativado
resultado2 = stepFunction(soma(entradas1, pesos1)) #neoronio nao sera ativado