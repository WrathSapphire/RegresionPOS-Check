##########################################################################################################
# DOCUMENTACION: Automatizacion de consultas de casos de prueba Test de Regresión en POS de BANCARD S.A. #
# QA: Javier Bernal                                                                                      #
##########################################################################################################

import os
import shutil
from datetime import datetime

carpeta = datetime.now().strftime("Ejecución_%Y-%m-%d_%H-%M-%S")
reporte = datetime.now().strftime("Reporte_%Y-%m-%d_%H-%M-%S")
reporte = reporte + '.txt'

def TextoASCII():
    f = open('ASCII.text', 'r')                         #Lee e imprime archivo ASCII.text
    file_contents = f.read()
    print (file_contents)
    f.close()
    print("[Verificación de Casos de Prueba Regresión Express]\n")
    return 0


def Documentacion():
    print("Hora de finalización "+ datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    ruta = os.getcwd()
    archivos = os.listdir(ruta)
    os.mkdir(carpeta)
    for archivo in archivos:                            #Mueve los df generados a su carpeta correspondiente
        if (archivo.endswith('.xlsx') and archivo != 'MET001.xlsx'):
            shutil.move(os.path.join(ruta, archivo), carpeta)
    return 0

def MoverArchivos():
    source = ".\\"
    destination = '.\\Tests'
    os.rename('reporte.txt', reporte)                   #Una vez cerrado el archivo será renombrado

    for foldername in os.listdir(source):               #Mueve carpetas
        if foldername.startswith('Ejecución'):
            shutil.move(os.path.join(source, foldername), destination)

    for filename in os.listdir(source):                 #Mueve archivos .txt
        if filename.startswith('Reporte') and filename.endswith('.txt'):
            shutil.move(os.path.join(source, filename), destination)
    return 0
