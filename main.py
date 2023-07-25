##########################################################################################################
# DOCUMENTACION: Automatizacion de consultas de casos de prueba Test de Regresión en POS de BANCARD S.A. #
# QA: Javier Bernal                                                                                      #
##########################################################################################################

from modulos import *
from tkinter import *
import tkinter as tk
import logging
import pandas as pd
import warnings
from openpyxl.styles import NamedStyle

logging.basicConfig(filename='.\\resources\debugPrograma.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s:%(message)s')
warnings.simplefilter("ignore")
NamedStyle.font = None


class VentanaPrincipal:
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
        label2 = Label(master, text="Regresion POS Check v1.2",font=("Helvetica", 15, "bold"),fg="white", bg="#003B8D")
        label2.place(relx=0.5, rely=0.32, anchor=CENTER)

        #Boton Ejecutar Casos de Prueba
        self.botonRun = tk.Button(master, text="Regresión Check", font="Helvetica", command=self.RegresionCheck, height=1, width=20)
        self.botonRun.place(x=300, y=170, anchor=CENTER)
        #Boton Parámetros
        self.boton_parametros = tk.Button(master, text='Parámetros',font="Helvetica", command=self.abrir_ventana_parametros, height=1, width=20)
        self.boton_parametros.place(x=300, y=210, anchor=CENTER)
        #Boton Generar Excel
        self.botonExcel = tk.Button(master, text="Generar Excel", font="Helvetica", command=self.DBConnect, height=1, width=20)
        self.botonExcel.place(x=300, y=250, anchor=CENTER)
        #Boton Salir
        self.botonSalir = tk.Button(master, text="Salir", font="Helvetica", command=master.quit, height=1, width=20)
        self.botonSalir.place(x=300, y=290, anchor=CENTER)

    def RegresionCheck(self):
        try:
            TextoASCII()                                    
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
            CajaPOS()
            Documentacion()                                 
        except Exception as e:
            logging.error(f'Error en la ejecución del programa!\n{e}', exc_info=True)
        else:
            logging.info('El programa ejecutó todos los módulos!\n')

    def DBConnect(self):
        try:
            os.system('java -jar .\\resources\DBConnect.jar')
            os.remove('MET001Test.xlsx')
            os.remove('MET001Desa.xlsx')
            os.replace('MET001.xlsx', '.\\resources\\MET001.xlsx')
        except Exception as e:
            logging.error(f'Error en la ejecución del programa DBConnect!\n{e}', exc_info=True)
        else:
            logging.info('El programa ejecutó correctamente DBConnect\n')
    def abrir_ventana_parametros(self):
        ventana_parametros = VentanaParametros(tk.Tk())

##############################################################################################################################

