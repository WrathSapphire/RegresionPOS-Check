#############################################################################################################
# Regresión POS Check | Apache License 2.0 														    		#
# Software de generación automática de documentación para Test de Regresión en dispositivos POS         	#
# Javier Bernal | 2023																						#
# Source code: https://github.com/WrathfulNico/RegresionPOS-Check											#
#############################################################################################################

import os
import shutil
from datetime import datetime

def TextoASCII():
    mensajes= ["\n\n[Verificación de Casos de Prueba Regresión Express]\n"]                                                            
    with open('.\\resources\ASCII.text', 'r') as file:                      #Lee archivo ASCII.text
        ascii = file.read()
    file.close

    with open('reporte.txt', 'a') as file:
        file.write(str(ascii+"\n"))                                                   #Imprime archivo ASCII
        for mensaje in mensajes:
            file.write("%s\n" % mensaje)
    file.close
    return 0

def Documentacion():
    mensajes=[]
    mensajes.append(f"Hora de finalización "+ datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    with open('reporte.txt', 'a') as file:
            file.write(str(mensajes))                                     #Imprime mensajes
    file.close
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

    ruta_reporte = os.path.join('.\\tests\\', reporte)
    os.system('notepad.exe ' + ruta_reporte)

    return 0

