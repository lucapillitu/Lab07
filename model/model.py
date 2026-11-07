from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()
        self.libri = []
        self.biblioteche = []

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        pass

    def get_generi(self):
        generi = self._libro_dao.get_generi()  # chiamata unica
        if generi is not None:
            return generi
        else:
            return None




    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        bib = self._biblioteca_dao.get_biblioteche()
        if bib is not None:

            return bib
        else:
            return None
