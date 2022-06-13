from datetime import datetime

def fin_juego(estadisticas_finales_jugadores):
  print("\n\n","*"*75)
  print("*"*30,"FIN  DEL JUEGO","*"*30,"\n")
  
  lista_puntucaciones = list(estadisticas_finales_jugadores.values())
  lista_puntucaciones.sort(reverse=True)
  
  for jugador,data in estadisticas_finales_jugadores.items():
    hora_finalizacion = datetime.today().strftime("%H:%M:%S")
    estadisticas_finales_jugadores[jugador][2] =hora_finalizacion
    if data[0] == lista_puntucaciones[0][0]:
      print(f"GANADOR: {jugador} ----> OBTUVO: {data[0]}")
  
  print("\n","*"*75)
  input("\n\nEnter para finalizar...")
  
  #estadisticas_finales_jugadores ----> SE LEE:
  # LLAVE ---> JUGADOR
  #CLAVE --> LISTA DE 5 ELEMENTOS
  # 0. PUNTOS ACOMULADOS
  # 1. FECHA
  # 2. HORA FINALIZACION
  # 3. ACIERTOS
  # 4. INTENTOS (VECES QUE INGRESO UNA PALABRA)
  
  
  
  archivo = open("archivos/partidas.csv","a+")
  for jugador,data in estadisticas_finales_jugadores.items():
    archivo.write(f"{data[1]},{data[2]},{jugador},{data[3]},{data[4]},{data[0]}\n")
  archivo.close()
  