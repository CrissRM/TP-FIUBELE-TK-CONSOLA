from random import choice

def alternador_turnos(turno,jugadores):
  """
  """
  if len(jugadores) >1:
    
    nueva_lista = [jugador for jugador in jugadores if jugador != turno]
    turno = choice(nueva_lista)
  else:
    turno = jugadores[0]
  return turno

