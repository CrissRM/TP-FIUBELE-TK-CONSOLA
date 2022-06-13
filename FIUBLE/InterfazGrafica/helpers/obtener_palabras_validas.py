from helpers.formatear_palabra import formatear_palabra

def formatear_ruta(ruta):
  path_file = ""
  for letter in ruta:
    if letter =="\\":
      path_file +="/"
    else:
      path_file +=letter
  return path_file


def obtener_palabras_validas(CANT_LETRAS):

  archivo = open("archivos/palabras.csv")
  
  lista_palabra_secreta = []
  palabra = archivo.readline().split(",")[0]

  while palabra !="":
    if len(palabra) == CANT_LETRAS:
      lista_palabra_secreta.append(formatear_palabra(palabra))
    palabra = archivo.readline().split(",")[0]

  archivo.close() 

  return lista_palabra_secreta

