def contabilizar_puntos(puntos,ganador_parcial,turno,dicc_jugadores):
  """
  """
  if not ganador_parcial:
    
    for key in dicc_jugadores:
      if key == turno:
        dicc_jugadores[key][0] += puntos 
      else:
        dicc_jugadores[key][0] += puntos+50
  
  else:
    
    for key in dicc_jugadores:
      if key == turno:
        dicc_jugadores[key][0] += puntos
      else:
        dicc_jugadores[key][0] += -puntos

  
  return dicc_jugadores
