SELECT 
ME01MOVNUM AS Nro_Transaccion,
ME02STSMOV AS Estado_Movimiento,
GE66RESCOD AS Cod_Respuesta,
GE70RESEXT AS Cod_Respuesta_Extendida,
GE44CODPRE AS Cod_Prestacion,
GE52CPDPFI AS Cod_Prefijo,
ME01MOVIMP AS Importe,
ME01CUONRO AS Nro_Cuota,
ME01CSHBCK AS CashBack,
GE64PAGCOD AS Cod_Medio_Pago,
ME01REOTTR AS Nro_Trans_relacionada,
IN01MODCOD AS Codigo_de_Modelo,
IN02INVSER AS Nro_Serie_del_POS,
GE49TIPDIS AS Cod_Tipo_Dispositivo,
ME01VRSEQP AS Version_del_Software_en_el_Equipo,
ME01CCOCOD AS Comercio,
ME01CCOSUC AS Sucursal,
GE65TRACOD AS Cod_Transaccion,
ME10TRDOPE AS Codigo_Operacion,
ME01MONCOD AS Moneda,
GE50ORICAL AS Id_Origen,
ME01MOVPLA AS Plan,
ME01TARNRO AS Nro_Tarjeta,
GE42SRVIDE AS Id_Servicio,
ME01MARCOD AS Marca,
ME01PRMCOD AS Producto_de_la_Marca,
ME01MOVFHO AS Fecha_y_Hora_Transaccion,
ME01MOVFEC AS Fecha_Transaccion,
ME01MARLOC AS Marca_Local_Internacional,
ME01ENTEMI AS Entidad_Emisora,
ME01TARENM AS Tarjeta_Enmascarado,
GE33BINNRO AS Nro_de_Bin,
GE33CNTDIG AS Cantidad_de_Digitos,
ME01CTANRO AS Cuenta_Nro 
FROM GXSWDTA.MET001 
WHERE IN02INVSER IN ('9220425534', 'F2002022B200667')
AND ME01MOVFEC  >= '20230710'
