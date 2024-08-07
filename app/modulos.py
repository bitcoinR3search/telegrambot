# Este archivo contiene los módulos básicos
# que implementa el bot

import os, logging, json
import numpy as np


def init_bins(path_assets='/home/ghost/telegrambot/bins/'):
    # Crea un archivo log si no existe.
    if not os.path.exists(path_assets+'bot_telegram.log'):
        with open(path_assets+'bot_telegram.log','w') as log:
            log.write('#fecha,#hora,#evento,#nivel\n')
        #Configurando log del funcionamiento interno del bot.
        logging.basicConfig(filename=path_assets+'bot_telegram.log',filemode='a+',format='%(asctime)s,%(message)s,%(levelname)s', datefmt='%d-%b-%y,%H:%M:%S',level=logging.INFO)
        logging.info('Iniciado el Bot en Telegram')

# Cargamos los usuarios conocídos. De no existir creamos una lista vacía.
# KnownUsers es un array numpy de usuarios conocidos
    if (os.path.exists(path_assets+'knownUsers.npy')):
        logging.info('Cargando archivo con Usuarios Conocidos')
        aux         = np.load(path_assets+'knownUsers.npy', allow_pickle='TRUE') 
        knownUsers  = aux.tolist()
    else:
        logging.info('Creando archivo para nuevos Usuarios')
        knownUsers = []
        np.save(path_assets+'knownUsers.npy',knownUsers)

    if (os.path.exists(path_assets+'userStep.json')):
        logging.info('Cargando json userStep')
        with open(path_assets+'userStep.json','r') as filex:
            userStep=json.load(filex,object_hook=jsonKeys2int) 
    else:
        logging.info('Creando un diccionario userStep')
        userStep = {}
        print('chau')
    return knownUsers, userStep


def jsonKeys2int(x):
    if isinstance(x, dict):
            return {int(k):v for k,v in x.items()}
    return x


