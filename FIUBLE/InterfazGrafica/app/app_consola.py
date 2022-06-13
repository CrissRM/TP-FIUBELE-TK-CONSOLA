from app.inicial_juego import inicial_juego
from validadores.modulos import fin_juego

def inicia_app(jugadores):  
  estadisticas_finales = inicial_juego(jugadores)
  fin_juego(estadisticas_finales)