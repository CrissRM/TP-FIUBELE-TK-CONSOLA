def formatear_ruta(ruta):
  path_file = ""
  for letter in ruta:
    if letter =="\\":
      path_file +="/"
    else:
      path_file +=letter
  return path_file

