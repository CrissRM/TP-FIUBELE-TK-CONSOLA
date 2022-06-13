from tkinter import messagebox as mb

def validar_nombre(nombre):
  if 4<= len(nombre) <=15:
    char_valido = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyzáÁéÉíÍóÓúÚ0123456789_"
    i = 0
    error = False
    while i<len(nombre) and not error:
      if nombre[i] not in char_valido:
        error = True
      i +=1
    if error:
      mb.showerror("Error","El nombre solo acepta caracteres alfabéticos, numéricos y el guión bajo")
      res = False
    else:
      res = True
  else:
    mb.showwarning("Advertencia","El nombre debe no puede tener menos de 4 o más de 15 caracteres")
    res = False
  return res
  
