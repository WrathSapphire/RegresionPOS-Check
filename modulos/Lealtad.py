##########################################################################################################
# DOCUMENTACION: Automatizacion de consultas de casos de prueba Test de Regresión en POS de BANCARD S.A. #
# QA: Javier Bernal                                                                                      #
##########################################################################################################

import pandas as pd
import logging
logging.basicConfig(filename='registro.log', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s:%(message)s')

df = pd.read_excel('MET001.xlsx')

def Lealtad(): 
    try:
        # Canje TC Lealtad Aprobada
        df_temp = df.loc[(df['PRESTACION'] == 'TC  ')
                         & (df['COD_TRAN'] == 76)                     
                         & (df['METODO'] == '  ')
                         & (df['COD_RE'] == 00)
                         & (df['COD_REEXT'] == '    ')]

        count_row = df_temp.shape[0]  
        if df_temp.empty:
            print("[Falta] Canje TC Lealtad Aprobada")
        else:
            print("[Correcto] Canje TC Lealtad Aprobada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Canje TC Lealtad Aprobada.xlsx')


        # Canje TC Lealtad Reversada
        df_temp = df.loc[(df['PRESTACION'] == 'TC  ')
                         & (df['COD_TRAN'] == 76)
                         & (df['METODO'] == '  ')
                         & (df['COD_RE'] == 00)
                         & (df['COD_REEXT'] == 'R001')]
        count_row = df_temp.shape[0]  

        if df_temp.empty:
            print("[Falta] Canje TC Lealtad Reversada")
        else:
            print("[Correcto] Canje TC Lealtad Reversada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Canje TC Lealtad Reversada.xlsx')

        print("\n")
    except Exception as e:
        logging.error(f'Error occurred: {e}', exc_info=True)
    else:
        logging.info('Lealtad() ran successfully\n')
    return 0