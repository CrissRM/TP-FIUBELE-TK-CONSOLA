from helpers.msg_puntos_parciales import msg_puntos_parciales

def parcial_juego(ronda_terminada,dicc_jugadores,puntos):
  
  msg_puntos_parciales(puntos,ronda_terminada,dicc_jugadores)
  
  print("\n\n\x1b[33m*****************************************************************\x1b[0m")
  
  res = input("¿ Desean seguir jugando ? (s/n): ") .lower()
  while res !="s" and res !="n":
    print("\nDebe ingresar 's' o 'n'")
    res = input("¿ Desean seguir jugando ? (s/n): ") .lower()
  return res
  