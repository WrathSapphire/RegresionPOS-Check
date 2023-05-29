##########################################################################################################
# DOCUMENTACION: Automatizacion de consultas de casos de prueba Test de Regresión en POS de BANCARD S.A. #
# QA: Javier Bernal                                                                                      #
##########################################################################################################

import pandas as pd
import logging
logging.basicConfig(filename='registro.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')
df = pd.read_excel('MET001.xlsx')

def InfonetCobranzas(): 
    print("####InfonetCobranzas####\n")
    try:
        # Venta Infonet Cobranza   
        df_temp = df.loc[(df['COD_TRAN'] == 72)
                            & (df['SERVICIO'] == 'TIC')
                            & (df['DISPOSITIVO'] == 'WEB')
                            & (df['COD_RE'] == 00)
                            & (df['COD_REEXT'] == '    ')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Infonet Cobranzas")
        else:
            print("[Correcto] Infonet Cobranzas", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Infonet Cobranzas.xlsx')

        print('\n')
    except Exception as e:
        logging.error(f'Error occurred: {e}', exc_info=True)
        print("Hugo un error con el modulo Infonet Cobranzas\n")
    else:
        logging.info('InfonetCobranzas() se ejecutó correctamente')

    return 0
