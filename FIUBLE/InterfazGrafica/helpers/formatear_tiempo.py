import math
def formatear_tiempo(ronda_terminada): 
  """ 
  """
  inicia_juego = ronda_terminada["inicia_juego"]
  finaliza_juego = ronda_terminada["finaliza_juego"]
  time = math.floor(finaliza_juego-inicia_juego)
  horas=math.floor(time/3600)
  minutos= math.floor((time-horas*3600)/60)
  segundos= math.floor((((time-horas*3600)/60)-minutos)*60)

  return f"{horas} horas {minutos} minutos {segundos} segundos" if horas != 0 else f"{minutos} minutos {segundos} segundos"



import doctest
doctest.testmod()