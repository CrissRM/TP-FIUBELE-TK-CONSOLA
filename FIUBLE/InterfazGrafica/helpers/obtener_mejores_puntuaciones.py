from helpers.handler_files import archivo_close,archivo_open,formato_linea

def obtener_mejores_puntuaciones():
  archivo = archivo_open("archivo/partidas.csv")
  archivo_close(archivo)


#-------------------------------- FRAME RANKING--------------------------------
# archivo = archivo_open("archivos/ranking.csv")

# texto = "FECHA   HORA FINALAIZACION   NOMBRE   ACIERTOS   INTENTOS\n"

# linea = formato_linea(archivo.readline(),5)

# while linea[0] !="":
#   texto +=f"{linea[0]}    -   {linea[1]}   -   {linea[2]}   -   {linea[3]}   -   {linea[4]}\n"
#   linea = formato_linea(archivo.readline(),5)

# archivo_close(archivo)

# ranking = Frame(root)


# estilo = style_label(root,texto,5,5,"Releway",15,"roman",80,"center",estilos["BACKGROUND_PRIMARY"],estilos["FOREGROUND_PRIMARY"],"top",10,10)

# Label(estilo)

#-------------------------------------------------------------------------------