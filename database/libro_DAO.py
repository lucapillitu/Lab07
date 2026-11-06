from model.libro_DTO import Libro
import mysql.connector
from database.DB_connect import DBConnect

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_libri(self,genere, idbiblioteca):
        cnx = DBConnect.get_connection()
        if cnx is None:
            return None
        cursor = None

        try:
            # biblioteca_db = cnx.cursor()
            query = """SELECT l.id, l.titolo, l.autore, l.genere, l.anno_pubblicazione, l.id_biblioteca FROM libro l
                        WHERE l.id_biblioteca = COALESCE(%s, l.id_biblioteca) 
                        AND l.genere = COALESCE(%s, l.genere)"""

            cursor = cnx.cursor(dictionary=True)
            cursor.execute(query, (idbiblioteca,genere))

            result = []
            for row in cursor:
                l = Libro(int(row["id"]), row["titolo"], row["autore"], row["genere"],int(row["anno_pubblicazione"]), int(row["id_biblioteca"]))
                result.append(l)

            return result  # lista dizionari con i dati delle biblioteche dentro
        except mysql.connector.Error as err:
            print(err)
            return None

        finally:
            if cursor is not None:
                cursor.close()
            cnx.close()

    def get_generi(self):
        cnx = DBConnect.get_connection()
        if cnx is None:
            return None
        cursor = None

        try:
            # biblioteca_db = cnx.cursor()
            query = "SELECT distinct genere FROM libro l "
            cursor = cnx.cursor()
            cursor.execute(query)
            # Leggo tutto dal cursore in una variabile results
            # result = cursor.fetchall() --> returna tutte i record insieme in lista
            result = []
            for row in cursor:
                result.append(row[0])

            return result  # lista contenente i generi
        except mysql.connector.Error as err:
            print(err)
            return None

        finally:
            if cursor is not None:
                cursor.close()
            cnx.close()

