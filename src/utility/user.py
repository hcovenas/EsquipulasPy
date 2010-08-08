# -*- coding: utf-8 -*-
"""
Modulo en el que se maneja la logica de usuarios
"""
import hashlib

from PyQt4.QtSql import QSqlQuery, QSqlDatabase
from PyQt4.QtCore import QObject, SIGNAL, SLOT, Qt 
from PyQt4.QtGui import QDialog,  qApp, QDesktopWidget, QPixmap

from ui import res_rc
from ui.Ui_user import Ui_dlgUserLogin

UID, FULLNAME, ROLE = range( 3 )

class dlgUserLogin( QDialog, Ui_dlgUserLogin ):
    """
    Dialogo utilizado para pedir valores de usuario y contraseña
    """
    def __init__( self, parent = None ):
        super( dlgUserLogin, self ).__init__( parent )

        self.setupUi(self)

        self.setWindowTitle( qApp.applicationName() )
        self.txtUser.setText('root')
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        dw = QDesktopWidget()
        geometry = dw.screenGeometry()
        
        self.setGeometry( (geometry.width() -519) / 2, (geometry.height() -311)  / 2  , 519, 311)
        
        pixmap = QPixmap(":/images/res/passwd-bg.png");
        self.setMask(pixmap.mask());


        QObject.connect( self.buttonbox, SIGNAL( "accepted()" ), self, SLOT( "accept()" ) )
        QObject.connect( self.buttonbox, SIGNAL( "rejected()" ), self, SLOT( "reject()" ) )


class User:
    secret = '7/46u23opA)P231popas;asdf3289AOP23'
    u"""
    @cvar: El hash usado en esta aplicación para los usuarios
    @type: string  
    """
    def __init__( self, user, password ):
        self.__user = user
        """
        @ivar: el nombre de usuario
        @type:string
        """
        self.__password = password
        u"""
        @ivar: La contraseña
        @type:string
        """
        self.__roles = []
        """
        @ivar: La lista de permisos de un usuario
        @type: string[]
        """
        self.__valid = False
        """
        @ivar: si el usuario es valido o no
        @type: bool 
        """
        self.__fullname = ""
        """
        @ivar:El nombre completo de este usuario
        @type: string 
        """
        self.__uid = 0
        """
        @ivar: El id de este usuario
        @type: int
        """
        self.error = ""
        """
        @ivar:Posibles errores
        @type:string
        """
        self.db = QSqlDatabase.database()
        try:
            if not self.db.open():
                raise UserWarning( u'Existen problemas de conectividad con la base de datos' )
            else:
                query = QSqlQuery()
                if not query.prepare( """
                SELECT 
                    u.idusuario AS uid, 
                    p.nombre, 
                    r.nombre as rol 
                FROM usuarios u
                JOIN personas p ON p.idpersona = u.idusuario
                JOIN usuarios_has_roles ur ON u.idusuario = ur.idusuario
                JOIN roles r ON r.idrol = ur.idrol
                WHERE u.estado = 1
                AND u.username LIKE BINARY :user
                AND u.password LIKE BINARY SHA1(:password)
                """ ):
                    raise UserWarning( "No se pudo preparar la consulta para validar el usuario" )
                query.bindValue( ":user", self.user )
                query.bindValue( ":password", self.password + self.secret )

                if not query.exec_():
                    raise UserWarning( "La consulta no se pudo ejecutar" )

                if query.size() == 0:
                    raise UserWarning( "El usuario no es valido" )
                else:
                    while query.next():
                        self.__valid = True
                        self.__uid = query.value( UID ).toInt()[0]
                        self.__fullname = query.value( FULLNAME ).toString()
                        self.__roles.append( query.value( ROLE ).toString() )
        except UserWarning as inst:
            self.error = str( inst )
        except Exception as e:
            print e
        finally:
            if self.db.isOpen():
                self.db.close()
    @property
    def user( self ):
        """
        El nombre de usuario que se utilizo para validar el usuario
        @rtype: string
        """
        return self.__user

    @property
    def password( self ):
        """
        La contraseña que se utilizo para validar el usuario
        @rtype: string
        """
        return self.__password

    @property
    def valid( self ):
        """
        Si el usuario es valido o no
        @rtype: bool
        """
        return self.__valid

    @property
    def hash( self ):
        return  hashlib.sha1( hashlib.sha1( self.password + self.secret ).hexdigest() + self.secret ).hexdigest() if self.valid else ""

    @property
    def roles( self ):
        """
        La lista de roles del Usuario
        @rtype: list
        """
        return self.__roles if self.valid else []

    def hasRole( self, role ):
        """
        Esta funcion comprueba si  un usuario tiene determinado permiso
        @param role: este parametro es el rol que se quiere comprobar
        @rtype: bool 
        """
        if self.valid:
            if 'root' in self.__roles:
                return True
            else:
                return role in self.__roles
        return False

    @property
    def fullname( self ):
        """
        El nombre completo del usuario según lo definido en la base de datos
        @rtype: string
        """
        return self.__fullname
    @property
    def uid( self ):
        """
        El id del usuario en la base de datos
        @rtype: int
        """
        return self.__uid
if __name__=="__main__":
    import sys
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *

    app = QApplication(sys.argv)
    app.setStyleSheet("""
    dlgUserLogin{
        background: #2B579F;
    }
    """)
    dlg = dlgUserLogin()


    QObject.connect(dlg, SIGNAL("accepted()"), sys.exit)
    QObject.connect(dlg, SIGNAL("rejected()"), sys.exit)
    
    dlg.exec_()

    app.exec_()