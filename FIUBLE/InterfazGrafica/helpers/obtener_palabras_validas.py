from os import path

def formatear_ruta(ruta):
  path_file = ""
  for letter in ruta:
    if letter =="\\":
      path_file +="/"
    else:
      path_file +=letter
  return path_file


def obtener_palabras_validas(CANT_LETRAS):
  ruta = "C:/Users/Commodore/Desktop/TP-GITHUB/FIUBLE/InterfazGrafica/archivos_palabras/palabras.csv"
  
  # ruta = formatear_ruta(path.abspath("../archivos_palabras/palabras.csv"))
  # print(ruta)
  archivo = open(ruta)
  
  lista_palabra_secreta = []
  palabra = archivo.readline().split(",")[0]

  while palabra !="":
    if len(palabra) == CANT_LETRAS:
      lista_palabra_secreta.append(palabra)
    palabra = archivo.readline().split(",")[0]

  archivo.close() 

  return lista_palabra_secreta

