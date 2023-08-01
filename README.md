Regresión Check v1.2 | Apache License 2.0
Software de generación automática de documentación para Test de Regresión en dispositivos POS de BANCARD
Javier Bernal | 2023
Source code: https://github.com/WrathfulNico/RegresionPOS-Check

Requisitos:
Python 3.11 o superior
numpy 1.24.3 o superior
pandas 2.0.1 o superior
openpyxl 3.1 o superior
java SE-17 o superior para DBConnect

Regresión Check v1.2 es un software que automatiza la generación de documentación y evidencias de prueba para casos de "Test de Regresión" en dispositivos de POS.
Este software lee un archivo excel con las transacciones realizadas en los dispositivos de POS y filtra los diferentes casos de pruebas y combinaciones existentes según los criterios definidos por el usuario.
Luego, crea un reporte que indica si se encontraron todos los casos esperados, la cantidad de transacciones y el resultado de cada set de pruebas.
Además, cada caso de prueba exitoso genera un archivo excel donde se detallan las transacciones que corresponden a ese caso, facilitando así el análisis y la validación de las pruebas.




#TODO: MODULO DE CONSULTA PARA INFONET COBRANZAS
Para Infonet Cobranzas añadir los siguientes filtros para la consulta en el ambiente de desarrollo:

WHERE GE65TRACOD = 72 /*TRN PAGOS-INFONET COBRANZAS*/
AND GE42SRVIDE = 'TIC' AND GE49TIPDIS = 'WEB' /*TIC - TRANSACCIONES INFONET COBRANZAS || WEB*/ 
AND ME01CCOCOD =136 AND ME01CCOSUC = 92
AND GE70RESEXT =''
AND ME01MOVFEC >= '20230510'				/*FECHA*/