def archivo_open(archivo,modo="r"):
  return open(archivo,modo)

def archivo_close(archivo):
  archivo.close()

def formato_linea(linea,cant_campos):
  return linea.strip("\n").split(",") if linea !="" else [""]*cant_campos