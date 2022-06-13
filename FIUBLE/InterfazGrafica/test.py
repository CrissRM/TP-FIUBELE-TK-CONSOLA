def format(linea,cant):
  return linea.strip("\n").split(",") if linea != "" else [""]*cant

archivo = open("archivos/ranking.csv")
linea = format(archivo.readline(),5)
while linea[0] !="":
  print(linea)
  linea = format(archivo.readline(),5)
archivo.close()
