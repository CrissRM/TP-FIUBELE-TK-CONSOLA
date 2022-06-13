from helpers.mensaje_para_usuario import mensaje_para_usurio

def msg_puntos_parciales(puntos,ronda_terminada,dicc_jugadores):

  if not ronda_terminada["ganador_parcial"]:
    mensaje_para_usurio(dicc_jugadores,puntos,ronda_terminada)
  else:
    mensaje_para_usurio(dicc_jugadores,puntos,ronda_terminada)
    
