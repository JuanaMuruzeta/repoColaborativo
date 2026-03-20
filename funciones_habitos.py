# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 17:47:01 2026

@author: Regi
"""

def registrar_habitos():

    """
    Permite registrar habitos o actividadesingresadas por el usuario y guardarlas en una lista hasta que el usuario decida finalizar.
    
    Parametros
    ------------
    No recibe Parametros

    Returns
    -------
    habitos= lista
    Lista de los habitos ingresados.

    """
    habitos = []
    while True:
        actividad = input("Ingrese un hábito (o escriba 'fin' para terminar): ")
        habitos.append(actividad)
        
        if actividad == "fin":
            break
            
    return(habitos)
  
def analizar_habitos(lista):

    """
    Cuenta cuantas veces aparece cada actividad en la lista.
    
    Parametros
    ------------
    Lista = lista
    
    Returns
    -------
    resultado = diccionario
    Diccionario con cada actividad y la cantidad de veces que aparece.

    """


    resultado = {}

    for actividad in lista:
        if actividad in resultado:
            resultado[actividad] = resultado[actividad] + 1
        else:
            resultado[actividad] = 1

    return resultado
         
         

