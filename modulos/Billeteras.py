#########################################################################################################
# Regresión Check v1.2 | Apache License 2.0 															#
# Software de generación automática de documentación Test de Regresión en dispositivos POS de BANCARD	#
# Javier Bernal | 2023																					#
# Source code: https://github.com/WrathfulNico/RegresionPOS-Check										#
#########################################################################################################

import pandas as pd
import logging

def Billeteras(): 
    mensajes=[]
    df = pd.read_excel('.\\resources\MET001.xlsx')
    mensajes.append(f"####Billeteras####\n")
    try:
        # Venta Billetera ZIMPLE Aprobada   
        df_temp = df.loc[(df['COD_PRESTACION'] == 'STAR')
                         & (df['COD_TIPO_DISPOSITIVO'] == 'POS')
                         & (df['MARCA' ] == 'MIB')
                         & (df['PRODUCTO_DE_LA_MARCA' ] == 'MIB')
                         & (df['COD_PREFIJO'] == '  ') 
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            mensajes.append(f"[Falta] Billetera ZIMPLE Aprobada")
        else:
            mensajes.append(f"[Correcto] Billetera ZIMPLE Aprobada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Billetera ZIMPLE Aprobada.xlsx')

        # Venta Billetera ZIMPLE Reversada   
        df_temp = df.loc[(df['COD_PRESTACION'] == 'STAR')
                         & (df['COD_TIPO_DISPOSITIVO'] == 'POS')
                         & (df['MARCA' ] == 'MIB')
                         & (df['PRODUCTO_DE_LA_MARCA' ] == 'MIB')
                         & (df['COD_PREFIJO'] == '  ') 
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            mensajes.append(f"[Falta] Billetera ZIMPLE Reversada")
        else:
            mensajes.append(f"[Correcto] Billetera ZIMPLE Reversada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Billetera ZIMPLE Reversada.xlsx')

        # Venta Billetera Vision Aprobada   
        df_temp = df.loc[(df['COD_PRESTACION'] == 'STAR')
                            & (df['COD_TIPO_DISPOSITIVO'] == 'POS')
                            & (df['MARCA' ] == 'VIS')
                            & (df['PRODUCTO_DE_LA_MARCA' ] == 'MIB')
                            & (df['COD_PREFIJO'] == '  ') 
                            & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                            & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            mensajes.append(f"[Falta] Billetera Vision Aprobada")
        else:
            mensajes.append(f"[Correcto] Billetera Vision Aprobada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Billetera Vision Aprobada.xlsx')

        # Venta Billetera Vision Reversada   
        df_temp = df.loc[(df['COD_PRESTACION'] == 'STAR')
                            & (df['COD_TIPO_DISPOSITIVO'] == 'POS')
                            & (df['MARCA' ] == 'VIS')
                            & (df['PRODUCTO_DE_LA_MARCA' ] == 'MIB')
                            & (df['COD_PREFIJO'] == '  ') 
                            & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                            & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            mensajes.append(f"[Falta] Billetera Vision Reversada")
        else:
            mensajes.append(f"[Correcto] Billetera Vision Reversada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Billetera Vision Reversada.xlsx')

        # Venta Billetera PJ Aprobada   
        df_temp = df.loc[(df['COD_PRESTACION'] == 'STAR')
                            & (df['COD_TIPO_DISPOSITIVO'] == 'POS')
                            & (df['MARCA' ] == 'WPJ')
                            & (df['PRODUCTO_DE_LA_MARCA' ] == 'MIB')
                            & (df['COD_PREFIJO'] == '  ') 
                            & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                            & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            mensajes.append(f"[Falta] Billetera PJ Aprobada")
        else:
            mensajes.append(f"[Correcto] Billetera PJ Aprobada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Billetera PJ Aprobada.xlsx')

        # Venta Billetera PJ Reversada   
        df_temp = df.loc[(df['COD_PRESTACION'] == 'STAR')
                            & (df['COD_TIPO_DISPOSITIVO'] == 'POS')
                            & (df['MARCA' ] == 'WPJ')
                            & (df['PRODUCTO_DE_LA_MARCA' ] == 'MIB')
                            & (df['COD_PREFIJO'] == '  ') 
                            & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                            & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            mensajes.append(f"[Falta] Billetera PJ Reversada")
        else:
            mensajes.append(f"[Correcto] Billetera PJ Reversada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Billetera PJ Reversada.xlsx')

        # Venta Billetera BNF Aprobada   
        df_temp = df.loc[(df['COD_PRESTACION'] == 'STAR')
                            & (df['COD_TIPO_DISPOSITIVO'] == 'POS')
                            & (df['MARCA' ] == 'BBF')
                            & (df['PRODUCTO_DE_LA_MARCA' ] == 'MIB')
                            & (df['COD_PREFIJO'] == '  ') 
                            & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                            & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            mensajes.append(f"[Falta] Billetera BNF Aprobada")
        else:
            mensajes.append(f"[Correcto] Billetera BNF Aprobada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Billetera BNF Aprobada.xlsx')

        # Venta Billetera BNF Reversada   
        df_temp = df.loc[(df['COD_PRESTACION'] == 'STAR')
                            & (df['COD_TIPO_DISPOSITIVO'] == 'POS')
                            & (df['MARCA' ] == 'BBF')
                            & (df['PRODUCTO_DE_LA_MARCA' ] == 'MIB')
                            & (df['COD_PREFIJO'] == '  ') 
                            & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                            & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            mensajes.append(f"[Falta] Billetera BNF Reversada")
        else:
            mensajes.append(f"[Correcto] Billetera BNF Reversada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Billetera BNF Reversada.xlsx')
        mensajes.append(f"\n")

        with open('reporte.txt', 'a') as file:
            for mensaje in mensajes:
                file.write("%s\n" % mensaje)
        file.close
    
    except Exception as e:
        logging.error(f'Error occurred: {e}', exc_info=True)
        mensajes.append(f"Hubo un error en el modulo Billeteras\n")
    else:
        logging.info('Billeteras() se ejecutó correctamente')
    return 0
