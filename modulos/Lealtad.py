##########################################################################################################
# DOCUMENTACION: Automatizacion de consultas de casos de prueba Test de Regresión en POS de BANCARD S.A. #
# QA: Javier Bernal                                                                                      #
##########################################################################################################

import pandas as pd
import logging

def Lealtad():
    df = pd.read_excel('.\\resources\MET001.xlsx') 
    print("####Lealtad####\n")
    try:
        # Canje TC Lealtad Aprobada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TC  ')
                         & (df['COD_TRANSACCION'] == 76)                     
                         & (df['COD_PREFIJO'] == '  ')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]

        count_row = df_temp.shape[0] 

        if df_temp.empty:
            print("[Falta] Canje TC Lealtad Aprobada")
        else:
            print("[Correcto] Canje TC Lealtad Aprobada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Canje TC Lealtad Aprobada.xlsx')


        # Canje TC Lealtad Reversada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TC  ')
                         & (df['COD_TRANSACCION'] == 76)
                         & (df['COD_PREFIJO'] == '  ')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')]
        count_row = df_temp.shape[0]  

        if df_temp.empty:
            print("[Falta] Canje TC Lealtad Reversada")
        else:
            print("[Correcto] Canje TC Lealtad Reversada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Canje TC Lealtad Reversada.xlsx')
        print("\n")
    
    except Exception as e:
        logging.error(f'Error occurred: {e}', exc_info=True)
        print("Hubo un error en el modulo Lealtad\n")
    else:
        logging.info('Lealtad() se ejecutó correctamente')
    return 0