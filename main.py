##########################################################################################################
# DOCUMENTACION: Automatizacion de consultas de casos de prueba Test de Regresión en POS de BANCARD S.A. #
# QA: Javier Bernal                                                                                      #
##########################################################################################################

import sys
from modulos import *

sys.stdout = open(r'.\reporte.txt', 'w')        #Comienza a escribir todo lo impreso en reporte.txt
TextoASCII()                                    #Imprime el texto ASCII definido
VentaTDTC()
VentaCuota()
VentaQR()
VentaSaldo()
Billeteras()
DebitoCreditoExtranjero()                       #Con UENO. Se verifica por número de tarjeta. Pendiente
OpSinTarjeta()
TransaccionesAgiles()
VentaVuelto()
VentaTarjetasInternacionales()
InfonetCobranzas()                              #Falta terminar
Anulaciones() 
Lealtad() 
Documentacion()                                 #Crea carpeta c/ hora sistema y mueve los df exportados
sys.stdout.close()                              #Deja de escribir y cierra reporte.txt
ImprimirEnPantalla()                            #Abre el reporte y renombra el archivo una vez cerrado
MoverArchivos()                                 #Mueve carpetas y reportes a ./Tests
