##########################################################################################################
# DOCUMENTACION: Automatizacion de consultas de casos de prueba Test de Regresión en POS de BANCARD S.A. #
# QA: Javier Bernal                                                                                      #
##########################################################################################################

import pandas as pd
import logging

def VentaTarjetasInternacionales(): 
    mensajes= []
    df = pd.read_excel('.\\resources\MET001.xlsx')
    mensajes.append(f"####VentaTarjetasInternacionales####\n")
    try:
        # Venta Tarjeta Internacional Aprobada
        df_temp = df.loc[(df['MARCA_LOCAL_INTERNACIONAL'] == 'I')
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]  
        
        if df_temp.empty:
            mensajes.append(f"[Falta] Venta Tarjeta Internacional Aprobada [Simulador, DESA]")
        else:
            mensajes.append(f"[Correcto] Venta Tarjeta Internacional Aprobada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Tarjeta Internacional Aprobada.xlsx')

        # Venta Tarjeta Internacional Reversada
        df_temp = df.loc[(df['MARCA_LOCAL_INTERNACIONAL'] == 'I')
                         & ((df['COD_RESPUESTA'] == 00) | (df['COD_RESPUESTA'] == '00'))
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')]
        count_row = df_temp.shape[0]  
        
        if df_temp.empty:
            mensajes.append(f"[Falta] Venta Tarjeta Internacional Reversada [Simulador, DESA]")
        else:
            mensajes.append(f"[Correcto] Venta Tarjeta Internacional Reversada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Tarjeta Internacional Reversada.xlsx')
        mensajes.append(f"\n")
        
        with open('reporte.txt', 'a') as file:
            for mensaje in mensajes:
                file.write("%s\n" % mensaje)
        file.close
    
    except Exception as e:
        logging.error(f'Error occurred: {e}', exc_info=True)
        mensajes.append(f"Hubo un error con el modulo VentaTarjetasInternacionales\n")
    else:
        logging.info('VentaTarjetasInternacionales() se ejecutó correctamente')
    return 0