##########################################################################################################
# DOCUMENTACION: Automatizacion de consultas de casos de prueba Test de Regresión en POS de BANCARD S.A. #
# QA: Javier Bernal                                                                                      #
##########################################################################################################

import pandas as pd
import logging


def VentaTDTC(): 
    df = pd.read_excel('.\\resources\MET001.xlsx')
    print("####VentaTDTC####\n")
    try:
        # Venta TD Banda Aprobada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TD  ')
                         & (df['COD_PREFIJO'] == '90') 
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]  
        
        if df_temp.empty:
            print("[Falta] Venta TD Banda Aprobada")
        else:
            print("[Correcto] Venta TD Banda Aprobada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta TD Banda Aprobada.xlsx')

        # Venta TD Banda Reversada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TD  ')
                         & (df['COD_PREFIJO'] == '90')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Venta TD Banda Reversada")
        else:
            print("[Correcto] Venta TD Banda Reversada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta TD Banda Reversada.xlsx')

        # Venta TC Banda Aprobada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TC  ')
                         & (df['COD_PREFIJO'] == '90')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]  
        
        if df_temp.empty:
            print("[Falta] Venta TC Banda Aprobada")
        else:
            print("[Correcto] Venta TC Banda Aprobada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta TC Banda Aprobada.xlsx')

        # Venta TC Banda Reversada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TC  ')
                         & (df['COD_PREFIJO'] == '90')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')]
        count_row = df_temp.shape[0]  

        if df_temp.empty:
            print("[Falta] Venta TC Banda Reversada")
        else:
            print("[Correcto] Venta TC Banda Reversada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta TC Banda Reversada.xlsx')

        # Venta TD Chip Aprobada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TD  ')
                         & (df['COD_PREFIJO'] == '05')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]  
        
        if df_temp.empty:
            print("[Falta] Venta TD Chip Aprobada")
        else:
            print("[Correcto] Venta TD Chip Aprobada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta TD Chip Aprobada.xlsx')

        # Venta TD Chip Reversada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TD  ')
                         & (df['COD_PREFIJO'] == '05')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')]
        count_row = df_temp.shape[0]  

        if df_temp.empty:
            print("[Falta] Venta TD Chip Reversada")
        else:
            print("[Correcto] Venta TD Chip Reversada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta TD Chip Reversada.xlsx')

        # Venta TC Chip Aprobada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TC  ')
                         & (df['COD_PREFIJO'] == '05')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]  
        
        if df_temp.empty:
            print("[Falta] Venta TC Chip Aprobada")
        else:
            print("[Correcto] Venta TC Chip Aprobada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta TC Chip Aprobada.xlsx')

        # Venta TC Chip Reversada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TC  ')
                         & (df['COD_PREFIJO'] == '05')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')]
        count_row = df_temp.shape[0]  

        if df_temp.empty:
            print("[Falta] Venta TC Chip Reversada")
        else:
            print("[Correcto] Venta TC Chip Reversada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta TC Chip Reversada.xlsx')

        # Venta TD CTLS Aprobada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TD  ')
                         & (df['COD_PREFIJO'] == '07')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]  
        
        if df_temp.empty:
            print("[Falta] Venta TD CTLS Aprobada")
        else:
            print("[Correcto] Venta TD CTLS Aprobada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta TD CTLS Aprobada.xlsx')

        # Venta TD CTLS Reversada

        df_temp = df.loc[(df['COD_PRESTACION'] == 'TD  ')
                         & (df['COD_PREFIJO'] == '07')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')]
        count_row = df_temp.shape[0]  

        if df_temp.empty:
            print("[Falta] Venta TD CTLS Reversada")
        else:
            print("[Correcto] Venta TD CTLS Reversada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta TD CTLS Reversada.xlsx')

        # Venta TC CTLS Aprobada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TC  ')
                         & (df['COD_PREFIJO'] == '07')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]  
        
        if df_temp.empty:
            print("[Falta] Venta TC CTLS Aprobada")
        else:
            print("[Correcto] Venta TC CTLS Aprobada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta TC CTLS Aprobada.xlsx')

        # Venta TC CTLS Reversada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TC  ')
                         & (df['COD_PREFIJO'] == '07')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')]
        count_row = df_temp.shape[0]  

        if df_temp.empty:
            print("[Falta] Venta TC CTLS Reversada")
        else:
            print("[Correcto] Venta TC CTLS Reversada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta TC CTLS Reversada.xlsx')
        print("\n")
    
    except Exception as e:
        logging.error(f'Error occurred: {e}', exc_info=True)
        print("Hubo un error con el modulo VentaTDTC\n")
    else:
        logging.info('VentaTDTC() se ejecutó correctamente')
    return 0