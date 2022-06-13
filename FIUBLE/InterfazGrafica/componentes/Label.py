import tkinter as tk

def Label(estilo):
  Label = tk.Label(
    estilo["root"],
    text=estilo["text"],
    background=estilo["background"],
    foreground=estilo["foreground"],
    padx=estilo["padding_x"],
    pady=estilo["padding_y"],
    font=(estilo["font_family"],estilo["font_size"],estilo["font_slant"]),
    width=estilo["width"],
    anchor=estilo["anchor"]
  )
  Label.pack(side=estilo["side"],padx=estilo["margin_x"],pady=estilo["margin_y"])


