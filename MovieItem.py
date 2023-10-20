from tkinter import Frame, Label, Button, messagebox
from MoviesSeriesController import MoviesSeriesController


class MovieItem:
    controller = MoviesSeriesController()
    _callback = None

    def __init__(self, root: Frame, movie, row: int, col: int, callback) -> None:
        self._movie = movie
        self._row = row
        self._col = col
        self._root = root
        self._callback = callback
        self.__build_item()

    def __edit_movie(self):
        print("To edit", self._movie["id"])

    def __delete_movie(self, card_reference: Frame):
        response = messagebox.askyesno(
            "Eliminar", f"¿Esta seguro que quiere eliminar la película: {self._movie['name']}?")
        if (response):
            self.controller.delete_movie(self._movie)
            self._callback(card_reference)

    def __build_item(self):

        frame = Frame(self._root, width=200, height=200,
                      borderwidth=2, relief="groove")
        frame.grid(row=self._row, column=self._col,
                   padx=10, pady=10, sticky="we")

        card = Frame(frame)
        card.columnconfigure((0, 1), weight=1)
        card.rowconfigure((0, 1, 2, 3, 4), weight=1)
        # card.config(bg="white")
        card.pack(padx=10, pady=10)

        card_title = Label(card, text=self._movie["name"])
        card_title.grid(row=0, column=0, sticky="ew", columnspan=2)

        card_duration_label = Label(card, text="Duración:")
        card_duration_label.grid(row=1, column=0, sticky="w")
        card_duration = Label(card, text=self._movie["duration"])
        card_duration.grid(row=1, column=1, sticky="e")

        card_duration_label = Label(card, text="Clasificación:")
        card_duration_label.grid(row=2, column=0, sticky="w")
        card_duration = Label(card, text=self._movie["rating"])
        card_duration.grid(row=2, column=1, sticky="e")

        card_duration_label = Label(card, text="Género:")
        card_duration_label.grid(row=3, column=0, sticky="w")
        card_duration = Label(card, text=self._movie["genre"])
        card_duration.grid(row=3, column=1, sticky="e")

        edit_button = Button(card, text="Editar", command=self.__edit_movie)
        edit_button.grid(row=4, column=0, sticky="w", pady=8)
        delete_button = Button(card, text="Eliminar",
                               command=lambda: self.__delete_movie(frame))
        delete_button.grid(row=4, column=1, sticky="e", pady=8)
