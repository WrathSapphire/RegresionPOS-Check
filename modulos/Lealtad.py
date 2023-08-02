#############################################################################################################
# Regresión Check v1.2 | Apache License 2.0 																#
# Software de generación automática de documentación para Test de Regresión en dispositivos POS de BANCARD	#
# Javier Bernal | 2023																						#
# Source code: https://github.com/WrathfulNico/RegresionPOS-Check											#
#############################################################################################################

import pandas as pd
import logging

def Lealtad():
    mensajes=[]
    df = pd.read_excel('.\\resources\MET001.xlsx') 
    mensajes.append(f"####Lealtad####\n")
    try:
        # Canje TC Lealtad Aprobada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TC  ')
                         & ((df['COD_TRANSACCION'] == 76) | (df['COD_TRANSACCION'] == '76'))                     
                         & (df['COD_PREFIJO'] == '  ')
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]

        count_row = df_temp.shape[0] 

        if df_temp.empty:
            mensajes.append(f"[Falta] Canje TC Lealtad Aprobada")
        else:
            mensajes.append(f"[Correcto] Canje TC Lealtad Aprobada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Canje TC Lealtad Aprobada.xlsx')


        # Canje TC Lealtad Reversada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TC  ')
                         & ((df['COD_TRANSACCION'] == 76) | (df['COD_TRANSACCION'] == '76'))
                         & (df['COD_PREFIJO'] == '  ')
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')]
        count_row = df_temp.shape[0]  

        if df_temp.empty:
            mensajes.append(f"[Falta] Canje TC Lealtad Reversada")
        else:
            mensajes.append(f"[Correcto] Canje TC Lealtad Reversada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Canje TC Lealtad Reversada.xlsx')
        mensajes.append(f"\n")

        with open('reporte.txt', 'a') as file:
            for mensaje in mensajes:
                file.write("%s\n" % mensaje)
        file.close
    
    except Exception as e:
        logging.error(f'Error occurred: {e}', exc_info=True)
        mensajes.append(f"Hubo un error en el modulo Lealtad\n")
    else:
        logging.info('Lealtad() se ejecutó correctamente')
    return 0