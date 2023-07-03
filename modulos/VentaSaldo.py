##########################################################################################################
# DOCUMENTACION: Automatizacion de consultas de casos de prueba Test de Regresión en POS de BANCARD S.A. #
# QA: Javier Bernal                                                                                      #
##########################################################################################################

import pandas as pd
import logging

def VentaSaldo():
    df = pd.read_excel('.\\resources\MET001.xlsx')
    print("####VentaSaldo####\n")
    try:
        # Venta Saldo TD Banda Aprobada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'VMTE')
                         & (df['COD_MEDIO_PAGO'] == 2)
                         & (df['COD_PREFIJO'] == '90')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Venta Saldo TD Banda Aprobada")
        else:
            print("[Correcto] Venta Saldo TD Banda Aprobada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Saldo TD Banda Aprobada.xlsx')

        # Venta Saldo TD Banda Reversada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'VMTE')
                         & (df['COD_MEDIO_PAGO'] == 2)
                         & (df['COD_PREFIJO'] == '90')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Venta Saldo TD Banda Reversada")
        else:
            print("[Correcto] Venta Saldo TD Banda Reversada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Saldo TD Banda Reversada.xlsx')

        # Venta Saldo TC Banda Aprobada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'VMTE')
                         & (df['COD_MEDIO_PAGO'] == 1)
                         & (df['COD_PREFIJO'] == '90')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Venta Saldo TC Banda Aprobada")
        else:
            print("[Correcto] Venta Saldo TC Banda Aprobada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Saldo TC Banda Aprobada.xlsx')

        # Venta Saldo TC Banda Reversada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'VMTE')
                         & (df['COD_MEDIO_PAGO'] == 1)
                         & (df['COD_PREFIJO'] == '90')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Venta Saldo TC Banda Reversada")
        else:
            print("[Correcto] Venta Saldo TC Banda Reversada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Saldo TC Banda Reversada.xlsx')

        # Venta Saldo TD Chip Aprobada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'VMTE')
                         & (df['COD_MEDIO_PAGO'] == 2)
                         & (df['COD_PREFIJO'] == '05')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]
        
        if df_temp.empty:
            print("[Falta] Venta Saldo TD Chip Aprobada")
        else:
            print("[Correcto] Venta Saldo TD Chip Aprobada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Saldo TD Chip Aprobada.xlsx')

        # Venta Saldo TD Chip Reversada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'VMTE')
                         & (df['COD_MEDIO_PAGO'] == 2)
                         & (df['COD_PREFIJO'] == '05')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Venta Saldo TD Chip Reversada")
        else:
            print("[Correcto] Venta Saldo TD Chip Reversada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Saldo TD Chip Reversada.xlsx')

        # Venta Saldo TC Chip Aprobada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'VMTE')
                         & (df['COD_MEDIO_PAGO'] == 1)
                         & (df['COD_PREFIJO'] == '05')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]
        
        if df_temp.empty:
            print("[Falta] Venta Saldo TC Chip Aprobada")
        else:
            print("[Correcto] Venta Saldo TC Chip Aprobada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Saldo TC Chip Aprobada.xlsx')

        # Venta Saldo TC Chip Reversada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'VMTE')
                         & (df['COD_MEDIO_PAGO'] == 1)
                         & (df['COD_PREFIJO'] == '05')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Venta Saldo TC Chip Reversada")
        else:
            print("[Correcto] Venta Saldo TC Chip Reversada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Saldo TC Chip Reversada.xlsx')

        # Venta Saldo TD CTLS Aprobada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'VMTE')
                         & (df['COD_MEDIO_PAGO'] == 2)
                         & (df['COD_PREFIJO'] == '07')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]
        
        if df_temp.empty:
            print("[Falta] Venta Saldo TD CTLS Aprobada")
        else:
            print("[Correcto] Venta Saldo TD CTLS Aprobada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Saldo TD CTLS Aprobada.xlsx')

        # Venta Saldo TD CTLS Reversada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'VMTE')
                         & (df['COD_MEDIO_PAGO'] == 2)
                         & (df['COD_PREFIJO'] == '07')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Venta Saldo TD CTLS Reversada")
        else:
            print("[Correcto] Venta Saldo TD CTLS Reversada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Saldo TD CTLS Reversada.xlsx')

        # Venta Saldo TC CTLS Aprobada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'VMTE')
                         & (df['COD_MEDIO_PAGO'] == 1)
                         & (df['COD_PREFIJO'] == '07')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]
        
        if df_temp.empty:
            print("[Falta] Venta Saldo TC CTLS Aprobada")
        else:
            print("[Correcto] Venta Saldo TC CTLS Aprobada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Saldo TC CTLS Aprobada.xlsx')

        # Venta Saldo TC CTLS Reversada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'VMTE')
                         & (df['COD_MEDIO_PAGO'] == 1)
                         & (df['COD_PREFIJO'] == '07')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Venta Saldo TC CTLS Reversada")
        else:
            print("[Correcto] Venta Saldo TC CTLS Reversada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Saldo TC CTLS Reversada.xlsx')
        print("\n")
    
    except Exception as e:
        logging.error(f'Error occurred: {e}', exc_info=True)
        print("Hubo un error con el modulo VentaSaldo\n")
    else:
        logging.info('VentaSaldo() se ejecutó correctamente')
    return 0