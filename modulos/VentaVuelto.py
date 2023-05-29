##########################################################################################################
# DOCUMENTACION: Automatizacion de consultas de casos de prueba Test de Regresión en POS de BANCARD S.A. #
# QA: Javier Bernal                                                                                      #
##########################################################################################################

import pandas as pd
import logging
logging.basicConfig(filename='registro.log', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s:%(message)s')

df = pd.read_excel('MET001.xlsx')
def VentaVuelto():
    print("####VentaVuelto####\n")
    try:
        # Venta Vuelto TD Aprobada
        df_temp = df.loc[(df['PRESTACION'] == 'TD  ')
                         & (df['COD_PAGO'] == 2)
                         & (df['CASHBACK'] == 'S')
                         & (df['COD_RE'] == 00)
                         & (df['COD_REEXT'] == '    ')]

        count_row = df_temp.shape[0]
        if df_temp.empty:
            print("[Falta] Venta Vuelto TD Aprobada")
        else:
            print("[Correcto] Venta Vuelto TD Aprobada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Vuelto TD Aprobada.xlsx')


        # Venta Vuelto TD Reversada
        df_temp = df.loc[(df['PRESTACION'] == 'TD  ')
                         & (df['COD_PAGO'] == 2)
                         & (df['CASHBACK'] == 'S')
                         & (df['COD_RE'] == 00)
                         & (df['COD_REEXT'] == 'R001')]
        count_row = df_temp.shape[0]

        if df_temp.empty:
            print("[Falta] Venta Vuelto TD Reversada")
        else:
            print("[Correcto] Venta Vuelto TD Reversada", "|", count_row, "Caso(s) encontrado(s)")
            df_temp.to_excel('Venta Vuelto TD Reversada.xlsx')

        print("\n")
    except Exception as e:
        logging.error(f'Error occurred: {e}', exc_info=True)
        print("Hugo un error con el modulo VentaVuelto\n")
    else:
        logging.info('VentaVuelto() se ejecutó correctamente')
    return 0