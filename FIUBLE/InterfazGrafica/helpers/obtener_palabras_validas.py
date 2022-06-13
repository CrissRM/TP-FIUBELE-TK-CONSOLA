def obtener_palabras_validas(CANT_LETRAS):
  archivo = open("C:/Users/Commodore/Desktop/TP-GITHUB/FIUBLE/InterfazGrafica/archivos_palabras/palabras.csv")
  
  lista_palabra_secreta = []
  palabra = archivo.readline().split(",")[0]

  while palabra !="":
    if len(palabra) == CANT_LETRAS:
      lista_palabra_secreta.append(palabra)
    palabra = archivo.readline().split(",")[0]

  archivo.close() 

  return lista_palabra_secreta