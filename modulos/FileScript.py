##########################################################################################################
# DOCUMENTACION: Automatizacion de consultas de casos de prueba Test de Regresión en POS de BANCARD S.A. #
# QA: Javier Bernal                                                                                      #
##########################################################################################################

import os
import shutil
import sys
from datetime import datetime

def TextoASCII():
    f = open('.\\resources\ASCII.text', 'r')                         #Lee e imprime archivo ASCII.text
    file_contents = f.read()
    print (file_contents)
    f.close()
    print("\n\n[Verificación de Casos de Prueba Regresión Express]\n")
    return 0

def Documentacion():
    carpeta = datetime.now().strftime("Ejecución_%Y-%m-%d_%H-%M-%S")
    reporte = datetime.now().strftime("Reporte_%Y-%m-%d_%H-%M-%S")
    reporte = reporte + '.txt'
    ruta = os.getcwd()
    archivos = os.listdir(ruta)
    source = ".\\"
    destination = '.\\tests'

    os.mkdir(carpeta)
    os.rename('reporte.txt', reporte)                   #Una vez cerrado el archivo será renombrado

    for archivo in archivos:                            #Mueve los df generados a su carpeta correspondiente
        if (archivo.endswith('.xlsx') and archivo != 'MET001.xlsx'):
            shutil.move(os.path.join(ruta, archivo), carpeta)

    if not os.path.exists("./tests"):
        os.makedirs("tests")                            #Si no existe el directorio tests, el mismo será creado

    for foldername in os.listdir(source):               #Mueve carpetas
        if foldername.startswith('Ejecución'):
            shutil.move(os.path.join(source, foldername), destination)

    for filename in os.listdir(source):                 #Mueve archivos .txt
        if filename.startswith('Reporte') and filename.endswith('.txt'):
            shutil.move(os.path.join(source, filename), destination)
    return 0

