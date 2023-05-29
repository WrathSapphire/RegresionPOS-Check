##########################################################################################################
# DOCUMENTACION: Automatizacion de consultas de casos de prueba Test de Regresión en POS de BANCARD S.A. #
# QA: Javier Bernal                                                                                      #
##########################################################################################################

import sys
from modulos import *

try:
    sys.stdout = open(r'.\reporte.txt', 'w')        #Comienza a escribir todo lo impreso en reporte.txt
    TextoASCII()                                    #Imprime el texto ASCII definido
    VentaTDTC()
    VentaCuota()
    VentaQR()
    VentaSaldo()
    Billeteras()
    OpSinTarjeta()
    TransaccionesAgiles()
    VentaVuelto()
    VentaTarjetasInternacionales()
    InfonetCobranzas()
    Anulaciones() 
    Lealtad() 
    Documentacion()                                 #Crea carpeta c/ hora sistema y mueve los df exportados
    sys.stdout.close()                              #Deja de escribir y cierra reporte.txt
    MoverArchivos()                                 #Mueve carpetas y reportes a ./Tests
except Exception as e:
    logging.error(f'Error en la ejecución del programa!\n{e}', exc_info=True)
else:
    logging.info('El programa se ejecutó y finalizó correctamente!\n')