def fin_juego(estadisticas_finales_jugadores):
  print("\n\n","*"*75)
  print("*"*30,"FIN  DEL JUEGO","*"*30,"\n")
  
  lista_puntucaciones = list(estadisticas_finales_jugadores.values())
  lista_puntucaciones.sort(reverse=True)
  
  for jugador,puntos in estadisticas_finales_jugadores.items():
    if puntos == lista_puntucaciones[0]:
      print(f"GANADOR: {jugador} ----> OBTUVO: {puntos}")
  
  print("\n","*"*75)
  input("\n\nEnter para finalizar...")
  print(estadisticas_finales_jugadores)
  # try:
  #   archivo = open("archivos/ranking.csv")
  #   archivo.close()
  # except FileNotFoundError:
  #   archivo = open("archivos/ranking.csv","w")
  #   archivo.close()