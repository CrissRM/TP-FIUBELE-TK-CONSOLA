import tkinter as tk
from initialSetting.modulos import estilos
# from helpers.estilos_formatos import estilos

def Entry(estilos):
  if estilos["is_password"]:
    Entry = tk.Entry(
      estilos["root"],
      justify=estilos["justify"],
      font=(estilos["font_family"],estilos["font_size"],estilos["font_slant"]),
      width=estilos["width"],
      background=estilos["background"],
      foreground=estilos["foreground"],
      show=estilos["show"]
    )
  else:
    Entry =tk.Entry(
      estilos["root"],
      justify=estilos["justify"],
      font=(estilos["font_family"],estilos["font_size"],estilos["font_slant"]),
      width=estilos["width"],
      background=estilos["background"],
      foreground=estilos["foreground"],
      
    )
    
  Entry.pack(side=estilos["side"],padx=estilos["mgx"],pady=estilos["mgy"])
  
  return Entry

    