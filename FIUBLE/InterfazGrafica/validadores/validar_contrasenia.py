from tkinter import messagebox as mb

caracteres_validos ={
  "A":1,"Á":1,
  "B":2,
  "C":3,
  "D":4,
  "E":5,"É":5,
  "F":6,
  "G":7,
  "H":8,
  "I":9,"Í":9,
  "J":10,
  "K":11,
  "L":12,
  "M":13,
  "N":14,
  "Ñ":15,
  "O":16,"Ó":16,
  "P":17,
  "Q":18,
  "R":19,
  "S": 20,
  "T":21,
  "U":22,"Ú":22,
  "V":23,
  "W":24,
  "X":25,
  "Y":26,
  "Z":27,
  "a":28,"á":28,
  "b":29,
  "c":30,
  "d":31,
  "e":32,"é":32,
  "f":33,
  "g":34,
  "h":35,
  "i":36,"í":36,
  "j":37,
  "k":38,
  "l":39,
  "m":40,
  "n":41,
  "ñ":42,
  "o":43,"ó":43,
  "p":44,
  "q":45,
  "r":46,
  "s":47,
  "t":48,
  "u":49,"ú":49,
  "v":50,
  "w":51,
  "x":52,
  "y":53,
  "z":54,
  "-":55,
  "_":56,
  "0":57,
  "1":58,
  "2":59,
  "3":60,
  "4":61,
  "5":62,
  "6":63,
  "7":64,
  "8":65,
  "9":66

}


def validar_contrasenia(password,error = False,exceso_char=False):
  if 8<= len(password)<=12:
    i = 0
    cont_mayusculas = 0
    cont_minusculas = 0
    cont_numero = 0
    cont_guion = 0
    cont_guion_bajo = 0

    while i<len(password) and not error and not exceso_char:
      if caracteres_validos.get(password[i]):
        if 1<= caracteres_validos[password[i]]<=27:
          cont_mayusculas +=1
        if 28 <= caracteres_validos[password[i]] <=54:
          cont_minusculas +=1
        if caracteres_validos[password[i]] ==55:
          cont_guion +=1
        if caracteres_validos[password[i]] ==56:
          cont_guion_bajo +=1
        if 57 <= caracteres_validos[password[i]] <=66:
          cont_numero +=1
        if cont_guion >0 and cont_guion_bajo>0:
          exceso_char = True
        if cont_guion_bajo >1:
          exceso_char = True
        if cont_guion >1:
          exceso_char = True
      else:
        error = True
      i+=1

    if not error:
      if cont_mayusculas == 0:
        mb.showerror("Error","La contraseña debe contener por lo menos una letra mayúsculas")
        res = False
      elif cont_minusculas == 0:
        mb.showerror("Error","La contraseña debe contener por lo menos una letra minúscula")
        res = False
      elif cont_numero == 0:
        mb.showerror("Error","La contraseña debe contener por lo menos un numero")
        res = False
      elif (cont_guion >0 and cont_guion_bajo >0):
        mb.showerror("Error","La contraseña debe contener alguno de los caracteres '-' o '_'  pero no ambos")
        res = False
      elif cont_guion == 0 and cont_guion_bajo==0:
        mb.showerror("Error","La contraseña debe contener alguno de los caracteres '-' o '_'")
        res = False
      elif (cont_guion>1 and cont_guion_bajo==0) or (cont_guion_bajo>1 and cont_guion ==0):
        mb.showerror("Error","La contraseña no puede tener mas un un'-' ó un '_'")
        res =False
      else:
        res = True
    else:
      mb.showerror("Error","La contraseña debe estar compuesta solo por caracteres alfanuméricos excepto por alguno de los caractres '_' ó '-'")
      res = False
      error = True
  else:
    mb.showerror("ERROR","La contraseña debe tener mas de 8 caracteres y menos de 12")
    res = False

  
    
  return res


