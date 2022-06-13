import tkinter as tk
from initialSetting.modulos import estilos
# from helpers.estilos_formatos import estilos

def FrameHidden(padre):
  Formulario = tk.Frame(
  padre,
  padx=10,
  pady=10,
  background=estilos["BACKGROUND_PRIMARY"]
)

  Formulario.pack_forget()

  return Formulario