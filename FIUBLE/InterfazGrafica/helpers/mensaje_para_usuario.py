from helpers.formatear_tiempo import formatear_tiempo

def mensaje_para_usurio(dicc_jugadores,puntos_ronda,ronda_terminada):
  
  print("\n\x1b[33m*****************************PUNTAJES****************************\x1b[0m")
  
  print(f"\n\x1b[33m                    {'       JUGADOR      ':7} | {'PUNTOS':6} | {'ACOMULADO':9} |\x1b[0m")
  
  if ronda_terminada["ganador_parcial"]:
    for jugador,puntos in dicc_jugadores.items():
      if puntos<0:
        if ronda_terminada["ganador_parcial"] == jugador:
          print(f"\n                    {jugador:20} | {puntos_ronda:6} | \x1b[31m{puntos:9}\x1b[0m |")
        else:
          print(f"\n                    {jugador:20} | {-puntos_ronda:6} | \x1b[31m{puntos:9}\x1b[0m |")
      else:
        if ronda_terminada["ganador_parcial"] == jugador:
          print(f"\n                    {jugador:20} | {puntos_ronda:6} | \x1b[32m{puntos:9}\x1b[0m |")
        else:
          print(f"\n                    {jugador:20} | {-puntos_ronda:6} | \x1b[32m{puntos:9}\x1b[0m |")
    
    
    print(f"\n          Tiempo en adiviniar la palabra: {formatear_tiempo(ronda_terminada)}") 

  else:
    for jugador,puntos in dicc_jugadores.items():
      if puntos<0:
        if ronda_terminada["turno"] == jugador:
          print(f"\n                    {jugador:20} | {puntos_ronda:6} | \x1b[31m{puntos:9}\x1b[0m |")
        else: 
          print(f"\n                    {jugador:20} | {puntos_ronda+50:6} | \x1b[31m{puntos:9}\x1b[0m |")
      else:
        if ronda_terminada["turno"] == jugador:
          print(f"\n                    {jugador:20} | {puntos_ronda:6} | \x1b[32m{puntos:9}\x1b[0m |")
        else:
          print(f"\n                    {jugador:20} | {puntos_ronda+50:6} | \x1b[31m{puntos:9}\x1b[0m |")

