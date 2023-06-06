##########################################################################################################
# DOCUMENTACION: Automatizacion de consultas de casos de prueba Test de Regresión en POS de BANCARD S.A. #
# QA: Javier Bernal                                                                                      #
##########################################################################################################

import sys
from modulos import *
from datetime import datetime
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import logging
logging.basicConfig(filename='.\\resources\debugPrograma.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s:%(message)s')

class VentanaPrincipal:
    def __init__(self, master):
        self.master = master
        master.title("Bienvenido")
        master.geometry("250x150")
        master.configure(bg="black")
    

        self.botonRun = tk.Button(master, text="Ejecutar", command=self.RegresionCheck, height=2, width=20)
        self.botonRun.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.botonSalir = tk.Button(master, text="Salir", command=master.quit, height=1, width=5)
        self.botonSalir.place(relx=0.5, rely=0.8    , anchor=CENTER)

    def RegresionCheck(self):
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
            print("Hora de finalización "+ datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
            sys.stdout.close()                              #Deja de escribir y cierra reporte.txt
            Documentacion()                                 #Crea carpeta c/ hora sistema y mueve los df exportados...
                                                            #Mueve carpetas y reportes a ./Tests
        except Exception as e:
            logging.error(f'Error en la ejecución del programa!\n{e}', exc_info=True)
        else:
            logging.info('El programa se ejecutó y finalizó correctamente!\n')

root = tk.Tk()
mi_ventana = VentanaPrincipal(root)
root.mainloop()