def formato_linea(linea,cant_campos):
  return linea.strip("\n").split(",") if linea !="" else [""]*cant_campos

archivo = open("archivos/configuracion.csv")

linea = formato_linea(archivo.readline(),2)[1]
while linea !="":
  print(linea)
  linea = formato_linea(archivo.readline(),2)[1]

archivo.close()