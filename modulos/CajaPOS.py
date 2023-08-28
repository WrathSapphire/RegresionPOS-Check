#############################################################################################################
# Regresión POS Check | Apache License 2.0 														    		#
# Software de generación automática de documentación para Test de Regresión en dispositivos POS         	#
# Javier Bernal | 2023																						#
# Source code: https://github.com/WrathfulNico/RegresionPOS-Check											#
#############################################################################################################

import pandas as pd
import logging

def CajaPOS(): 
    mensajes=[]
    df = pd.read_excel('.\\resources\MET001.xlsx')
    mensajes.append(f"####CajaPOS####\n")
    try:
        # Venta CajaPOS TD Banda Aprobada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TD  ')
                         & ((df['COD_PREFIJO'] == 90) | (df['COD_PREFIJO'] == '90'))
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & ((df['NRO_LOTE'] == 1) | (df['NRO_LOTE'] == '1'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]  
        
        if df_temp.empty:
            mensajes.append(f"[Falta] CajaPOS Venta CajaPOS TD Banda Aprobada")
        else:
            mensajes.append(f"[Correcto] CajaPOS Venta CajaPOS TD Banda Aprobada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('CajaPOS Venta TD Banda Aprobada.xlsx')

        # Venta CajaPOS TC Banda Aprobada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TC  ')
                         & ((df['COD_PREFIJO'] == 90) | (df['COD_PREFIJO'] == '90'))
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & ((df['NRO_LOTE'] == 1) | (df['NRO_LOTE'] == '1'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]  
        
        if df_temp.empty:
            mensajes.append(f"[Falta] CajaPOS Venta CajaPOS TC Banda Aprobada")
        else:
            mensajes.append(f"[Correcto] CajaPOS Venta CajaPOS TC Banda Aprobada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('CajaPOS Venta TC Banda Aprobada.xlsx')

        # Venta CajaPOS TD Chip Aprobada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TD  ')
                         & ((df['COD_PREFIJO'] == 5) | (df['COD_PREFIJO'] == '05'))
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & ((df['NRO_LOTE'] == 1) | (df['NRO_LOTE'] == '1'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]  
        
        if df_temp.empty:
            mensajes.append(f"[Falta] CajaPOS Venta CajaPOS TD Chip Aprobada")
        else:
            mensajes.append(f"[Correcto] CajaPOS Venta CajaPOS TD Chip Aprobada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('CajaPOS Venta TD Chip Aprobada.xlsx')

        # Venta CajaPOS TC Chip Aprobada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TC  ')
                         & ((df['COD_PREFIJO'] == 5) | (df['COD_PREFIJO'] == '05'))
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & ((df['NRO_LOTE'] == 1) | (df['NRO_LOTE'] == '1'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]  
        
        if df_temp.empty:
            mensajes.append(f"[Falta] CajaPOS Venta CajaPOS TC Chip Aprobada")
        else:
            mensajes.append(f"[Correcto] CajaPOS Venta CajaPOS TC Chip Aprobada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('CajaPOS Venta TC Chip Aprobada.xlsx')

        # Venta CajaPOS TD CTLS Aprobada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TD  ')
                         & ((df['COD_PREFIJO'] == 7) | (df['COD_PREFIJO'] == '07'))
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & ((df['NRO_LOTE'] == 1) | (df['NRO_LOTE'] == '1'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]  
        
        if df_temp.empty:
            mensajes.append(f"[Falta] CajaPOS Venta CajaPOS TD CTLS Aprobada")
        else:
            mensajes.append(f"[Correcto] CajaPOS Venta CajaPOS TD CTLS Aprobada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('CajaPOS Venta TD CTLS Aprobada.xlsx')

        # Venta CajaPOS TC CTLS Aprobada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TC  ')
                         & ((df['COD_PREFIJO'] == 7) | (df['COD_PREFIJO'] == '07'))
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & ((df['NRO_LOTE'] == 1) | (df['NRO_LOTE'] == '1'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]  
        
        if df_temp.empty:
            mensajes.append(f"[Falta] CajaPOS Venta CajaPOS TC CTLS Aprobada")
        else:
            mensajes.append(f"[Correcto] CajaPOS Venta CajaPOS TC CTLS Aprobada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('CajaPOS Venta TC CTLS Aprobada.xlsx')

        # Venta CajaPOS QR TC Aprobada   
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TCQR')
                         & (df['COD_TIPO_DISPOSITIVO'] == 'APP')
                         & ((df['COD_PREFIJO'] == 00) | (df['COD_PREFIJO'] == '00'))
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         #& ((df['NRO_LOTE'] == 1) | (df['NRO_LOTE'] == '1'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            mensajes.append(f"[Falta] CajaPOS Venta CajaPOS QR TC Aprobada")
        else:
            mensajes.append(f"[Correcto] CajaPOS Venta CajaPOS QR TC Aprobada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('CajaPOS Venta QR TC Aprobada.xlsx')

        # Venta CajaPOS QR TD Aprobada   
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TDQR')
                         & (df['COD_TIPO_DISPOSITIVO'] == 'APP')
                         & ((df['COD_PREFIJO'] == 00) | (df['COD_PREFIJO'] == '00'))
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         #& ((df['NRO_LOTE'] == 1) | (df['NRO_LOTE'] == '1'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            mensajes.append(f"[Falta] CajaPOS Venta CajaPOS QR TD Aprobada")
        else:
            mensajes.append(f"[Correcto] CajaPOS Venta CajaPOS QR TD Aprobada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('CajaPOS Venta QR TD Aprobada.xlsx')

        # Venta CajaPOS Billetera ZIMPLE Aprobada   
        df_temp = df.loc[(df['COD_PRESTACION'] == 'STAR')
                         & (df['COD_TIPO_DISPOSITIVO'] == 'POS')
                         & (df['MARCA' ] == 'MIB')
                         & (df['PRODUCTO_DE_LA_MARCA' ] == 'MIB')
                         & (df['COD_PREFIJO'] == '  ') 
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         #& ((df['NRO_LOTE'] == 1) | (df['NRO_LOTE'] == '1'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            mensajes.append(f"[Falta] CajaPOS Billetera ZIMPLE Aprobada")
        else:
            mensajes.append(f"[Correcto] CajaPOS Billetera ZIMPLE Aprobada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('CajaPOS Billetera ZIMPLE Aprobada.xlsx')

        # Canje TC Lealtad Aprobada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TC  ')
                         & ((df['COD_TRANSACCION'] == 76) | (df['COD_TRANSACCION'] == '76'))                     
                         & (df['COD_PREFIJO'] == '  ')
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         #& ((df['NRO_LOTE'] == 1) | (df['NRO_LOTE'] == '1'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]

        count_row = df_temp.shape[0] 

        if df_temp.empty:
            mensajes.append(f"[Falta] CajaPOS Canje TC Lealtad Aprobada")
        else:
            mensajes.append(f"[Correcto] CajaPOS Canje TC Lealtad Aprobada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('CajaPOS Canje TC Lealtad Aprobada.xlsx')
        mensajes.append(f'\n')

        with open('reporte.txt', 'a') as file:
            for mensaje in mensajes:
                file.write("%s\n" % mensaje)
                
        file.close
    
    except Exception as e:
        logging.error(f'Error occurred: {e}', exc_info=True)
        mensajes.append(f"Hubo un error en el modulo CajaPOS\n")
    else:
        logging.info('CajaPOS() se ejecutó correctamente')

    return 0
