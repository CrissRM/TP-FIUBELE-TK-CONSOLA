from helpers.modulos import formatear_palabra
from initialSetting.modulos import condiciones_iniciales

def validar_condicion_palabra():
  """
  """
  MAX_LETRAS = condiciones_iniciales()["cantidad_letras"]
  
  palabra=input("Arriesgo :")
  while len(palabra)!=MAX_LETRAS or (not palabra.isalpha()):
    if len(palabra)!=MAX_LETRAS:
        print(f"la palabra debe tener {MAX_LETRAS} letras y tiene {len(palabra)}")
    elif not palabra.isalpha() :
        print(f"La palabra debe contener solo letras")
    palabra=input("Arriesgo :") 
  palabra=formatear_palabra(palabra)
  """
  Aqui nos devuelve la palabra sin acentos,ver funcion especifica
  """
  return palabra.lower()
  