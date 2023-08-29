#############################################################################################################
# Regresión POS Check | Apache License 2.0 														    		#
# Software de generación automática de documentación para Test de Regresión en dispositivos POS         	#
# Javier Bernal | 2023																						#
# Source code: https://github.com/WrathfulNico/RegresionPOS-Check											#
#############################################################################################################

import pandas as pd
import logging

def InfonetCobranzas(): 
    mensajes=[]
    df = pd.read_excel('.\\resources\MET001.xlsx')
    mensajes.append(f"####InfonetCobranzas####\n")
    try:
        # Infonet Cobranzas 
        df_temp = df.loc[((df['COD_TRANSACCION'] == 72) | (df['COD_TRANSACCION'] == '72'))
                            & (df['ID_SERVICIO'] == 'TIC')
                            & (df['COD_TIPO_DISPOSITIVO'] == 'WEB')
                            & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                            & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            mensajes.append(f"[Falta] Infonet Cobranzas")
        else:
            mensajes.append(f"[Correcto] Infonet Cobranzas | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Infonet Cobranzas.xlsx')
        mensajes.append(f'\n')

        with open('reporte.txt', 'a') as file:
            for mensaje in mensajes:
                file.write("%s\n" % mensaje)
        file.close
    
    except Exception as e:
        logging.error(f'Error occurred: {e}', exc_info=True)
        mensajes.append(f"Hubo un error en el modulo Infonet Cobranzas\n")
    else:
        logging.info('InfonetCobranzas() se ejecutó correctamente')

    return 0
