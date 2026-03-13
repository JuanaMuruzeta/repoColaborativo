# repo-colaborativo

def registrar_habitos():
    habitos = []
    while True:
        actividad = input("Ingrese un hábito (o escriba 'fin' para terminar): ")
        habitos.append(actividad)
        
        if actividad == "fin":
            break
            
    return(habitos)
  
def analizar_habitos(lista):

    resultado = {}

    for actividad in lista:
        if actividad in resultado:
            resultado[actividad] = resultado[actividad] + 1
        else:
            resultado[actividad] = 1

    return resultado
         