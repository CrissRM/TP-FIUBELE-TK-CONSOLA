from componentes.modulos import msg_error,msg_warning

def validar_entry(valor):
  try:
    valor_a_validar = int(valor)
  except ValueError:
    msg_error("No es valido. Ingresar números enteros")
    valor_a_validar = False
  else:
    if valor_a_validar <= 0:
      msg_warning("No es un valor, válido")
      valor_a_validar = False
  return valor_a_validar