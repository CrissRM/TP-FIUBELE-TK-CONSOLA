dicc_palabra = {}

def leer_Archivo(archivo):
    linea = archivo.readline()
    if linea !="":
        respuesta=linea.rstrip('\n').rstrip(',').rstrip('.').rstrip(';').rstrip('!').rstrip('¡').rstrip("?").rstrip('¿').rstrip('-').rstrip('_').rstrip('"').rstrip('*').rstrip('<<').rstrip('>>').split(' ') 
    else :
        respuesta=[""]
    return respuesta

def analizador_texto(texto,num_text,LONG):
  palabras=leer_Archivo(texto)
  while (palabras !=[""]):
    for palabra in palabras :
      if (palabra.isalpha()) and (palabra!="") and (len(palabra)==LONG) :
        if palabra.lower() in palabras:
          palabras[palabra.lower()][1]+=1
        else:
          if num_text ==1:
            dicc_palabra.setdefault(palabra.lower(),[1,0,0])
          elif num_text ==2:
            dicc_palabra.setdefault(palabra.lower(),[0,1,0])
          else:
            dicc_palabra.setdefault(palabra.lower(),[0,0,1])
    palabra=leer_Archivo(texto)

archivo = open("archivos/Cuentos.csv")
analizador_texto(archivo,1,7)
archivo.close()