def grabar_datos(nombre,password):
  with open("jugadores.csv","a") as jugadores:
    
    jugadores.write(f"{nombre},{password}\n")