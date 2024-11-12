import mysql.connector

class ConexionBD:
    def __init__(self):
        self.conn = None

    def conectar(self):
        if self.conn is None:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1597845",
                database="gestiontareas"
            )
        return self.conn

    def obtener_cursor(self):
        if self.conn is None:
            self.conectar()
        return self.conn.cursor()

    def cerrar(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None
