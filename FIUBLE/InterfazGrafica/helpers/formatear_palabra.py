import doctest
letras = {
  "á": "a",
  "é": "e",
  "í": "i",
  "ó": "o",
  "ú": "u"
}

def formatear_palabra(palabra):
  """
  """
  lista = [x for x in palabra]
  for i in range(len(lista)):
    if lista[i] in list(letras.keys()):
      lista[i] = letras[lista[i]]
  return "".join(lista)

import doctest
doctest.testmod()