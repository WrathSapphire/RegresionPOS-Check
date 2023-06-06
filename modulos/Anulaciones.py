##########################################################################################################
# DOCUMENTACION: Automatizacion de consultas de casos de prueba Test de Regresión en POS de BANCARD S.A. #
# QA: Javier Bernal                                                                                      #
##########################################################################################################

import pandas as pd
import logging

df = pd.read_excel('.\\resources\MET001.xlsx')

def Anulaciones(): 
    print("####Anulaciones####\n")
    try:
         # Venta TD Anulada
        df_temp = df.loc[(df['PRESTACION'] == 'TD  ')
                         & (df['COD_RE'] == 00)
                         & (df['COD_REEXT'] == 'R006')]

        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Venta TD Anulada")
        else:
            print("[Correcto] Venta TD Anulada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta TD Anulada.xlsx')

        # Venta TC Anulada
        df_temp = df.loc[(df['PRESTACION'] == 'TC  ')         
                         & (df['COD_RE'] == 00)
                         & (df['COD_REEXT'] == 'R006')]
        count_row = df_temp.shape[0]  

        if df_temp.empty:
            print("[Falta] Venta TC Anulada")
        else:
            print("[Correcto] Venta TC Anulada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta TC Anulada.xlsx')

        # Venta Tarjeta Internacional Anulada
        df_temp = df.loc[(df['LOCAL_INTERNACIONAL'] == 'I')
                         & (df['COD_RE'] == 00)
                         & (df['COD_REEXT'] == 'R006')]

        count_row = df_temp.shape[0]  
        if df_temp.empty:
            print("[Falta] Venta Tarjeta Internacional Anulada [Simulador, DESA]")
        else:
            print("[Correcto] Venta Tarjeta Internacional Anulada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Tarjeta Internacional Anulada.xlsx')

        # Venta Tarjeta Otra Procesadora (UENO) Anulada
        # Para correcto funcionamiento del módulo es necesario almacenar la columna NRO_TARJETA como texto
        df_temp = df.loc[((df['NRO_TARJETA'].str.contains('5585480009064136'))          #TC 
                          | (df['NRO_TARJETA'].str.contains('5585490001200661')))       #TD
                          & (df['COD_REEXT'] == 'R006')]

        count_row = df_temp.shape[0]  
        if df_temp.empty:
            print("[Falta] Venta Tarjeta Otra Procesadora (UENO) Anulada")
        else:
            print("[Correcto] Venta Tarjeta Otra Procesadora (UENO) Anulada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Tarjeta Otra Procesadora (UENO) Anulada.xlsx')
        print("\n")

    except Exception as e:
        logging.error(f'Error occurred: {e}', exc_info=True)
        print("Hubo un error en el modulo Anulaciones\n")

    else:
        logging.info('Anulaciones() se ejecutó correctamente')
    return 0