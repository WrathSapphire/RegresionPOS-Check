import os
import shutil
from datetime import datetime

carpeta = datetime.now().strftime("Ejecución_%Y-%m-%d_%H-%M-%S")
reporte = datetime.now().strftime("Reporte_%Y-%m-%d_%H-%M-%S")
reporte = reporte + '.txt'

def TextoASCII():
    f = open('ASCII.txt', 'r') #Lee e imprime archivo testing.txt
    file_contents = f.read()
    print (file_contents)
    f.close()
    print("[Verificación de Casos de Prueba Regresión Express]\n")


def Documentacion():
    print("Hora de finalización "+ datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    ruta = os.getcwd()
    archivos = os.listdir(ruta)
    os.mkdir(carpeta)
    for archivo in archivos:
        if (archivo.endswith('.xlsx') and archivo != 'MET001.xlsx'):
            shutil.move(os.path.join(ruta, archivo), carpeta)

def ImprimirEnPantalla():
    import os
    os.system('cmd /c reporte.txt')
    os.rename('reporte.txt', reporte)
    





