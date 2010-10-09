# -*- coding: utf-8 -*-
'''
Created on 06/07/2010

@author: Luis Carlos Mejia
'''

IDCAJA = 2
ACCESOCAJA = ['caja']

IDCONTABILIDAD = 3
ACCESOCONTABILIDAD = ['contabilidad']

IDINVENTARIO = 4
ACCESOINVENTARIO =['inventario','contabilidad','kardex']

#conceptos
IDCONCEPTODEPOSITO = 0


# constantes de tipos de documento
IDANULACION = 2
IDFACTURA = 5
IDLIQUIDACION = 7
#IDDEVOLUCION = 14
IDND = 11
IDCHEQUE = 12
IDDEPOSITO = 13
IDNOTACREDITO=14
IDNC = 10
IDRECIBO = 18
IDRETENCION = 19
IDENTRADALOCAL = 21
IDAPERTURA = 22
IDARQUEO = 23
IDAJUSTECONTABLE = 24
IDCONCILIACION = 25
IDERROR = 26
IDKARDEX = 27
IDCIERREMENSUAL = 28
IDCIERREANUAL = 29
IDPAGO = 30

IDAJUSTEBODEGA = 30

#TIPOS DE PERSONA
CLIENTE = 1
PROVEEDOR = 2
VENDEDOR = 3
AUTOR = 4
SUPERVISOR = 5
CONTADOR = 6



#TIPOS DE ESTADOS DE DOCUMENTOS
CONFIRMADO=1
ANULADO = 2
PENDIENTE = 3
INCOMPLETO = 4
ANULACIONPENDIENTE = 5

#TIPOS COSTO
IVA = 1
ISC = 2
DAI = 3
SPE = 4
TSIM = 5
ISO = 6
COMISION = 7
RETENCIONFUENTE = 8
RETENCIONPROFESIONALES = 9


#TIPOS DE MONEDA
IDCORDOBAS=1
IDDOLARES=2

#TIPOS DE PAGO
IDPAGOEFECTIVO = 1
IDPAGOCHEQUE = 2
IDPAGODEPOSITO = 3
IDPAGOTRANSFERENCIA = 4
IDPAGOTARJETA = 5

#ACCIONES
ACCCOMPRA = 1
ACCABASTECE = 2
ACCVENDE = 3
ACCCREA = 4
ACCAUTORIZA = 5
ACCCONTABILIZA = 6


#ACCFACTURA = 6
# CUENTAS PARA CIERRE MENSUAL
INGRESOSXVENTA=170
OTROSINGRESOS=175
COSTOSGASTOSOPERACIONES=181
GASTOSXVENTAS=183
GASTOS=249
GASTOSFINANCIEROS=314
PRODUCTOSFINANCIEROS=323
OTROSGASTOS=327