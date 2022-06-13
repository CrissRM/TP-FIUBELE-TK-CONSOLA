def grabar_datos(nombre,password):
  with open("archivos/jugadores.csv","a") as jugadores:
    
    jugadores.write(f"{nombre},{password}\n")