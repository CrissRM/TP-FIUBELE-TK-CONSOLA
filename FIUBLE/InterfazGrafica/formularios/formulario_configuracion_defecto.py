from componentes.modulos import FrameHidden,Frame,Label,Button,Entry,msg_warning
from initialSetting.modulos import style_button,style_label,style_entry,estilos,condiciones_iniciales
from funcionalidadButtonTk.modulos import volver
from validadores.validar_entry import validar_entry
from formularios.modulos import formulario_ingreso
from app.app_consola import inicia_app
from archivos_apareo.diccionario_de_palabras import diccionario_de_palabras

def confirmar(lista):
  players_entry,entrada_jugadores,root,registro,ingresar = lista
  MAX_JUGADORES = condiciones_iniciales()["cantidad_jugadores"]
  cantidad = validar_entry(players_entry.get())

  if cantidad and cantidad<= MAX_JUGADORES:
      entrada_jugadores.pack_forget()
      jugadores = []
      diccionario_de_palabras()
      formulario_ingreso(root,registro,ingresar,jugadores,cantidad,inicia_app).pack() 
  elif cantidad:
    msg_warning("El juego esta implementado para un maximo de 2 jugadores")

def formulario_configuracion_defecto(root,registro,ingresar):
  entrada_jugadores = FrameHidden(root)

  players = Frame(entrada_jugadores)
  Label(style_label(players,"Jugadores: ",5,5,"Releway",12,"roman",15,"w",estilos["BACKGROUND_PRIMARY"],estilos["FOREGROUND_PRIMARY"],"left",10,10))

  players_entry = Entry(style_entry(players,0,1,"Releway",19,"normal","#fff","#000","left","?",3,"left",5,10,False))
  #-------------------------------------------------------------------------------
  frame_btn = Frame(entrada_jugadores)
  Button(style_button(frame_btn,"CONFIRMAR",0,1.5,"Releway",13,"normal",10,"normal","register","left",5,10),confirmar,[players_entry,entrada_jugadores,root,registro,ingresar])

  Button(style_button(frame_btn,"VOLVER",0,1.5,"Releway",13,"normal",10,"normal","back","left",5,10),volver,[entrada_jugadores,registro,ingresar])

  return entrada_jugadores
