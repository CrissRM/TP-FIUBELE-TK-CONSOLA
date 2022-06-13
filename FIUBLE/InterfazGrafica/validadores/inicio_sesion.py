from componentes.modulos import msg_error
from helpers.modulos import formato_linea

def inicio_sesion(nombre,contrasenia):
  existe = False
  try:
    with open("jugadores.csv","r") as archivo_csv:
      jugador,password = formato_linea(archivo_csv.readline())
      while jugador !="" and not existe:
        if jugador == nombre and password == contrasenia:
          existe  = True
        jugador,password = formato_linea(archivo_csv.readline())
  except FileNotFoundError:
    msg_error("No hay usuarios registrados")
    
    
  return existe

