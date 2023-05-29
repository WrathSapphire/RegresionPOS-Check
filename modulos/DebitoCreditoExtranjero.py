##########################################################################################################
# DOCUMENTACION: Automatizacion de consultas de casos de prueba Test de Regresión en POS de BANCARD S.A. #
# QA: Javier Bernal                                                                                      #
##########################################################################################################




#####################################
#   Modulo en desuso debido         #
#   debido a que se verifica        #
#   la pantalla debito/credito      #
#   con una tarjeta local           #
#   y no es posible                 #
#   verificar por base de datos     #
#####################################
import pandas as pd
import logging
logging.basicConfig(filename='registro.log', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s:%(message)s')

df = pd.read_excel('MET001.xlsx')


def DebitoCreditoExtranjero(): 
    print("####DebitoCreditoExtranjero####\n")
    try:
        print("DebitoCredito Extranjero por terminar\n")
    except Exception as e:
        logging.error(f'Error occurred: {e}', exc_info=True)
        print("Hugo un error con el modulo DebitoCreditoExtranjero\n")
    else:
        logging.info('DebitoCreditoExtranjero() se ejecutó correctamente')
    return 0