##########################################################################################################
# DOCUMENTACION: Automatizacion de consultas de casos de prueba Test de Regresión en POS de BANCARD S.A. #
# QA: Javier Bernal                                                                                      #
##########################################################################################################

import pandas as pd
import logging
logging.basicConfig(filename='registro.log', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s:%(message)s')

df = pd.read_excel('MET001.xlsx')


def DebitoCreditoExtranjero(): 
    try:
        print("DebitoCredito Extranjero por terminar\n")
    except Exception as e:
        logging.error(f'Error occurred: {e}', exc_info=True)
    else:
        logging.info('DebitoCreditoExtranjero() ran successfully')
    return 0