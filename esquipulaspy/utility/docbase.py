# -*- coding: utf-8 -*-
'''
Created on 16/08/2010

@author: Andrés Reyes Monge
'''

from PyQt4.QtCore import QAbstractTableModel, QDateTime


class DocumentBase( QAbstractTableModel ):

    """
    Esta se convertira en un futuro en la clase base para los nuevos documentos
    idealmente aca irian todas las propiedades que de todos modos todos los
    documentos tienen Eg: exchangeRate, exchangeRateId, observaciones

    ademas de algunos metodos como validLines
    """
    __documentType = NotImplementedError()

    def __init__( self ):
        super( DocumentBase, self ).__init__()



        self.printedDocumentNumber = ""
        """
        @ivar:El numero de documento impreso del documento
        @type:string
        """

        self.datetime = QDateTime.currentDateTime()
        u"""
        @ivar:La fecha de la liquidación
        @type:QDateTime
        """



        self.observations = ""
        """
        @ivar:Las observaciones de este documento
        @type:string
        """

        self.__validError = ""
        """
        @ivar: Si existe algún error de validación aca es que se muestra
        @type:string
        """

    @property
    def validError( self ):
        return self.__validError

    @property
    def validLines( self ):
        """
        El total de lineas con la propiedad valid = True
        @rtype: int
        """
        return len( [line for line in self.lines if line.valid] )

    @property
    def valid( self ):
        raise NotImplementedError( "El metodo valid deberia de ser"\
                                  + " implementado en todos los documentos" )

    def save( self ):
        raise NotImplementedError()

class LineaBase( object ):
    u"""
    Esta se convertira en un futuro en la clase base para las nuevas lineas,
    con suerte se podran pasar aca muchos metodos genericos
    """
    @property
    def valid( self ):
        """
        Es esta linea valida
        @rtype: bool
        """
        raise NotImplementedError( "No se ha implementado la propiedad Valid" )

    def save( self, iddocumento, nlinea ):
        """
        Este metodo guarda la linea en la base de datos
        @param iddocumento: el id del documento al que esta enlazada la linea
        @rtype: bool
        @return: Si se pudo o no guardar el documento
        """
        raise NotImplementedError( "No se ha implementado el metodo save" )
