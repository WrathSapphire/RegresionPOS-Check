#############################################################################################################
# Regresión Check v1.2 | Apache License 2.0 																#
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
         # Venta TD Anulada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TD  ')
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R006')]

        count_row = df_temp.shape[0]

        if df_temp.empty:
            mensajes.append(f"[Falta] Venta TD Anulada")
        else:
            mensajes.append(f"[Correcto] Venta TD Anulada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Venta TD Anulada.xlsx')

        # Venta TC Anulada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TC  ')         
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R006')]
        count_row = df_temp.shape[0]  

        if df_temp.empty:
            mensajes.append(f"[Falta] Venta TC Anulada")
        else:
            mensajes.append(f"[Correcto] Venta TC Anulada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Venta TC Anulada.xlsx')

        # Venta Tarjeta Internacional Anulada
        df_temp = df.loc[(df['MARCA_LOCAL_INTERNACIONAL'] == 'I')
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R006')]

        count_row = df_temp.shape[0]  
        if df_temp.empty:
            mensajes.append(f"[Falta] Venta Tarjeta Internacional Anulada [Simulador, DESA]")
        else:
            mensajes.append(f"[Correcto] Venta Tarjeta Internacional Anulada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Tarjeta Internacional Anulada.xlsx')
            
        # Venta Tarjeta Otra Procesadora (UENO) Anulada
        df_temp = df.loc[((df['NRO_TARJETA'].str.contains('5585480009064136'))          #TC 
                    | (df['NRO_TARJETA'].str.contains('5585490001200661')))       #TD
                    & (df['COD_RESPUESTA_EXTENDIDA'] == 'R006')]

        count_row = df_temp.shape[0]  
        if df_temp.empty:
            mensajes.append(f"[Falta] Venta Tarjeta Otra Procesadora (UENO) Anulada")
        else:
            mensajes.append(f"[Correcto] Venta Tarjeta Otra Procesadora (UENO) Anulada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Tarjeta Otra Procesadora (UENO) Anulada.xlsx')
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