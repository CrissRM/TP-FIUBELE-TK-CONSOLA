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
  
  #ESTO SE LEE:
  # LLAVE ---> JUGADOR
  #CLAVE --> LISTA DE 5 ELEMENTOS
  # 1. PUNTOS ACOMULADOS
  # 2. FECHA
  # 3. HORA FINALIZACION
  # 4. ACIERTOS
  # 5. INTENTOS (VECES QUE INGRESO UNA PALABRA)
  print(estadisticas_finales_jugadores)
  
  # try:
  #   archivo = open("archivos/ranking.csv")
  #   archivo.close()
  # except FileNotFoundError:
  #   archivo = open("archivos/ranking.csv","w")
  #   archivo.close()