def formatear_nombre(nombre):
  check = False
  array_name = [name.capitalize() for name in nombre.split()]
  i=0
  while i<len(array_name) and array_name[i].isalpha():
    i+=1
  if i == len(array_name):
    check = True
  
  return check," ".join(array_name)