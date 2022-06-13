from componentes.MsgBox import msg_warning,msg_error,msg_info,msg_confirm
from validadores.validar_nombre import validar_nombre
from validadores.validar_contrasenia import validar_contrasenia
from validadores.existe_usuario import existe_usuario
from validadores.inicio_sesion import inicio_sesion 
from helpers.grabar_datos import grabar_datos


def volver(argumentos):
  frame_hidden,btn_registro,btn_ingreso = argumentos
  frame_hidden.pack_forget()
  btn_ingreso["state"] = "normal"
  btn_registro["state"] = "normal"

def acceder(argumentos):
  nombre_entry,clave_entry,jugadores,cant,inicia_app,root = argumentos 
  nombre = nombre_entry.get()
  password = clave_entry.get()
  
  if nombre =="":
    msg_warning("El campo nombre es requerido")
  else:
    usuario_valido = validar_nombre(nombre)

  if password =="":
    msg_warning("El campo contraseña es requerido")
  else:
    password_valida = validar_contrasenia(password)
    
  if usuario_valido and password_valida:
    if inicio_sesion(nombre,password):
      if nombre in jugadores:
        msg_warning(f"El usuario {nombre} ya inicio sesión  ")
      else:
        jugadores.append(nombre)
        msg_info("Sesión Iniciada correctamente")
        nombre_entry.delete(0,"end")
        clave_entry.delete(0,"end")
        
    else:
      msg_error("Contraseña y/o usuario no son incorrectas")
  
  if len(jugadores) == cant:
    root.destroy()
    inicia_app(jugadores)

def guardar(argumentos):
  
  form_registro,btn_registro,btn_ingreso,nombre_entry,clave_entry,clave_entry_repeat = argumentos
  nombre = nombre_entry.get()
  password = clave_entry.get()
  password_repeat = clave_entry_repeat.get()
  if nombre =="" and password =="":
    msg_warning("Los camos nombre y contraseña son requeridos")
  elif nombre =="":
    msg_warning("El campo nombre es requerido")
  elif password =="":
    msg_warning("El campo contraseña es requerido")
  elif password !=password_repeat:
    msg_error("Las contraseñas no coinciden")
  else:
    if validar_nombre(nombre) and validar_contrasenia(password):
      if existe_usuario(nombre):
        msg_warning("El usuario ya existe")
      else:
        grabar_datos(nombre,password)
        msg_info("Usuario registrado con éxito")
        res = msg_confirm("¿Quiere registrar otro usuario?")
        if res:
          nombre_entry.delete(0,"end")
          clave_entry.delete(0,"end")
          clave_entry_repeat.delete(0,"end")
        else:
          volver([form_registro,btn_registro,btn_ingreso])