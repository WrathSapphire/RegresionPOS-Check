#############################################################################################################
# Regresión POS Check | Apache License 2.0 															    	#
# Software de generación automática de documentación para Test de Regresión en dispositivos POS de BANCARD	#
# Javier Bernal | 2023																						#
# Source code: https://github.com/WrathfulNico/RegresionPOS-Check											#
#############################################################################################################

import pandas as pd
import logging

def Anulaciones(): 
    mensajes=[]
    df = pd.read_excel('.\\resources\MET001.xlsx')
    mensajes.append(f"####Anulaciones####\n")
    try:
         # Anulaciones Venta TD 
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TD  ')
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R006')]

        count_row = df_temp.shape[0]

        if df_temp.empty:
            mensajes.append(f"[Falta] Anulaciones Venta TD ")
        else:
            mensajes.append(f"[Correcto] Anulaciones Venta TD  | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Anulaciones Venta TD .xlsx')

        # Anulaciones Venta TC
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TC  ')         
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R006')]
        count_row = df_temp.shape[0]  

        if df_temp.empty:
            mensajes.append(f"[Falta] Anulaciones Venta TC")
        else:
            mensajes.append(f"[Correcto] Anulaciones Venta TC | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Anulaciones Venta TC.xlsx')

        # Anulaciones Venta Tarjeta Internacional
        df_temp = df.loc[(df['MARCA_LOCAL_INTERNACIONAL'] == 'I')
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R006')]

        count_row = df_temp.shape[0]  
        if df_temp.empty:
            mensajes.append(f"[Falta] Anulaciones Venta Tarjeta Internacional [Simulador, DESA]")
        else:
            mensajes.append(f"[Correcto] Anulaciones Venta Tarjeta Internacional | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Anulaciones Venta Tarjeta Internacional.xlsx')
            
        # Anulaciones Venta Tarjeta Otra Procesadora (UENO)
        df_temp = df.loc[((df['NRO_TARJETA'].str.contains('558548'))          #TC 
                    | (df['NRO_TARJETA'].str.contains('558549')))       #TD
                    & (df['COD_RESPUESTA_EXTENDIDA'] == 'R006')]

        count_row = df_temp.shape[0]  
        if df_temp.empty:
            mensajes.append(f"[Falta] Anulaciones Venta Tarjeta Otra Procesadora (UENO)")
        else:
            mensajes.append(f"[Correcto] Anulaciones Venta Tarjeta Otra Procesadora (UENO) | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Anulaciones Venta Tarjeta Otra Procesadora (UENO).xlsx')
        mensajes.append(f"\n")

        with open('reporte.txt', 'a') as file:
            for mensaje in mensajes:
                file.write("%s\n" % mensaje)
        file.close

    except Exception as e:
        logging.error(f'Error occurred: {e}', exc_info=True)
        mensajes.append(f"Hubo un error en el modulo Anulaciones\n")

    else:
        logging.info('Anulaciones() se ejecutó correctamente')
    return 0