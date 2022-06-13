import tkinter as tk
from app.app_consola import inicia_app
from initialSetting.modulos import estilos,style_button,style_label,style_entry
from formularios.modulos import formulario_registro,formulario_ingreso
from funcionalidadButtonTk.modulos import volver
from componentes.modulos import msg_error,msg_info,msg_warning,FrameHidden,Label,Button,Frame,Entry
from initialSetting.modulos import condiciones_iniciales


def btn_registrarse(not_argument):
  form_registro = formulario_registro(root,registro,ingresar)
  form_registro.pack()
  registro["state"] = "disabled"
  ingresar["state"] = "disabled"
  
def btn_ingresar(not_argument):
  cant_jugadores.pack()
  registro["state"] = "disabled"
  ingresar["state"] = "disabled"

def handler_cant(not_argument):
  MAX_JUGADORES = condiciones_iniciales()["cantidad_jugadores"]
  try:
    cant = int(cant_entry.get())
  except ValueError:
    msg_error("No es valido. Ingresar números enteros")
  else:
    if cant <= 0:
      msg_warning("No es un valor, válido")
    elif cant<=MAX_JUGADORES:
      jugadores = []
      cant_jugadores.pack_forget() 
      form_ingreso = formulario_ingreso(root,registro,ingresar,jugadores,cant,inicia_app)
      form_ingreso.pack()
    else:
      msg_info(f"Por el momento, el juego está implementado para un máximo de {MAX_JUGADORES} jugadores")

root = tk.Tk()
root.title("FIUBLE - SERPIENTE")
root.geometry("+300+200")
root.minsize(width=700,height=400)
root.configure(background=estilos["BACKGROUND_PRIMARY"])

#------------------------------------TITULO------------------------------------
style = style_label(root,"FIUBELE-SERPIENTE",5,5,"Releway",25,"roman",25,"center",estilos["BACKGROUND_PRIMARY"],estilos["FOREGROUND_PRIMARY"],"top",10,10)

Label(style) 
#-------------------------------------------------------------------------------

#------------------------------------BOTONES------------------------------------
botones = Frame(root)



registro = Button(style_button(botones,"REGISTRARSE",5,5,"Releway",10,"normal",10,"normal","register","left",10,10),btn_registrarse,False )



ingresar = Button(style_button(botones,"INGRESAR",5,5,"Releway",10,"normal",10,"normal","signin","left",10,10),btn_ingresar,False)
#-------------------------------------------------------------------------------


#---------------------------FRAME CANTIDAD JUGADORES---------------------------
cant_jugadores = FrameHidden(root)

cant_entry = Entry(style_entry(cant_jugadores,0,1,"Releway",19,"normal","#fff","#000","left","?",3,"left",5,10,False))

Button(style_button(cant_jugadores,"CONFIRMAR",0,1.5,"Releway",13,"normal",10,"normal","register","left",5,10),handler_cant,False)

Button(style_button(cant_jugadores,"VOLVER",0,1.5,"Releway",13,"normal",10,"normal","back","left",5,10),volver,[cant_jugadores,registro,ingresar])
#-------------------------------------------------------------------------------
root.mainloop()

