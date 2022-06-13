from helpers.modulos import msg_puntos_parciales

def parcial_juego(ronda_terminada,dicc_jugadores,puntos):
  
  msg_puntos_parciales(puntos,ronda_terminada,dicc_jugadores)
  
  print("\n\n\x1b[33m","*"*75,"\x1b[0m")
  
  res = input(" ¿ Desean seguir jugando ? (s/n): ") .lower()
  while res !="s" and res !="n":
    print("\n Debe ingresar 's' o 'n'")
    res = input(" ¿ Desean seguir jugando ? (s/n): ") .lower()
  return res
  