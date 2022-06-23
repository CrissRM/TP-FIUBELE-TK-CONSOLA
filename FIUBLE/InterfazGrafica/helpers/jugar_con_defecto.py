from componentes.MsgBox import msg_error,msg_warning


def jugar_con_defecto(lista):
  entrada_jugadores,players_entry,formulario_ingreso,root,registro,ingresar,inicia_app,MAX_JUGADORES = lista
  
  entrada_jugadores.pack()
  try:
    cant = int(players_entry)
  except ValueError:
    msg_error("No es valido. Ingresar números enteros")  
  else:
    if cant <= 0:
      msg_warning("No es un valor, válido")
    elif cant<=MAX_JUGADORES:
      jugadores = []
      entrada_jugadores.pack_forget() 
      form_ingreso = formulario_ingreso(root,registro,ingresar,jugadores,cant,inicia_app)
      form_ingreso.pack()


# try:
#       cant = int(players_entry.get())
#     except ValueError:
#       msg_error("No es valido. Ingresar números enteros")  
#     else:
#       if cant <= 0:
#         msg_warning("No es un valor, válido")
#       elif cant<=MAX_JUGADORES:
#         jugadores = []
#         entrada_jugadores.pack_forget() 
#         form_ingreso = formulario_ingreso(root,registro,ingresar,jugadores,cant,inicia_app)
#         form_ingreso.pack()