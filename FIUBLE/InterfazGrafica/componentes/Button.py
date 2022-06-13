# from estilos_formatos import button_style
from initialSetting.modulos import estilos,button_style
import tkinter as tk

def Button(estilos,comando,arg): 
  
  Boton = tk.Button(
    estilos["root"],
    text=estilos["text"],
    font=(estilos["font_family"],estilos["font_size"],estilos["font_slant"]),
    background=button_style(estilos["button_style"])[0],
    foreground=button_style(estilos["button_style"])[1],
    activebackground=button_style(estilos["button_style"])[2],
    padx=estilos["padding_x"],
    pady=estilos["padding_y"],
    state=estilos["state"],
    command= lambda: comando(arg)
  )

  Boton.pack(side=estilos["side"],padx=estilos["margin_x"],pady=estilos["margin_y"])
  return Boton