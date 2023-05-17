##########################################################################################################
# DOCUMENTACION: Automatizacion de consultas de casos de prueba Test de Regresión en POS de BANCARD S.A. #
# QA: Javier Bernal                                                                                      #
##########################################################################################################

import pandas as pd
import logging
logging.basicConfig(filename='registro.log', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s:%(message)s')

df = pd.read_excel('MET001.xlsx')

def VentaTarjetasInternacionales(): 
    try:
        # Venta Tarjeta Internacional Aprobada
        df_temp = df.loc[(df['LOCAL_INTERNACIONAL'] == 'I')
                         & (df['COD_RE'] == 00)
                         & (df['COD_REEXT'] == '    ')]

        count_row = df_temp.shape[0]  
        if df_temp.empty:
            print("[Falta] Venta Tarjeta Internacional Aprobada [Simulador, DESA]")
        else:
            print("[Correcto] Venta Tarjeta Internacional Aprobada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Tarjeta Internacional Aprobada.xlsx')

        # Venta Tarjeta Internacional Reversada
        df_temp = df.loc[(df['LOCAL_INTERNACIONAL'] == 'I')
                         & (df['COD_RE'] == 00)
                         & (df['COD_REEXT'] == 'R001')]

        count_row = df_temp.shape[0]  
        if df_temp.empty:
            print("[Falta] Venta Tarjeta Internacional Reversada [Simulador, DESA]")
        else:
            print("[Correcto] Venta Tarjeta Internacional Reversada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Tarjeta Internacional Reversada.xlsx')


        print("\n")
    except Exception as e:
        logging.error(f'Error occurred: {e}', exc_info=True)
    else:
        logging.info('VentaTarjetasInternacionales() ran successfully')
    return 0