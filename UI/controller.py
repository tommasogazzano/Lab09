import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_hello(self, e):
        name = self._view.txt_distanza.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()


    def handle_analisi(self, e):
        limite = self._view.txt_distanza.value
        if limite is None or limite == "":
            self._view.create_alert("Inserire un valore di distanza valido")
        self._model._limite = limite
        self._model.buildGraph()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo Correttamente creato!!"))
        self._view.txt_result.controls.append(ft.Text(f"il grafo ha {self._model.getNumNodi()} nodi"))
        self._view.txt_result.controls.append(ft.Text(f"il grafo ha {self._model.getNumArchi()} archi"))
        self._view.txt_result.controls.append(ft.Text(f"{self._model.stampaVoli()}"))

        self._view.update_page()
