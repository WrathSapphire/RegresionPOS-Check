##########################################################################################################
# DOCUMENTACION: Automatizacion de consultas de casos de prueba Test de Regresión en POS de BANCARD S.A. #
# QA: Javier Bernal                                                                                      #
##########################################################################################################

import pandas as pd
import logging
logging.basicConfig(filename='registro.log', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s:%(message)s')

df = pd.read_excel('MET001.xlsx')

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

        # Venta Tarjeta de Otra Procesadora (UENO) Anulada [Pendiente de arreglo xd]

        df_temp = df.loc[((df['NRO_TARJETA'].str.contains('5585480009064136')) 
                          | (df['NRO_TARJETA'].str.contains('5585490001200661'))) 
                          & (df['COD_REEXT'] == 'R006')]

        count_row = df_temp.shape[0]  
        if df_temp.empty:
            print("[Falta] Venta Tarjeta de Otra Procesadora (UENO) Anulada")
            df_temp.to_excel('Venta Tarjeta de Otra Procesadora (UENO) Anulada.xlsx')
        else:
            print("[Correcto] Venta Tarjeta de Otra Procesadora (UENO) Anulada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Tarjeta de Otra Procesadora (UENO) Anulada.xlsx')

        print("\n")

    except Exception as e:
        logging.error(f'Error occurred: {e}', exc_info=True)
    else:
        logging.info('Anulaciones() se ejecutó correctamente')
    return 0