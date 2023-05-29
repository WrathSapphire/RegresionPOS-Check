##########################################################################################################
# DOCUMENTACION: Automatizacion de consultas de casos de prueba Test de Regresión en POS de BANCARD S.A. #
# QA: Javier Bernal                                                                                      #
##########################################################################################################

import pandas as pd
import logging
logging.basicConfig(filename='registro.log', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s:%(message)s')

df = pd.read_excel('MET001.xlsx')

def Billeteras(): 
    print("####Billeteras####\n")
    try:
        # Venta Billetera ZIMPLE Aprobada   
        df_temp = df.loc[(df['PRESTACION'] == 'STAR')
                         & (df['DISPOSITIVO'] == 'POS')
                         & (df['MARCA' ] == 'MIB')
                         & (df['PRODUCTO' ] == 'MIB')
                         & (df['METODO'] == '  ') 
                         & (df['COD_RE'] == 00)
                         & (df['COD_REEXT'] == '    ')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Billetera ZIMPLE Aprobada [TEST]")
        else:
            print("[Correcto] Billetera ZIMPLE Aprobada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Billetera ZIMPLE Aprobada.xlsx')

        # Venta Billetera ZIMPLE Reversada   
        df_temp = df.loc[(df['PRESTACION'] == 'STAR')
                         & (df['DISPOSITIVO'] == 'POS')
                         & (df['MARCA' ] == 'MIB')
                         & (df['PRODUCTO' ] == 'MIB')
                         & (df['METODO'] == '  ') 
                         & (df['COD_RE'] == 00)
                         & (df['COD_REEXT'] == 'R001')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Billetera ZIMPLE Reversada [TEST]")
        else:
            print("[Correcto] Billetera ZIMPLE Reversada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Billetera ZIMPLE Reversada.xlsx')

        # Venta Billetera Vision Aprobada   
        df_temp = df.loc[(df['PRESTACION'] == 'STAR')
                            & (df['DISPOSITIVO'] == 'POS')
                            & (df['MARCA' ] == 'VIS')
                            & (df['PRODUCTO' ] == 'MIB')
                            & (df['METODO'] == '  ') 
                            & (df['COD_RE'] == 00)
                            & (df['COD_REEXT'] == '    ')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Billetera Vision Aprobada")
        else:
            print("[Correcto] Billetera Vision Aprobada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Billetera Vision Aprobada.xlsx')

        # Venta Billetera Vision Reversada   
        df_temp = df.loc[(df['PRESTACION'] == 'STAR')
                            & (df['DISPOSITIVO'] == 'POS')
                            & (df['MARCA' ] == 'VIS')
                            & (df['PRODUCTO' ] == 'MIB')
                            & (df['METODO'] == '  ') 
                            & (df['COD_RE'] == 00)
                            & (df['COD_REEXT'] == 'R001')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Billetera Vision Reversada")
        else:
            print("[Correcto] Billetera Vision Reversada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Billetera Vision Reversada.xlsx')

        # Venta Billetera PJ Aprobada   
        df_temp = df.loc[(df['PRESTACION'] == 'STAR')
                            & (df['DISPOSITIVO'] == 'POS')
                            & (df['MARCA' ] == 'WPJ')
                            & (df['PRODUCTO' ] == 'MIB')
                            & (df['METODO'] == '  ') 
                            & (df['COD_RE'] == 00)
                            & (df['COD_REEXT'] == '    ')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Billetera PJ Aprobada")
        else:
            print("[Correcto] Billetera PJ Aprobada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Billetera PJ Aprobada.xlsx')

        # Venta Billetera PJ Reversada   
        df_temp = df.loc[(df['PRESTACION'] == 'STAR')
                            & (df['DISPOSITIVO'] == 'POS')
                            & (df['MARCA' ] == 'WPJ')
                            & (df['PRODUCTO' ] == 'MIB')
                            & (df['METODO'] == '  ') 
                            & (df['COD_RE'] == 00)
                            & (df['COD_REEXT'] == 'R001')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Billetera PJ Reversada")
        else:
            print("[Correcto] Billetera PJ Reversada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Billetera PJ Reversada.xlsx')

            # Venta Billetera BNF Aprobada   
        df_temp = df.loc[(df['PRESTACION'] == 'STAR')
                            & (df['DISPOSITIVO'] == 'POS')
                            & (df['MARCA' ] == 'BBF')
                            & (df['PRODUCTO' ] == 'MIB')
                            & (df['METODO'] == '  ') 
                            & (df['COD_RE'] == 00)
                            & (df['COD_REEXT'] == '    ')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Billetera BNF Aprobada")
        else:
            print("[Correcto] Billetera BNF Aprobada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Billetera BNF Aprobada.xlsx')

        # Venta Billetera BNF Reversada   
        df_temp = df.loc[(df['PRESTACION'] == 'STAR')
                            & (df['DISPOSITIVO'] == 'POS')
                            & (df['MARCA' ] == 'BBF')
                            & (df['PRODUCTO' ] == 'MIB')
                            & (df['METODO'] == '  ') 
                            & (df['COD_RE'] == 00)
                            & (df['COD_REEXT'] == 'R001')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Billetera BNF Reversada")
        else:
            print("[Correcto] Billetera BNF Reversada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Billetera BNF Reversada.xlsx')

        print("\n")
    except Exception as e:
        logging.error(f'Error occurred: {e}', exc_info=True)
        print("Hugo un error con el modulo Billeteras\n")
    else:
        logging.info('Billeteras() se ejecutó correctamente')
    return 0
