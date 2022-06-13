from app.inicia_juego import inicia_juego
from validadores.modulos import fin_juego

def inicia_app(jugadores):  
  estadisticas_finales = inicia_juego(jugadores)
  fin_juego(estadisticas_finales)