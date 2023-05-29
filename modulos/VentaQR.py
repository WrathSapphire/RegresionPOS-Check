##########################################################################################################
# DOCUMENTACION: Automatizacion de consultas de casos de prueba Test de Regresión en POS de BANCARD S.A. #
# QA: Javier Bernal                                                                                      #
##########################################################################################################

import pandas as pd
import logging

df = pd.read_excel('.\\resources\MET001.xlsx')

def VentaQR():
    print("####VentaQR####\n")
    try: 
        # Venta QR TC Aprobada   
        df_temp = df.loc[(df['PRESTACION'] == 'TCQR')
                         & (df['DISPOSITIVO'] == 'APP')
                         & (df['METODO'] == 00) 
                         & (df['COD_RE'] == 00)
                         & (df['COD_REEXT'] == '    ')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Venta QR TC Aprobada [DESA]")
        else:
            print("[Correcto] Venta QR TC Aprobada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta QR TC Aprobada.xlsx')

        # Venta QR TC Reversada   
        df_temp = df.loc[(df['PRESTACION'] == 'TCQR')
                         & (df['DISPOSITIVO'] == 'APP')
                         & (df['METODO'] == 00) 
                         & (df['COD_RE'] == 00)
                         & (df['COD_REEXT'] == 'R001')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Venta QR TC Reversada [DESA]")
        else:
            print("[Correcto] Venta QR TC Reversada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta QR TC Reversada.xlsx')


        # Venta QR TD Aprobada   
        df_temp = df.loc[(df['PRESTACION'] == 'TDQR')
                         & (df['DISPOSITIVO'] == 'APP')
                         & (df['METODO'] == 00) 
                         & (df['COD_RE'] == 00)
                         & (df['COD_REEXT'] == '    ')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Venta QR TD Aprobada [DESA]")
        else:
            print("[Correcto] Venta QR TD Aprobada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta QR TD Aprobada.xlsx')

        # Venta QR TD Reversada   
        df_temp = df.loc[(df['PRESTACION'] == 'TDQR')
                         & (df['DISPOSITIVO'] == 'APP')
                         & (df['METODO'] == 00) 
                         & (df['COD_RE'] == 00)
                         & (df['COD_REEXT'] == 'R001')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Venta QR TD Reversada [DESA]")
        else:
            print("[Correcto] Venta QR TD Reversada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta QR TD Reversada.xlsx')

        print("\n")
    except Exception as e:
        logging.error(f'Error occurred: {e}', exc_info=True)
        print("Hugo un error con el modulo VentaQR\n")
    else:
        logging.info('VentaQR() se ejecutó correctamente')
    return 0