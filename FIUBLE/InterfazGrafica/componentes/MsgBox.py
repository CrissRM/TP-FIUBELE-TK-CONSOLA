from tkinter import messagebox as mb

def msg_warning(msg):
  mb.showwarning("Advertencia",msg)

def msg_error(msg):
  mb.showerror("Error",msg)

def msg_info(msg):
  mb.showinfo("Info",msg)

def msg_confirm(msg):
  return mb.askyesno("Preguntar",msg)
  