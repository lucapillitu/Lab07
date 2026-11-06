import mysql.connector
from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_biblioteche(self):
        cnx = DBConnect.get_connection()
        if cnx is None:
            return None
        cursor = None

        try:
            #biblioteca_db = cnx.cursor()
            query  = "SELECT distinct id,nome,indirizzo from biblioteca b "
            cursor = cnx.cursor(dictionary=True)
            cursor.execute(query)
            # Leggo tutto dal cursore in una variabile results
            # result = cursor.fetchall() --> returna tutte i record insieme in lista
            result = []
            for row in cursor:
                 b = Biblioteca(row["id"], row["nome"], row["indirizzo"])
                 result.append(b)

            return result#lista dizionari con i dati delle biblioteche dentro
        except mysql.connector.Error as err:
                print(err)
                return None

        finally:
            if cursor is not None:
                cursor.close()
            cnx.close()
