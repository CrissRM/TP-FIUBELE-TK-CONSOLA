def write_archivo(c_letras,cmax_partidas,reiniciar):
    lista_1=["LONGITUD_PALABRA_SECRETA","MAXIMO_PARTIDAS","REINICIAR_ARCHIVO_PARTIDAS"
    ,"CREDITOS_MAX","CANTIDAD_MAX_JUGADORES"]
    
    lista_2=[c_letras,cmax_partidas,reiniciar,"5","2"]
    archivo_config=open("archivos/configuracion.csv","w")
    for i in range (0,5) :
        archivo_config.write(str(lista_1[i])+","+str(lista_2[i])+"\n")
    archivo_config.close() 

