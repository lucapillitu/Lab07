from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):

    def get_biblioteche(self):
        biblioteca_db = []

        db = DBConnect()
        cnx = db.get_connection()

        if cnx is not None:
            #biblioteca_db = cnx.cursor()
            query  = "SELECT distinct id,nome from biblioteca b "