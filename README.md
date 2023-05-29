##########################################################################################################
# DOCUMENTACION: Automatizacion de consultas de casos de prueba Test de Regresión en POS de BANCARD S.A. #
# QA: Javier Bernal                                                                                      #
##########################################################################################################

Requisitos:
Python 3.11 o superior
numpy 1.24.3 o superior
pandas 2.0.1 o superior
openpyxl 3.1 o superior

Abrir el archivo excel con nombre 'MET001.xlsx' o crearlo. En caso de crear el archivo desde cero es necesario definir las columnas O (Serial) y P (Nro_Tarjeta) como texto para el correcto funcionamiento del programa.
Utilizar el siguiente SQL sobre la GXSWDTA.MET001 en ambos ambientes, copiar las filas de resultado y pegar sobre el archivo mencionado:

SELECT 
ME01MOVNUM AS BOLETA,
GE66RESCOD AS COD_RE,
GE70RESEXT AS COD_REEXT,
ME01CSHBCK AS CASHBACK,
GE52CPDPFI AS METODO,
GE44CODPRE AS PRESTACION,
ME01CUONRO AS CANT_CUOTA,
GE49TIPDIS AS DISPOSITIVO,
GE64PAGCOD AS COD_PAGO,
GE65TRACOD AS COD_TRAN,
ME01MARCOD AS MARCA, 
ME01PRMCOD AS PRODUCTO,
ME10TRDOPE AS FLAG_SIN_PIN,
IN02INVSER AS SERIAL,
ME01MARLOC AS LOCAL_INTERNACIONAL
ME01TARNRO AS NRO_TARJETA		
FROM GXSWDTA.MET001
WHERE (IN02INVSER = '9220194831' OR IN02INVSER ='9220349690' OR IN02INVSER = '9220425534')	/*SERIAL*/
AND ME01MOVFEC >= '20230510'				/*FECHA*/
ORDER BY ME01MOVNUM DESC;


Para Infonet Cobranzas añadir los siguientes filtros para la consulta en el ambiente de desarrollo:

WHERE GE65TRACOD = 72 /*TRN PAGOS-INFONET COBRANZAS*/
AND GE42SRVIDE = 'TIC' AND GE49TIPDIS = 'WEB' /*TIC - TRANSACCIONES INFONET COBRANZAS || WEB*/ 
AND ME01CCOCOD =136 AND ME01CCOSUC = 92
AND GE70RESEXT =''
AND ME01MOVFEC >= '20230510'				/*FECHA*/