from modo_juego.inicial_juego import inicial_juego
from validadores.fin_juego import fin_juego

def inicia_app(jugadores):  
  estadisticas_finales = inicial_juego(jugadores)
  fin_juego(estadisticas_finales)