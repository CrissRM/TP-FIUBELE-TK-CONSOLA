from importaciones.import_file import Label,Entry,Frame,FrameHidden,Button,style_button,style_entry,style_label,estilos,volver,guardar

def formulario_registro(root,btn_registro,btn_ingreso):
  form_registro = FrameHidden(root)
  
  #-----------------------------------------------------------------------------
  data_nombre = Frame(form_registro)
  
  Label(style_label(data_nombre,"Nombre: ",5,5,"Releway",12,"roman",15,"w",estilos["BACKGROUND_PRIMARY"],estilos["FOREGROUND_PRIMARY"],"left",10,10))

  nombre_entry = Entry(style_entry(data_nombre,0,0,"Releway",15,"normal","#fff","#000","left","?",15,"left",10,10,False))
  #-----------------------------------------------------------------------------
  data_clave = Frame(form_registro)

  Label(style_label(data_clave,"Contraseña: ",5,5,"Releway",12,"roman",15,"w",estilos["BACKGROUND_PRIMARY"],estilos["FOREGROUND_PRIMARY"],"left",10,10))
  
  clave_entry = Entry(style_entry(data_clave,0,0,"Releway",15,"normal","#fff","#000","left","*",15,"left",10,10,True))
  #-----------------------------------------------------------------------------
  data_clave_repeat =Frame(form_registro)
  
  Label(style_label(data_clave_repeat,"Repetir Contraseña: ",5,5,"Releway",12,"roman",15,"w",estilos["BACKGROUND_PRIMARY"],estilos["FOREGROUND_PRIMARY"],"left",10,10))
  
  clave_entry_repeat = Entry(style_entry(data_clave_repeat,0,0,"Releway",15,"normal","#fff","#000","left","*",15,"left",10,10,True))
  #-----------------------------------------------------------------------------
  
# --------------------------BOTONES OPCIONES--------------------------
  botones = Frame(form_registro)
  
  Button(style_button(botones,"VOLVER",5,5,"Releway",10,"normal",10,"normal","back","left",10,10),volver,[form_registro,btn_ingreso,btn_registro])
  
  Button(style_button(botones,"GUARDAR",5,5,"Releway",10,"normal",10,"normal","send","left",10,10),guardar,[form_registro,btn_registro,btn_ingreso,nombre_entry,clave_entry,clave_entry_repeat],)
  
  return form_registro