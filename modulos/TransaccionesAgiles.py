##########################################################################################################
# DOCUMENTACION: Automatizacion de consultas de casos de prueba Test de Regresión en POS de BANCARD S.A. #
# QA: Javier Bernal                                                                                      #
##########################################################################################################

import pandas as pd
import logging

def TransaccionesAgiles(): 
    mensajes=[]
    df = pd.read_excel('.\\resources\MET001.xlsx')
    mensajes.append(f"####TransaccionesAgiles####\n")
    try:
        # Transacción Ágil TD Aprobada 
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TD  ')
                         & ((df['COD_PREFIJO'] == 7) | (df['COD_PREFIJO'] == '07'))
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')
                         & (df['CODIGO_OPERACION'] == '01')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            mensajes.append(f"[Falta] Transacción Ágil TD Aprobada")
        else:
            mensajes.append(f"[Correcto] Transacción Ágil TD Aprobada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Transacción Ágil TD Aprobada.xlsx')

        # Transacción Ágil TD PIN Aprobada 
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TD  ')
                         & ((df['COD_PREFIJO'] == 7) | (df['COD_PREFIJO'] == '07'))
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')
                         & (df['CODIGO_OPERACION'] == '00')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            mensajes.append(f"[Falta] Transacción Ágil TD PIN Aprobada")
        else:
            mensajes.append(f"[Correcto] Transacción Ágil TD PIN Aprobada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Transacción Ágil TD PIN Aprobada.xlsx')

        # Transacción Ágil TD Reversada 
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TD  ')
                         & ((df['COD_PREFIJO'] == 7) | (df['COD_PREFIJO'] == '07'))
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')
                         & (df['CODIGO_OPERACION'] == '01')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            mensajes.append(f"[Falta] Transacción Ágil TD Reversada")
        else:
            mensajes.append(f"[Correcto] Transacción Ágil TD Reversada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Transacción Ágil TD Reversada.xlsx')

        # Transacción Ágil TC Aprobada 
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TC  ')
                         & ((df['COD_PREFIJO'] == 7) | (df['COD_PREFIJO'] == '07'))
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')
                         & (df['CODIGO_OPERACION'] == '01')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            mensajes.append(f"[Falta] Transacción Ágil TC Aprobada")
        else:
            mensajes.append(f"[Correcto] Transacción Ágil TC Aprobada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Transacción Ágil TC Aprobada.xlsx')

        # Transacción Ágil TC PIN Aprobada 
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TC  ')
                         & ((df['COD_PREFIJO'] == 7) | (df['COD_PREFIJO'] == '07'))
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')
                         & (df['CODIGO_OPERACION'] == '00')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            mensajes.append(f"[Falta] Transacción Ágil TC PIN Aprobada")
        else:
            mensajes.append(f"[Correcto] Transacción Ágil TC PIN Aprobada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Transacción Ágil TC PIN Aprobada.xlsx')

        # Transacción Ágil TC Reversada 
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TC  ')
                         & ((df['COD_PREFIJO'] == 7) | (df['COD_PREFIJO'] == '07'))
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')
                         & (df['CODIGO_OPERACION'] == '01')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            mensajes.append(f"[Falta] Transacción Ágil TC Reversada")
        else:
            mensajes.append(f"[Correcto] Transacción Ágil TC Reversada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Transacción Ágil TC Reversada.xlsx')
        mensajes.append(f"\n")

        with open('reporte.txt', 'a') as file:
            for mensaje in mensajes:
                file.write("%s\n" % mensaje)
        file.close
    
    except Exception as e:
        logging.error(f'Error occurred: {e}', exc_info=True)
        mensajes.append(f"Hubo un error con el modulo TransaccionesAgiles\n")

    else:
        logging.info('TransaccionesAgiles() se ejecutó correctamente')
    return 0