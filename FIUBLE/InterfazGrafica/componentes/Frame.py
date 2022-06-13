import tkinter as tk
from helpers.estilos_formatos import estilos

def Frame(padre):
  Frame = tk.Frame(
    padre,
    padx=10,
    pady=10,
    background=estilos["BACKGROUND_PRIMARY"],
    relief=estilos["BORDER_GROOVE"]
  )

  Frame.pack()

  return Frame