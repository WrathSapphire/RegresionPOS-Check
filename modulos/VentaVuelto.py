##########################################################################################################
# DOCUMENTACION: Automatizacion de consultas de casos de prueba Test de Regresión en POS de BANCARD S.A. #
# QA: Javier Bernal                                                                                      #
##########################################################################################################

import pandas as pd
import logging

def VentaVuelto():
    mensajes=[]
    df = pd.read_excel('.\\resources\MET001.xlsx')
    mensajes.append(f"####VentaVuelto####\n")
    try:
        # Venta Vuelto TD Aprobada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TD  ')
                         & (df['COD_MEDIO_PAGO'] == 2)
                         & (df['CASHBACK'] == 'S')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]
        
        if df_temp.empty:
            mensajes.append(f"[Falta] Venta Vuelto TD Aprobada")
        else:
            mensajes.append(f"[Correcto] Venta Vuelto TD Aprobada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Vuelto TD Aprobada.xlsx')

        # Venta Vuelto TD Reversada
        df_temp = df.loc[(df['COD_PRESTACION'] == 'TD  ')
                         & (df['COD_MEDIO_PAGO'] == 2)
                         & (df['CASHBACK'] == 'S')
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            mensajes.append(f"[Falta] Venta Vuelto TD Reversada")
        else:
            mensajes.append(f"[Correcto] Venta Vuelto TD Reversada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Vuelto TD Reversada.xlsx')
        mensajes.append(f"\n")

        with open('reporte.txt', 'a') as file:
            for mensaje in mensajes:
                file.write("%s\n" % mensaje)
        file.close
    
    except Exception as e:
        logging.error(f'Error occurred: {e}', exc_info=True)
        mensajes.append(f"Hubo un error con el modulo VentaVuelto\n")
    else:
        logging.info('VentaVuelto() se ejecutó correctamente')
    return 0