from componentes.modulos import FrameHidden,Frame,Label,Entry,Button,msg_warning
from initialSetting.modulos import style_label,style_entry,style_button,estilos,condiciones_iniciales
from funcionalidadButtonTk.modulos import volver
from app.app_consola import inicia_app
from validadores.validar_entry import validar_entry
from formularios.modulos import formulario_ingreso
from helpers.write_config import write_archivo
from archivos_apareo.diccionario_de_palabras import diccionario_de_palabras

def confirmar(lista):
  players_entry,configuraciones,root,registro,ingresar,letras_entry,partidas_entry = lista

  MAX_JUGADORES = condiciones_iniciales()["cantidad_jugadores"]
  MAX_LONG_LETRAS = condiciones_iniciales()["max_long_letras"]
  MAX_PARTIDAS = condiciones_iniciales()["max_partidas"]

  cantidad_jugadores = validar_entry(players_entry.get())
  cantidad_letras = validar_entry(letras_entry.get())
  cantidad_partidas = validar_entry(partidas_entry.get())

  if cantidad_jugadores and cantidad_letras and cantidad_partidas:
    if cantidad_jugadores> MAX_JUGADORES:
      msg_warning(f"El juego esta implementado para un maximo de {MAX_JUGADORES} jugadores")
    elif cantidad_letras> MAX_LONG_LETRAS:
      msg_warning(f"La cantidad de letras por palabra no puede ser mayor {MAX_LONG_LETRAS}")
    elif cantidad_partidas>MAX_PARTIDAS:
      msg_warning(f"El juego no puede tener un numero de partidas mayor a {MAX_PARTIDAS}")
    else:
      configuraciones.pack_forget()
      jugadores = []
      reiniciar =False
      
      write_archivo(cantidad_letras,cantidad_partidas,reiniciar)
      diccionario_de_palabras()
      formulario_ingreso(root,registro,ingresar,jugadores,cantidad_jugadores,inicia_app).pack()
    

def formulario_configuracion_personalizada(root,registro,ingresar):
  configuraciones = FrameHidden(root) 

  #---CANT JUGADORES
  cant_jugadores = Frame(configuraciones)

  Label(style_label(cant_jugadores,"Jugadores: ",5,5,"Releway",12,"roman",15,"w",estilos["BACKGROUND_PRIMARY"],estilos["FOREGROUND_PRIMARY"],"left",10,10))

  players_entry = Entry(style_entry(cant_jugadores,0,1,"Releway",19,"normal","#fff","#000","left","?",3,"left",5,10,False))

  #--LONG PALABRA
  longitud_palabra = Frame(configuraciones)

  Label(style_label(longitud_palabra,"Letras: ",5,5,"Releway",12,"roman",15,"w",estilos["BACKGROUND_PRIMARY"],estilos["FOREGROUND_PRIMARY"],"left",10,10))
  
  letras_entry = Entry(style_entry(longitud_palabra,0,1,"Releway",19,"normal","#fff","#000","left","?",3,"left",5,10,False))

  #--- CANT PARTIDAS
  cantidad_partidas = Frame(configuraciones)
  Label(style_label(cantidad_partidas,"Partidas: ",5,5,"Releway",12,"roman",15,"w",estilos["BACKGROUND_PRIMARY"],estilos["FOREGROUND_PRIMARY"],"left",10,10))

  partidas_entry = Entry(style_entry(cantidad_partidas,0,1,"Releway",19,"normal","#fff","#000","left","?",3,"left",5,10,False))
  #-----------------------------------------------------------------------------
  frame_botones = Frame(configuraciones)
  
  Button(style_button(frame_botones,"CONFIRMAR",0,1.5,"Releway",13,"normal",10,"normal","register","left",5,10),confirmar,[players_entry,configuraciones,root,registro,ingresar,letras_entry,partidas_entry])

  Button(style_button(frame_botones,"VOLVER",0,1.5,"Releway",13,"normal",10,"normal","back","left",5,10),volver,[configuraciones,registro,ingresar])

  return configuraciones