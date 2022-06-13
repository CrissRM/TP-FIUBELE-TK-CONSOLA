import os
from time import time
from random import choice
from initialSetting.modulos import condiciones_iniciales
from app.app import application
from datetime import datetime
from helpers.modulos import alternador_turnos,contar_puntos,contabilizar_puntos,parcial_juego


def inicia_juego(jugadores):
  os.system("clear")
  os.system("cls")
  turno = choice(jugadores) 
  
  init_jugadores = dict()
  
  for jugador in jugadores:
    puntos_iniciales = condiciones_iniciales()["puntos_acomulados_jugador"]
    fecha = datetime.today().strftime("%d-%m-%Y")
    hora_finalizacion = ""
    aciertos = 0
    intentos = 0
    
    init_jugadores.setdefault(jugador,[puntos_iniciales,fecha,hora_finalizacion,aciertos,intentos])
  
  res="s"
  numero_partida = 0
  while res =="s" and numero_partida<condiciones_iniciales()["max_partidas"]:
    numero_partida +=1
    inicia_juego = time()
    turno =alternador_turnos(turno,jugadores)
      
    datos_iniciales = condiciones_iniciales()
    datos_iniciales["jugadores"] = init_jugadores
    
    datos_iniciales["turno"] = turno
    
    ronda_terminada = application(datos_iniciales,init_jugadores)
      
    ronda_terminada["inicia_juego"] = inicia_juego
      
    ganador_parcial = ronda_terminada["ganador_parcial"]
    turno_jugador = ronda_terminada["turno"]
    
    
    puntos = contar_puntos(ronda_terminada["contador_credito"])
    
    dicc_jugadores = contabilizar_puntos(puntos,ganador_parcial,turno_jugador,init_jugadores)
    
    res= parcial_juego(ronda_terminada,dicc_jugadores,puntos)

    os.system("clear")
  return dicc_jugadores