class VentanaParametros:
    def __init__(self, master):
        # Crear la ventana principal
        self.master = master
        self.master.title("Parametros")
        self.master.configure(background='#003B8D')
        self.master.geometry("330x350")
        self.master.resizable(False,True)

        #Etiqueta
        labeltitle = Label(master, text="Parámetros SQL",fg="white",font=("Helvetica", 15, "bold"),bg="#003B8D")
        labeltitle.place(relx=0.5, y=20, anchor=CENTER)   
        
        #TODO:ScrollBar
        #scrollbar = Scrollbar(master)
        #scrollbar.pack( side = RIGHT, fill = Y )
        #scrollbar.config(command = self.Crear_Entry_Seriales.yview )

        # Crear el cuadro de texto para fecha de inicio de las pruebas
        self.fecha_cert_label = tk.Label(self.master, text="Inicio de pruebas",fg="white",font=("Helvetica", 12, "bold"), bg="#003B8D")
        self.fecha_cert_label.place(relx=0.25, y=50, anchor=CENTER)
        self.fecha_cert_entry = tk.Entry(self.master, justify=CENTER, font=("Helvetica", 10, "bold"))
        self.fecha_cert_entry.insert(0, "20230710")
        self.fecha_cert_entry.place(relx=0.25, y=75, anchor=CENTER,width=70)

        #Boton guardar fecha
        self.fecha_cert_button = tk.Button(self.master, text="Guardar fecha", font="Helvetica", command=self.fecha_cert,width=15)
        self.fecha_cert_button.place(relx=0.25, y=110, anchor=CENTER)

        # Crear el cuadro de texto para el número de equipos a certificar
        self.num_equipos_label = tk.Label(self.master, text="Cantidad de POS",fg="white",font=("Helvetica", 12, "bold"), bg="#003B8D")
        self.num_equipos_label.place(relx=0.75, y=50, anchor=CENTER)
        self.num_equipos_entry = tk.Entry(self.master, justify=CENTER, font=("Helvetica", 10, "bold"))
        self.num_equipos_entry.insert(0, "3")
        self.num_equipos_entry.place(relx=0.75, y=75, anchor=CENTER,width=25)
        #Boton crear cuadros
        self.Crear_Entry_Seriales_button = tk.Button(self.master, text="Crear cuadros", font="Helvetica", command=self.Crear_Entry_Seriales, width=15)
        self.Crear_Entry_Seriales_button.place(relx=0.75, y=110, anchor=CENTER)

        #Etiqueta Seriales
        labelSeriales = Label(master, text="Ingrese Seriales",fg="white",font=("Helvetica", 12, "bold"),bg="#003B8D")
        labelSeriales.place(relx=0.5, y=185, anchor=CENTER)

        # Lista para almacenar los cuadros de texto para los seriales
        self.serial_entries = []

        def Crear_Entry_Seriales_Default():
            # Obtener el número de equipos a certificar
            num_equipos = int(self.num_equipos_entry.get())
            # Crear N cuadros de texto para los seriales
            for i in range(num_equipos):
                serial_entry = tk.Entry(self.master, justify=CENTER, font=("Helvetica", 10, "bold"))
                serial_entry.place(relx=0.5, y=210 + i * 30, anchor=CENTER)
                self.serial_entries.append(serial_entry)

        Crear_Entry_Seriales_Default()

        # Crear el botón para guardar los seriales en el archivo query.sql
        self.guardar_seriales_button = tk.Button(self.master, text="Guardar seriales", font="Helvetica",  command=self.Guardar_Seriales, width=15)
        self.guardar_seriales_button.place(relx=0.75, y=145, anchor=CENTER)

        #Boton volver
        self.volver_button = tk.Button(self.master, text="Volver", font="Helvetica",  command=self.master.withdraw,width=15)
        self.volver_button.place(relx=0.25, y=145, anchor=CENTER)

    def Crear_Entry_Seriales(self):
        # Obtener el número de equipos a certificar
        num_equipos = int(self.num_equipos_entry.get())
        # Crear N cuadros de texto para los seriales
        serial_entries = []
        for i in range(num_equipos):
            serial_entry = tk.Entry(self.master, justify=CENTER, font=("Helvetica", 10, "bold"))
            serial_entry.place(relx=0.5, y=210 + i * 30, anchor=CENTER)
            serial_entries.append(serial_entry)
        # Destruir cuadros de texto anteriores
        for entry2 in self.serial_entries:
            entry2.destroy()
            print(entry2,"entradas")
        # Eliminar entradas anteriores de la lista
        del self.serial_entries[:]
        # Agregar nuevas entradas a la lista
        self.serial_entries.extend(serial_entries)

    seriales=[]

    def Guardar_Seriales(self):
        # Obtener los seriales ingresados por el usuario
        for entry in self.serial_entries:
            if entry.get() != "":
                self.seriales.append(entry.get())
                if not entry.winfo_exists():
                    i=0
                    entry = tk.Entry(self.master)
                    entry.place(relx=0.5, y=(210 + i * 30), anchor=CENTER)
                    self.serial_entries.append(entry)
                # Abrir el archivo query.sql y leer su contenido
                with open('.\\resources\\query.sql', 'r') as f:
                    lines = f.readlines()
                # Modificar la línea 38 con los seriales ingresados por el usuario
                    lines[37] = "WHERE IN02INVSER IN ('" + "', '".join(self.seriales) + "')\n"
                with open('.\\resources\\query.sql', 'w') as f:
                    f.writelines(lines)
                f.close()
        del self.seriales[:]

    def fecha_cert(self):
        # Obtener los seriales ingresados por el usuario
        fecha = ""
        if self.fecha_cert_entry.get() != "":
            fecha=(self.fecha_cert_entry.get())
        # Abrir el archivo query.sql y leer su contenido
            with open('.\\resources\\query.sql', 'r') as f:
                lines = f.readlines()
        # Modificar la línea 39 con los seriales ingresados por el usuario
            lines[38] = 'AND ME01MOVFEC  >= \'' + ''.join(fecha) + '\'\n'
        # Guardar los cambios en el archivo query.sql
            with open('.\\resources\\query.sql', 'w') as f:
                f.writelines(lines)

root = tk.Tk()
mi_ventana = VentanaPrincipal(root)
root.mainloop()