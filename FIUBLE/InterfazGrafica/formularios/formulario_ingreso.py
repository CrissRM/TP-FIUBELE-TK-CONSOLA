from importaciones.import_file import FrameHidden,Frame,Label,Entry,Button,estilos,style_button,style_entry,style_label,volver,acceder

def formulario_ingreso(root,btn_registro,btn_ingreso,jugadores,cant,inicia_app):
  
  form_ingreso = FrameHidden(root) 
  #-----------------------------------------------------------------------------
  data_nombre = Frame(form_ingreso)
  
  style = style_label(data_nombre,"Nombre: ",5,5,"Releway",12,"roman",15,"w",estilos["BACKGROUND_PRIMARY"],estilos["FOREGROUND_PRIMARY"],"left",10,10)
  Label(style)
  
  nombre_entry = Entry(style_entry(data_nombre,0,0,"Releway",15,"normal","#fff","#000","left","?",15,"left",10,10,False))
  #-----------------------------------------------------------------------------
  data_clave = Frame(form_ingreso)
  
  style = style_label(data_clave,"Contraseña: ",5,5,"Releway",12,"roman",15,"w",estilos["BACKGROUND_PRIMARY"],estilos["FOREGROUND_PRIMARY"],"left",10,10)
  Label(style)
  
  clave_entry = Entry(style_entry(data_clave,0,0,"Releway",15,"normal","#fff","#000","left","*",15,"left",10,10,True))
  #-----------------------------------------------------------------------------
  botones = Frame(form_ingreso)

  style = style_button(botones,"VOLVER",5,5,"Releway",10,"normal",10,"normal","back","left",10,10)
  Button(style,volver,[form_ingreso,btn_ingreso,btn_registro])

  style = style_button(botones,"ACCEDER",5,5,"Releway",10,"normal",10,"normal","send","left",10,10)
  Button(style,acceder,[nombre_entry,clave_entry,jugadores,cant,inicia_app,root])
  #----------------------------------------------------------------------------
  
  return form_ingreso
  