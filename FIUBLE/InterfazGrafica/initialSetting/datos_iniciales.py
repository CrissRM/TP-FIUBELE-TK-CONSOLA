from random import choice
from helpers.modulos import obtener_palabras_validas,archivo_open,archivo_close,formato_linea


def iniciar_tablero(cantidad_letras):
  tablero=[]
  for i in range(cantidad_letras):
    tablero.append([ "?" for l in range(cantidad_letras)])
  return tablero

def obtener_color(letra,color):
  colores = {
  "Verde" : "\x1b[32m",
  "Amarillo" : "\x1b[33m",
  "GrisOscuro" : "\x1b[90m",
  "Defecto" : "\x1b[39m" ,
  "Rojo" : "\x1b[31m",
  "ENDC": "\x1b[0m"
  }
  return colores[color] + letra + colores["ENDC"]

def condiciones_iniciales():
  print("cargando..")
  configuraciones = []
  archivo = archivo_open("archivos/configuracion.csv")
  linea = formato_linea(archivo.readline(),2)[1] 
  while linea !="":
    configuraciones.append(linea)
    linea = formato_linea(archivo.readline(),2)[1]

  archivo_close(archivo)

  LONGITUD_PALABRA_SECRETA,MAXIMO_PARTIDAS,REINICIAR_ARCHIVO_PARTIDAS,CREDITOS_MAX,CANTIDAD_MAX_JUGADORES = configuraciones
  
  
  return {
    "tablero": iniciar_tablero(int(LONGITUD_PALABRA_SECRETA)),
    "palabra_secret": choice(obtener_palabras_validas()),
    "es_ganador": False,
    "contador_credito": 0,
    "contador_credito_max": int(CREDITOS_MAX), 
    "puntos_acomulados_jugador": 0,
    "cantidad_jugadores": int(CANTIDAD_MAX_JUGADORES),
    "cantidad_letras": int(LONGITUD_PALABRA_SECRETA),
    "max_partidas": int(MAXIMO_PARTIDAS),
    "reiniciar_archivo_partidas": bool(REINICIAR_ARCHIVO_PARTIDAS),
    "max_long_letras": 12 
  }
