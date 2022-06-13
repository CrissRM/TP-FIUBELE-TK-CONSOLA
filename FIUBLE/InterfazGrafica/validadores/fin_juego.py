def fin_juego(estadisticas_finales_jugadores):
  print("\n\n*****************************************************************")
  print("**************************FIN DEL JUEGO**************************\n")
  lista_puntucaciones = list(estadisticas_finales_jugadores.values())
  lista_puntucaciones.sort(reverse=True)
  
  for jugador,puntos in estadisticas_finales_jugadores.items():
    if puntos == lista_puntucaciones[0]:
      print(f"GANADOR: {jugador} ----> OBTUVO: {puntos}")
  
  print("\n*****************************************************************")
  input("\n\nEnter para finalizar...")
  