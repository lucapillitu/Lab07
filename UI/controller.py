import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view
        self.biblioteche = []
        self.libri = []

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def add_generi(self):
        generi = self._model.get_generi()
        if generi is None :
            return None

        self._view._dd2.options.append(ft.dropdown.Option("Nessun Genere"))
        for g in generi:
            self._view._dd2.options.append(ft.dropdown.Option(g))
        self._view.update()

    def add_biblioteche(self):
        self.biblioteche = self._model.get_biblioteche()
        if self.biblioteche is None:
            return None

        self._view._dd.options.append(ft.dropdown.Option("Nessuna Biblioteca"))
        for b in self.biblioteche:
            self._view._dd.options.append(ft.dropdown.Option(b.nome))
        self._view.update()


    # CALLBACKS DROPDOWN :  dopo che seleziono i dropdown o meno deve ritornarmi un dato valore per poter fafre le query di ricerca
    def add_genere_selezionato(self,e):
        self.genere_selezionato = self._view._dd2.value
        if self.genere_selezionato == "Nessun Genere":
            self.genere_selezionato = None


    def add_biblioteca_selezionata(self,e):

        if self._view._dd.value == "Nessuna Biblioteca":
            self.biblioteca_selezionata = None
        else :
            bib = self.biblioteche#prendo il dizionario di bibliteche per trovare il rispettivo id
            for b in bib:
                if b.nome == self._view._dd.value:
                    self.biblioteca_selezionata = b.id



    # AZIONE: MOSTRA LIBRI
    def mostra_libri(self, e):
        self.libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)

        # svuoto la lista mostrata prima
        self._view._list_view.controls.clear()

        if self.libri is None:
            self._view.show_alert("❌ Errore nella lettura dei libri dal database")
            return

        if len(self.libri) == 0:
            self._view.show_alert("ℹ️ Nessun libro trovato con i filtri selezionati")
            self._view.update()
            return

        for libro in self.libri:
            self._view._list_view.controls.append(ft.Text(str(libro)))

        self._view.update()


