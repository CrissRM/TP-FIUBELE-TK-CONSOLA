import tkinter as tk
from initialSetting.modulos import estilos,style_button,style_label
from formularios.modulos import formulario_registro
from formularios.formulario_configuracion_personalizada import formulario_configuracion_personalizada
from formularios.formulario_configuracion_defecto import formulario_configuracion_defecto
from componentes.modulos import msg_confirm,Label,Button,Frame



def btn_registrarse(not_argument):
  form_registro = formulario_registro(root,registro,ingresar)
  form_registro.pack()
  registro["state"] = "disabled"
  ingresar["state"] = "disabled"
  
def btn_ingresar(not_argument):
  registro["state"] = "disabled"
  ingresar["state"] = "disabled"
  res = msg_confirm("¿Quiere usar las configuraciones por defecto ?")
  configuracion_defecto.pack() if res else configuracion_personalizada .pack()



root = tk.Tk()
root.title("FIUBLE - SERPIENTE")
root.geometry("+300+200")
root.minsize(width=700,height=400)
root.configure(background=estilos["BACKGROUND_PRIMARY"])

#------------------------------------TITULO------------------------------------
style = style_label(root,"FIUBLE-SERPIENTE",5,5,"Releway",25,"roman",25,"center",estilos["BACKGROUND_PRIMARY"],estilos["FOREGROUND_PRIMARY"],"top",10,10)

Label(style) 
#-------------------------------------------------------------------------------

#------------------------------------BOTONES------------------------------------
botones = Frame(root)

registro = Button(style_button(botones,"REGISTRARSE",5,5,"Releway",10,"normal",10,"normal","register","left",10,10),btn_registrarse,False )

ingresar = Button(style_button(botones,"INGRESAR",5,5,"Releway",10,"normal",10,"normal","signin","left",10,10),btn_ingresar,False)

#-------------------------------------------------------------------------------

configuracion_defecto =formulario_configuracion_defecto(root,registro,ingresar)

configuracion_personalizada = formulario_configuracion_personalizada(root,registro,ingresar)
#-------------------------------------------------------------------------------






root.mainloop()
