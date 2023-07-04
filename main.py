##########################################################################################################
# DOCUMENTACION: Automatizacion de consultas de casos de prueba Test de Regresión en POS de BANCARD S.A. #
# QA: Javier Bernal                                                                                      #
##########################################################################################################

import sys
from modulos import *
from datetime import datetime
from tkinter import *
import tkinter as tk
import logging
import pandas as pd
import warnings
from tkinter import messagebox
from openpyxl.styles import NamedStyle
logging.basicConfig(filename='.\\resources\debugPrograma.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s:%(message)s')
warnings.simplefilter("ignore")
NamedStyle.font = None

class VentanaPrincipal:
    
    def JavaConnect(self):
        messagebox.showinfo("Atencion!", "Favor ingresar credenciales en consola!")
        os.system('java -jar .\\resources\javaConnect.jar')
        df1 = pd.read_excel('MET001Test.xlsx')
        df2 = pd.read_excel('MET001Desa.xlsx')
        df = pd.concat([df1, df2])
        os.remove('MET001Test.xlsx')
        os.remove('MET001Desa.xlsx')
        df.to_excel('MET001.xlsx', index=False)
        os.replace('MET001.xlsx', '.\\resources\\MET001.xlsx')

    def __init__(self, master):
        self.master = master
        master.title("Regresion POS Check v1.2")
        master.geometry("600x400")
        master.resizable(False,False)
        #Fondo
        self.bg = PhotoImage(file = ".\\resources\\background.png")
        label1 = Label(master, image = self.bg)
        label1.place(x = 0,y = 0)
        #Etiqueta
        label2 = Label(master, text="Regresion POS Check v1.2",fg="white",font="Helvetica",bg="black")
        label2.place(relx=0.5, rely=0.32, anchor=CENTER)

        #Boton Ejecutar Casos de Prueba
        self.botonRun = tk.Button(master, text="Regresión Check", font="Helvetica", command=self.RegresionCheck, height=2, width=20)
        self.botonRun.place(x=300, y=180, anchor=CENTER)
        #Boton Generar Excel
        self.botonExcel = tk.Button(master, text="Generar Excel", font="Helvetica", command=self.JavaConnect, height=2, width=20)
        self.botonExcel.place(x=300, y=245, anchor=CENTER)
        #Boton Salir
        self.botonSalir = tk.Button(master, text="Salir", font="Helvetica", command=master.quit, height=2, width=20)
        self.botonSalir.place(x=300, y=310, anchor=CENTER)

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