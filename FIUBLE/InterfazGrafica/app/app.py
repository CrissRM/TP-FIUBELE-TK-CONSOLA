from helpers.modulos import alternador_turnos,mensaje_turno_de
from validadores.modulos import validar_condicion_palabra,validar_palabra,analizar_palabra
from initialSetting.datos_iniciales import obtener_color
from time import time

    
def application(datos_iniciales,dicc_jugadores):
  print("\x1b[33m*****************************************************************\x1b[0m")
  print("\x1b[33m**************************JUEGO INICIADO*************************\x1b[0m")
  
  tablero = datos_iniciales["tablero"]
  palabra_secret = datos_iniciales["palabra_secret"]
  contador_credito = datos_iniciales["contador_credito"]
  es_ganador = datos_iniciales["es_ganador"]
  jugadores = list(datos_iniciales["jugadores"].keys())
  turno = datos_iniciales["turno"]
  CREDITO_MAX = datos_iniciales["contador_credito_max"]
  CANTIDAD_LETRAS = datos_iniciales["cantidad_letras"]
  print(palabra_secret)
  
  while (not es_ganador) and (contador_credito< CREDITO_MAX):
    
    turno= alternador_turnos(turno,jugadores)
    mensaje_turno_de(turno)
    
    ganador_parcial = False
    
    palabra = validar_condicion_palabra()
    
    for player,data in dicc_jugadores.items():
      if player == turno:
        data[4] +=1



    if validar_palabra(palabra,palabra_secret):
      es_ganador=True 
      ganador_parcial = turno
      tablero[contador_credito] = [obtener_color( letra,"Verde" ) for letra in palabra]
      finaliza_juego = time()
    
    else:
      lista_2 = analizar_palabra(palabra,palabra_secret)
      tablero[contador_credito]=lista_2 
    
    if not es_ganador:
      contador_credito+=1
    
    if contador_credito>=CREDITO_MAX:
      finaliza_juego = time()
    
    for i in range(CANTIDAD_LETRAS): 
      print(" ".join(tablero[i]))  

  return {
    "finaliza_juego": finaliza_juego,
    "contador_credito": contador_credito,
    "ganador_parcial": ganador_parcial,
    "turno": turno,
    "cambiar_turno": alternador_turnos(turno,jugadores)
  }

  
  
  

  