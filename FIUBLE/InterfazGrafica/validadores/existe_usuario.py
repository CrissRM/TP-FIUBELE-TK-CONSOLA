def existe_usuario(nombre):
  existe = False
  try:
    with open("jugadores.csv","r") as archivo_csv:
      jugador = archivo_csv.readline().strip("\n").split(",")[0]
      while jugador !="" and not existe:
        if jugador == nombre:
          existe  = True
        jugador = archivo_csv.readline().strip("\n").split(",")[0]
  except FileNotFoundError:
    with open("jugadores.csv","w") as archivo_csv:
      pass
    
  return existe