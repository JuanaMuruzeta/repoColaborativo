# repo-colaborativo

def registrar_habitos():
    habitos = []
    while True:
        actividad = input("Ingrese un hábito (o escriba 'fin' para terminar): ")
        habitos.append(actividad)
        
        if actividad == "fin":
            break
            
    return(habitos)
  
  
         