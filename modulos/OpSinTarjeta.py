##########################################################################################################
# DOCUMENTACION: Automatizacion de consultas de casos de prueba Test de Regresión en POS de BANCARD S.A. #
# QA: Javier Bernal                                                                                      #
##########################################################################################################

import pandas as pd
import logging

df = pd.read_excel('.\\resources\MET001.xlsx')

def OpSinTarjeta(): 
    print("####OpSinTarjeta####\n")
    try:
        # Venta Operaciones Sin Tarjeta Aprobada   
        df_temp = df.loc[(df['PRESTACION'] == 'STAR')
                         & (df['DISPOSITIVO'] == 'POS')
                         & (df['MARCA'] == 'ENT')
                         & (df['PRODUCTO'] == 'PMO')
                         & (df['METODO'] == '  ') 
                         & (df['COD_RE'] == 00)
                         & (df['COD_REEXT'] == '    ')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Op. Sin Tarjeta Aprobada [DESA]")
        else:
            print("[Correcto] Op. Sin Tarjeta Aprobada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Op Sin Tarjeta Aprobada.xlsx')

        # Venta Operaciones Sin Tarjeta Reversada   
        df_temp = df.loc[(df['PRESTACION'] == 'STAR')
                         & (df['DISPOSITIVO'] == 'POS')
                         & (df['MARCA'] == 'ENT')
                         & (df['PRODUCTO'] == 'PMO')
                         & (df['METODO'] == '  ') 
                         & (df['COD_RE'] == 00)
                         & (df['COD_REEXT'] == 'R001')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Op. Sin Tarjeta Reversada [DESA]")
        else:
            print("[Correcto] Op. Sin Tarjeta Reversada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Op Sin Tarjeta Reversada.xlsx')
        print ("\n")
    
    except Exception as e:
        logging.error(f'Error occurred: {e}', exc_info=True)
        print("Hubo un error con el modulo OpSinTarjeta\n")

    else:
        logging.info('OpSinTarjeta() se ejecutó correctamente')
    return 0