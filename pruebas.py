#######################################################################
##******************Telegram Nodo Btc********************************##
#######################################################################

# Este proyecto busca mostrar como montar un bot en telegram
# para el despliegue de informacion de precios de bitcoin en bs
# y compartir graficas
# La primera versión solo tiene tres acciones:
# /start - Inicia el bot, realiza un saludo y guarda usuario en log.
# send_ip - manda el ip con que el rpi se conecta.        solo admins
# terminal - Abre una terminal en el rpi por mensajes.    solo admins

# importación de librerias
import numpy as np
import logging, os
from app.modulos import init_bins
from telebot import types
from dotenv import load_dotenv




knowUsers, userStep = init_bins()

#####################  Comandos Bot ##############################


#CARGANDO TOKENS
#donde se guardan los tokens como variables de entorno
path = '/home/ghost/'
load_dotenv(path+'.env')
# autenrtificación y cuenta maestra
token = os.getenv('token')
master = float(os.getenv('master'))
if token: logging.info('Carga de Credenciales de ingreso: ok!')
else: logging.error('Error con carga de Credenciales')
print(token)
