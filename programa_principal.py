# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:03:55 2026

@author: Regi
"""

import funciones_habitos


lista = funciones_habitos.registrar_habitos() 
resultado = funciones_habitos.analizar_habitos(lista) 

print("Resumen de actividades:") 
print(resultado)