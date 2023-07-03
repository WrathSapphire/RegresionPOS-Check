##########################################################################################################
# DOCUMENTACION: Automatizacion de consultas de casos de prueba Test de Regresión en POS de BANCARD S.A. #
# QA: Javier Bernal                                                                                      #
##########################################################################################################

import pandas as pd
import logging

def VentaCuota():
    df = pd.read_excel('.\\resources\MET001.xlsx') 
    print("####VentaCuota####\n")
    try:
        # Venta Cuota Banda Aprobada   
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TC  ')
                         & (df['NRO_CUOTA'] > 1)
                         & (df['COD_PREFIJO'] =='90') 
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Venta Cuota Banda Aprobada")
        else:
            print("[Correcto] Venta Cuota Banda Aprobada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Cuota Banda Aprobada.xlsx')

        # Venta Cuota Banda Reversada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TC  ')
                         & (df['NRO_CUOTA'] > 1)
                         & (df['COD_PREFIJO'] =='90')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Venta Cuota Banda Reversada")
        else:
            print("[Correcto] Venta Cuota Banda Reversada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Cuota Banda Reversada.xlsx')

        # Venta Cuota Chip Aprobada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TC  ')
                         & (df['NRO_CUOTA'] > 1)
                         & (df['COD_PREFIJO'] =='05') 
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Venta Cuota Chip Aprobada")
        else:
            print("[Correcto] Venta Cuota Chip Aprobada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Cuota Chip Aprobada.xlsx')

        # Venta Cuota Chip Reversada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TC  ')
                         & (df['NRO_CUOTA'] > 1)
                         & (df['COD_PREFIJO'] =='05')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Venta Cuota Chip Reversada")
        else:
            print("[Correcto] Venta Cuota Chip Reversada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Cuota Chip Reversada.xlsx')

        # Venta Cuota CTLS Aprobada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TC  ')
                         & (df['NRO_CUOTA'] > 1)
                         & (df['COD_PREFIJO'] =='07')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Venta Cuota CTLS Aprobada")
        else:
            print("[Correcto] Venta Cuota CTLS Aprobada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Cuota CTLS Aprobada.xlsx')

        # Venta Cuota CTLS Reversada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TC  ')
                         & (df['NRO_CUOTA'] > 1)
                         & (df['COD_PREFIJO'] =='07')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')]
        count_row = df_temp.shape[0]
        
        if df_temp.empty:
            print("[Falta] Venta Cuota CTLS Reversada")
        else:
            print("[Correcto] Venta Cuota CTLS Reversada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Cuota CTLS Reversada.xlsx')
        print("\n")

    except Exception as e:
        logging.error(f'Error occurred: {e}', exc_info=True)
        print("Hubo un error con el modulo VentaCuota\n")
    else:
        logging.info('VentaCuota() se ejecutó correctamente')
    return 0