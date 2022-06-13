from initialSetting.datos_iniciales import condiciones_iniciales
from helpers.formatear_nombre import formatear_nombre
import os


lista_cantidad = condiciones_iniciales()["cantidad_jugadores"]
MAXIMO = len(lista_cantidad)

def ingreso_de_jugadores():
  os.system("cls")
  print("\n\n\x1b[33m********************* REGISTRO DE JUGADORES *********************\x1b[0m")
  print("\n\n\x1b[33m*****************************************************************\x1b[0m")
  ciclar = True
  while ciclar:
    try:
      cantidad_jugadores = int(input("\nIngrese la cantidad de jugadores: "))
    except ValueError:
      print("\n\x1b[31m >>> ALERTA!!! Debe ingresar un numero\x1b[0m")
    else:
      if cantidad_jugadores not in lista_cantidad:
        print(f"\n\x1b[33mPor el momento, el juego esta implementado para un maximo de dos {MAXIMO} jugadores\x1b[0m")
      else:
        ciclar = False

  lista_jugadores = []
  for i in range(cantidad_jugadores):
    jugador = input(f"\nPor favor, ingrese el nombre del {i+1}° jugador: ")
    check,jugador = formatear_nombre(jugador)
    while not check:
      print("\n\x1b[31m>>>> ALERTA!!! Solo se aceptan caracteres alfabeticos...\x1b[0m")
      jugador = input("Por favor, ingrese un nombre valido: ")
      check,jugador = formatear_nombre(jugador)
    
    while jugador in lista_jugadores:
      print("\n\x1b[31m>>> ALERTA Debe ingresar un nombre diferente al anterior\x1b[0m")
      jugador = input("Por favor, ingrese otro nombre: ")
    
    lista_jugadores.append(jugador)
  return lista_jugadores

