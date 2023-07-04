##########################################################################################################
# DOCUMENTACION: Automatizacion de consultas de casos de prueba Test de Regresión en POS de BANCARD S.A. #
# QA: Javier Bernal                                                                                      #
##########################################################################################################

import pandas as pd
import logging

def OpSinTarjeta(): 
    mensajes=[]
    df = pd.read_excel('.\\resources\MET001.xlsx')
    mensajes.append(f"####OpSinTarjeta####\n")
    try:
        # Venta Operaciones Sin Tarjeta Aprobada   
        df_temp = df.loc[(df['COD_PRESTACION'] == 'STAR')
                         & (df['COD_TIPO_DISPOSITIVO'] == 'POS')
                         & (df['MARCA'] == 'ENT')
                         & (df['PRODUCTO_DE_LA_MARCA'] == 'PMO')
                         & (df['COD_PREFIJO'] == '  ') 
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == '    ')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            mensajes.append(f"[Falta] Op. Sin Tarjeta Aprobada [DESA]")
        else:
            mensajes.append(f"[Correcto] Op. Sin Tarjeta Aprobada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Op Sin Tarjeta Aprobada.xlsx')

        # Venta Operaciones Sin Tarjeta Reversada   
        df_temp = df.loc[(df['COD_PRESTACION'] == 'STAR')
                         & (df['COD_TIPO_DISPOSITIVO'] == 'POS')
                         & (df['MARCA'] == 'ENT')
                         & (df['PRODUCTO_DE_LA_MARCA'] == 'PMO')
                         & (df['COD_PREFIJO'] == '  ') 
                         & (df['COD_RESPUESTA'] == 00)
                         & (df['COD_RESPUESTA_EXTENDIDA'] == 'R001')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            mensajes.append(f"[Falta] Op. Sin Tarjeta Reversada [DESA]")
        else:
            mensajes.append(f"[Correcto] Op. Sin Tarjeta Reversada | {count_row} Caso(s) encontrado(s)")
            df_temp.to_excel('Op Sin Tarjeta Reversada.xlsx')
        mensajes.append("\n")

        with open('reporte.txt', 'a') as file:
            for mensaje in mensajes:
                file.write("%s\n" % mensaje)
        file.close
    
    except Exception as e:
        logging.error(f'Error occurred: {e}', exc_info=True)
        mensajes.append(f"Hubo un error con el modulo OpSinTarjeta\n")

    else:
        logging.info('OpSinTarjeta() se ejecutó correctamente')
    return 0