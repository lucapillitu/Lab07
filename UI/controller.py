import flet as ft

import model
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
            self._view._dd2.options.append(g)

        self._view.update()



    # CALLBACKS DROPDOWN
    # TODO

    # AZIONE: MOSTRA LIBRI
    # TODO
