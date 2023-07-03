##########################################################################################################
# DOCUMENTACION: Automatizacion de consultas de casos de prueba Test de Regresión en POS de BANCARD S.A. #
# QA: Javier Bernal                                                                                      #
##########################################################################################################

import pandas as pd
import logging

def TransaccionesAgiles(): 
    df = pd.read_excel('.\\resources\MET001.xlsx')
    print("####TransaccionesAgiles####\n")
    try:
        # Transacción Ágil TD Aprobada 
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TD  ')
                         & (df['COD_PREFIJO'] == '07')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')
                         & (df['CODIGO_OPERACION'] == 1)]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Transacción Ágil TD Aprobada")
        else:
            print("[Correcto] Transacción Ágil TD Aprobada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Transacción Ágil TD Aprobada.xlsx')

        # Transacción Ágil TD PIN Aprobada 
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TD  ')
                         & (df['COD_PREFIJO'] == '07')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')
                         & (df['CODIGO_OPERACION'] == 0)]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Transacción Ágil TD PIN Aprobada")
        else:
            print("[Correcto] Transacción Ágil TD PIN Aprobada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Transacción Ágil TD PIN Aprobada.xlsx')

        # Transacción Ágil TD Reversada 
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TD  ')
                         & (df['COD_PREFIJO'] == '07')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')
                         & (df['CODIGO_OPERACION'] == 1)]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Transacción Ágil TD Reversada")
        else:
            print("[Correcto] Transacción Ágil TD Reversada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Transacción Ágil TD Reversada.xlsx')

        # Transacción Ágil TC Aprobada 
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TC  ')
                         & (df['COD_PREFIJO'] == '07')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')
                         & (df['CODIGO_OPERACION'] == 1)]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Transacción Ágil TC Aprobada")
        else:
            print("[Correcto] Transacción Ágil TC Aprobada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Transacción Ágil TC Aprobada.xlsx')

        # Transacción Ágil TC PIN Aprobada 
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TC  ')
                         & (df['COD_PREFIJO'] == '07')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')
                         & (df['CODIGO_OPERACION'] == 0)]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Transacción Ágil TC PIN Aprobada")
        else:
            print("[Correcto] Transacción Ágil TC PIN Aprobada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Transacción Ágil TC PIN Aprobada.xlsx')

        # Transacción Ágil TC Reversada 
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TC  ')
                         & (df['COD_PREFIJO'] == '07')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')
                         & (df['CODIGO_OPERACION'] == 1)]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Transacción Ágil TC Reversada")
        else:
            print("[Correcto] Transacción Ágil TC Reversada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Transacción Ágil TC Reversada.xlsx')
        print("\n")
    
    except Exception as e:
        logging.error(f'Error occurred: {e}', exc_info=True)
        print("Hubo un error con el modulo TransaccionesAgiles\n")

    else:
        logging.info('TransaccionesAgiles() se ejecutó correctamente')
    return 0