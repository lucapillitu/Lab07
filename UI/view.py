from contextlib import nullcontext
import flet as ft
from UI.alert import AlertManager

'''    - Riceve i dati dal MODELLO e li presenta senza modificarli'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK
        self._dd = None
        self._dd2 = None
        self._list_view = None
        # Alert
        self.alert = AlertManager(page)
        # Controller
        self.controller = None


    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()

 #Crea e aggiunge gli elementi di UI alla pagina e la aggiorna

    def load_interface(self):
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Biblioteche di Torino", size=38, weight=ft.FontWeight.BOLD)
        # --- Sezione 2: Filtraggio ---
        self._dd = ft.Dropdown(label="Biblioteca" ,width=300,on_select=self.controller.add_biblioteca_selezionata)#senza le parentesi il metodo è allocato ma non eseguito
        self._dd2 = ft.Dropdown(label="Genere", width=300,on_select=self.controller.add_genere_selezionato)
        btn = ft.Button(content="Mostra libri",on_click=self.controller.mostra_libri)
        # Sezione 3: Libri
        self._list_view = ft.ListView(expand=True)
        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            ft.Row([self._dd, self._dd2],
                   alignment=ft.MainAxisAlignment.CENTER)
            ,
            ft.Divider(),

            ft.Row(controls=[btn], alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(),

            # Sezione 3: Libri
            self._list_view
        )
        self.controller.add_generi()
        self.controller.add_biblioteche()
        self.page.scroll = "adaptive"
        self.page.update()


