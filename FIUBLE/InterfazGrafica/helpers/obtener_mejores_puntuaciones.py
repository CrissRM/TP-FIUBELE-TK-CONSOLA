from helpers.handler_files import archivo_close,archivo_open,formato_linea

def obtener_mejores_puntuaciones():
  archivo = archivo_open("archivo/partidas.csv")

  archivo_close(archivo)


#-------------------------------- FRAME RANKING--------------------------------
# texto = "JUFADOR PUNTOS\n"

# archivo = archivo_open("archivos/PARTIDAS.csv")


# linea = formato_linea(archivo.readline(),5)

# while linea[0] !="":
#   texto +=f"{linea[0]}    -   {linea[1]}\n"
#   linea = formato_linea(archivo.readline(),5)

# archivo_close(archivo)

# ranking = Frame(root)


# estilo = style_label(root,texto,5,5,"Releway",15,"roman",80,"center",estilos["BACKGROUND_PRIMARY"],estilos["FOREGROUND_PRIMARY"],"top",10,10)

# Label(estilo)

#-------------------------------------------------------------------------------
