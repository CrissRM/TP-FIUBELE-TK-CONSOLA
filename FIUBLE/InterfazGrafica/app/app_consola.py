from importaciones.import_file import inicial_juego,fin_juego

def inicia_app(jugadores):  
  estadisticas_finales = inicial_juego(jugadores)
  fin_juego(estadisticas_finales)