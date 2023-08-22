#############################################################################################################
# Regresión POS Check | Apache License 2.0 			    													#
# Software de generación automática de documentación para Test de Regresión en dispositivos POS de BANCARD	#
# Javier Bernal | 2023																						#
# Source code: https://github.com/WrathfulNico/RegresionPOS-Check											#
#############################################################################################################

import pandas as pd
import logging

def VentaSaldo():
    mensajes= []
    df = pd.read_excel('.\\resources\MET001.xlsx')
    mensajes.append(f"####VentaSaldo####\n")
    try:
        # Venta Saldo TD Banda Aprobada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'VMTE')
		                 & ((df['COD_MEDIO_PAGO'] == 2) | (df['COD_MEDIO_PAGO'] == '02'))
                         & ((df['COD_PREFIJO'] == 90) | (df['COD_PREFIJO'] == '90'))
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            mensajes.append(f"[Falta] Venta Saldo TD Banda Aprobada")
        else:
            mensajes.append(f"[Correcto] Venta Saldo TD Banda Aprobada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Saldo TD Banda Aprobada.xlsx')

        # Venta Saldo TD Banda Reversada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'VMTE')
		                 & ((df['COD_MEDIO_PAGO'] == 2) | (df['COD_MEDIO_PAGO'] == '02'))
                         & ((df['COD_PREFIJO'] == 90) | (df['COD_PREFIJO'] == '90'))
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            mensajes.append(f"[Falta] Venta Saldo TD Banda Reversada")
        else:
            mensajes.append(f"[Correcto] Venta Saldo TD Banda Reversada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Saldo TD Banda Reversada.xlsx')

        # Venta Saldo TC Banda Aprobada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'VMTE')
		                 & ((df['COD_MEDIO_PAGO'] == 1) | (df['COD_MEDIO_PAGO'] == '01'))
                         & ((df['COD_PREFIJO'] == 90) | (df['COD_PREFIJO'] == '90'))
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            mensajes.append(f"[Falta] Venta Saldo TC Banda Aprobada")
        else:
            mensajes.append(f"[Correcto] Venta Saldo TC Banda Aprobada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Saldo TC Banda Aprobada.xlsx')

        # Venta Saldo TC Banda Reversada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'VMTE')
		                 & ((df['COD_MEDIO_PAGO'] == 1) | (df['COD_MEDIO_PAGO'] == '01'))
                         & ((df['COD_PREFIJO'] == 90) | (df['COD_PREFIJO'] == '90'))
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            mensajes.append(f"[Falta] Venta Saldo TC Banda Reversada")
        else:
            mensajes.append(f"[Correcto] Venta Saldo TC Banda Reversada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Saldo TC Banda Reversada.xlsx')

        # Venta Saldo TD Chip Aprobada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'VMTE')
		                 & ((df['COD_MEDIO_PAGO'] == 2) | (df['COD_MEDIO_PAGO'] == '02'))
                         & ((df['COD_PREFIJO'] == 5) | (df['COD_PREFIJO'] == '05'))
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]
        
        if df_temp.empty:
            mensajes.append(f"[Falta] Venta Saldo TD Chip Aprobada")
        else:
            mensajes.append(f"[Correcto] Venta Saldo TD Chip Aprobada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Saldo TD Chip Aprobada.xlsx')

        # Venta Saldo TD Chip Reversada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'VMTE')
		                 & ((df['COD_MEDIO_PAGO'] == 2) | (df['COD_MEDIO_PAGO'] == '02'))
                         & ((df['COD_PREFIJO'] == 5) | (df['COD_PREFIJO'] == '05'))
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            mensajes.append(f"[Falta] Venta Saldo TD Chip Reversada")
        else:
            mensajes.append(f"[Correcto] Venta Saldo TD Chip Reversada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Saldo TD Chip Reversada.xlsx')

        # Venta Saldo TC Chip Aprobada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'VMTE')
		                 & ((df['COD_MEDIO_PAGO'] == 1) | (df['COD_MEDIO_PAGO'] == '01'))
                         & ((df['COD_PREFIJO'] == 5) | (df['COD_PREFIJO'] == '05'))
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]
        
        if df_temp.empty:
            mensajes.append(f"[Falta] Venta Saldo TC Chip Aprobada")
        else:
            mensajes.append(f"[Correcto] Venta Saldo TC Chip Aprobada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Saldo TC Chip Aprobada.xlsx')

        # Venta Saldo TC Chip Reversada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'VMTE')
		                 & ((df['COD_MEDIO_PAGO'] == 1) | (df['COD_MEDIO_PAGO'] == '01'))
                         & ((df['COD_PREFIJO'] == 5) | (df['COD_PREFIJO'] == '05'))
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            mensajes.append(f"[Falta] Venta Saldo TC Chip Reversada")
        else:
            mensajes.append(f"[Correcto] Venta Saldo TC Chip Reversada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Saldo TC Chip Reversada.xlsx')

        # Venta Saldo TD CTLS Aprobada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'VMTE')
		                 & ((df['COD_MEDIO_PAGO'] == 2) | (df['COD_MEDIO_PAGO'] == '02'))
                         & ((df['COD_PREFIJO'] == 7) | (df['COD_PREFIJO'] == '07'))
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]
        
        if df_temp.empty:
            mensajes.append(f"[Falta] Venta Saldo TD CTLS Aprobada")
        else:
            mensajes.append(f"[Correcto] Venta Saldo TD CTLS Aprobada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Saldo TD CTLS Aprobada.xlsx')

        # Venta Saldo TD CTLS Reversada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'VMTE')
		                 & ((df['COD_MEDIO_PAGO'] == 2) | (df['COD_MEDIO_PAGO'] == '02'))
                         & ((df['COD_PREFIJO'] == 7) | (df['COD_PREFIJO'] == '07'))
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            mensajes.append(f"[Falta] Venta Saldo TD CTLS Reversada")
        else:
            mensajes.append(f"[Correcto] Venta Saldo TD CTLS Reversada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Saldo TD CTLS Reversada.xlsx')

        # Venta Saldo TC CTLS Aprobada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'VMTE')
		                 & ((df['COD_MEDIO_PAGO'] == 1) | (df['COD_MEDIO_PAGO'] == '01'))
                         & ((df['COD_PREFIJO'] == 7) | (df['COD_PREFIJO'] == '07'))
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]
        
        if df_temp.empty:
            mensajes.append(f"[Falta] Venta Saldo TC CTLS Aprobada")
        else:
            mensajes.append(f"[Correcto] Venta Saldo TC CTLS Aprobada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Saldo TC CTLS Aprobada.xlsx')

        # Venta Saldo TC CTLS Reversada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'VMTE')
		                 & ((df['COD_MEDIO_PAGO'] == 1) | (df['COD_MEDIO_PAGO'] == '01'))
                         & ((df['COD_PREFIJO'] == 7) | (df['COD_PREFIJO'] == '07'))
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            mensajes.append(f"[Falta] Venta Saldo TC CTLS Reversada")
        else:
            mensajes.append(f"[Correcto] Venta Saldo TC CTLS Reversada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Saldo TC CTLS Reversada.xlsx')
        mensajes.append(f"\n")

        with open('reporte.txt', 'a') as file:
            for mensaje in mensajes:
                file.write("%s\n" % mensaje)
        file.close
    
    except Exception as e:
        logging.error(f'Error occurred: {e}', exc_info=True)
        mensajes.append(f"Hubo un error con el modulo VentaSaldo\n")
    else:
        logging.info('VentaSaldo() se ejecutó correctamente')
    return 0