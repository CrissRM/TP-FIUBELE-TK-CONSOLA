from random import choice
from helpers.modulos import obtener_palabras_validas

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
  CANTIDAD_LETRAS = 7
  return {
    "tablero": iniciar_tablero(CANTIDAD_LETRAS),
    "palabra_secret": choice(obtener_palabras_validas(CANTIDAD_LETRAS)),
    "es_ganador": False,
    "contador_credito": 0,
    "contador_credito_max": 5, 
    "puntos_acomulados_jugador": 0,
    "cantidad_jugadores": [x for x in range(1,3)],
    "cantidad_letras": CANTIDAD_LETRAS
  }
