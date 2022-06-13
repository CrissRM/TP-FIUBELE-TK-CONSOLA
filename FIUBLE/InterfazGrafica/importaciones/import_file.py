import os
from time import time
from random import choice
from initialSetting.datos_iniciales import condiciones_iniciales
from helpers.alternador_turnos import alternador_turnos
from helpers.contar_puntos import contar_puntos
from helpers.contabilizar_puntos import contabilizar_puntos
from helpers.parcial_juego import parcial_juego
from app.app import application
from validadores.validar_condicion_palabra import validar_condicion_palabra 
from validadores.validar_palabra import validar_palabra
from validadores.analizar_palabra import analizar_palabra
from initialSetting.datos_iniciales import obtener_color
from helpers.mensaje_turno_de import mensaje_turno_de
from app.inicial_juego import inicial_juego
from validadores.fin_juego import fin_juego
import tkinter as tk
from helpers.estilos_formatos import estilos
from tkinter import messagebox as mb
from componentes.FrameHidden import FrameHidden
from componentes.Frame import Frame
from componentes.Label import Label
from componentes.Entry import Entry
from componentes.Button import Button
from estilos_formatos import style_label,style_button,style_entry
from funcionalidadButtonTk.actions_button import volver,acceder,guardar