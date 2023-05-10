##########################################################################################################
# DOCUMENTACION: Automatizacion de consultas de casos de prueba Test de Regresión en POS de BANCARD S.A.
# QA: Javier Bernal
##########################################################################################################

from modulos.VentaVuelto import *
from modulos.VentaCuota import *
from modulos.VentaTDTC import *
from modulos.VentaSaldo import *
from modulos.VentaQR import *
from modulos.OpSinTarjeta import *
from modulos.Billeteras import *
from modulos.Anulaciones import *
from modulos.TransaccionesAgiles import *
from modulos.VentaTarjetasInternacionales import *
from modulos.Lealtad import *
from modulos.InfonetCobranzas import *
from modulos.FileScript import *
import sys

sys.stdout = open(r'.\reporte.txt', 'w')
TextoASCII() #Imprime el texto ASCII definido
VentaTDTC()
VentaCuota()
VentaQR()
VentaSaldo()
Billeteras()
####Debito/Credito Extranjero con Tarjeta Dual UENO, se va a verificar por número de tarjeta
OpSinTarjeta()
TransaccionesAgiles()
VentaVuelto()
VentaTarjetasInternacionales()
InfonetCobranzas() # Falta terminar
Anulaciones() 
Lealtad() 
Documentacion() #Crea la carpeta con hora sistema de ejecución y mueve los df exportados a excel
sys.stdout.close()
ImprimirEnPantalla()
