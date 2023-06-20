##########################################################################################################
# DOCUMENTACION: Automatizacion de consultas de casos de prueba Test de Regresión en POS de BANCARD S.A. #
# QA: Javier Bernal                                                                                      #
##########################################################################################################

import pandas as pd
import logging

def InfonetCobranzas(): 
    df = pd.read_excel('.\\resources\MET001.xlsx')
    print("####InfonetCobranzas####\n")
    try:
        # Infonet Cobranzas 
        df_temp = df.loc[(df['COD_TRANSACCION'] == 72)
                            & (df['ID_SERVICIO'] == 'TIC')
                            & (df['COD_TIPO_DISPOSITIVO'] == 'WEB')
                            & (df['COD_RESPUESTA'] == 00)
                            & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Infonet Cobranzas")
        else:
            print("[Correcto] Infonet Cobranzas", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Infonet Cobranzas.xlsx')
        print('\n')
    
    except Exception as e:
        logging.error(f'Error occurred: {e}', exc_info=True)
        print("Hubo un error en el modulo Infonet Cobranzas\n")
    else:
        logging.info('InfonetCobranzas() se ejecutó correctamente')

    return 0
