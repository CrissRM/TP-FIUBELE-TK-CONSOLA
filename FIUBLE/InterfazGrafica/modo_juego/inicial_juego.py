import os
from time import time
from random import choice
from initialSetting.datos_iniciales import condiciones_iniciales
from helpers.alternador_turnos import alternador_turnos
from helpers.contar_puntos import contar_puntos
from helpers.contabilizar_puntos import contabilizar_puntos
from helpers.parcial_juego import parcial_juego
from flujo_juego.app import app


def inicial_juego(jugadores):
  os.system("clear")
  os.system("cls")
  turno = choice(jugadores)
  
  init_jugadores = dict()
  
  for jugador in jugadores:
    init_jugadores.setdefault(jugador,condiciones_iniciales()["puntos_acomulados_jugador"])
  
  res="s"
  while res =="s":
    inicia_juego = time()
    turno =alternador_turnos(turno,jugadores)
      
    datos_iniciales = condiciones_iniciales()
    datos_iniciales["jugadores"] = init_jugadores
    
    datos_iniciales["turno"] = turno
    
    ronda_terminada = app(datos_iniciales)
      
    ronda_terminada["inicia_juego"] = inicia_juego
      
    ganador_parcial = ronda_terminada["ganador_parcial"]
    turno_jugador = ronda_terminada["turno"]
    
    
    puntos = contar_puntos(ronda_terminada["contador_credito"])
    
    dicc_jugadores = contabilizar_puntos(puntos,ganador_parcial,turno_jugador,init_jugadores)
    
    res= parcial_juego(ronda_terminada,dicc_jugadores,puntos)

    os.system("clear")
  return dicc_jugadores