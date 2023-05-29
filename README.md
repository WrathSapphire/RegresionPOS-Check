##########################################################################################################
# DOCUMENTACION: Automatizacion de consultas de casos de prueba Test de Regresión en POS de BANCARD S.A. #
# QA: Javier Bernal                                                                                      #
##########################################################################################################

Requisitos:
Python 3.11 o superior
numpy 1.24.3 o superior
pandas 2.0.1 o superior

Utilizar el siguiente SQL sobre la GXSWDTA.MET001 y exportarlo a un archivo excel con nombre 'MET001.xlsx':

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
--ME01TARNRO AS NRO_TARJETA		*/Para el módulo DEBITO/CREDITO Extranjero se evaluará por nro de tarjeta de una UENO/*
FROM GXSWDTA.MET001