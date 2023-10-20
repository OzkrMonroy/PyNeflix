from tkinter import Frame, Label, Button


class SeriesItem:
    def __init__(self, root: Frame, series, row: int, col: int) -> None:
        self._series = series
        self._row = row
        self._col = col
        self._root = root
        self.__build_item()

    def __edit_series(self):
        print(f"series to edit {self._series['id']}")

    def __delete_series(self):
        print(f"series to delete {self._series['id']}")

    def __build_item(self):
        frame = Frame(self._root, width=200, height=200,
                      borderwidth=2, relief="groove")
        frame.grid(row=self._row, column=self._col,
                   padx=10, pady=10, sticky="we")

        card = Frame(frame)
        card.columnconfigure((0, 1), weight=1)
        card.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        card.pack(padx=10, pady=10)

        card_title = Label(card, text=self._series["name"])
        card_title.grid(row=0, column=0, sticky="ew", columnspan=2)

        card_duration_label = Label(card, text="Temporadas:")
        card_duration_label.grid(row=1, column=0, sticky="w")
        card_duration = Label(card, text=self._series["seasons"])
        card_duration.grid(row=1, column=1, sticky="e")

        card_duration_label = Label(card, text="Clasificación:")
        card_duration_label.grid(row=2, column=0, sticky="w")
        card_duration = Label(card, text=self._series["rating"])
        card_duration.grid(row=2, column=1, sticky="e")

        card_duration_label = Label(card, text="Género:")
        card_duration_label.grid(row=3, column=0, sticky="w")
        card_duration = Label(card, text=self._series["genre"])
        card_duration.grid(row=3, column=1, sticky="e")

        card_duration_label = Label(card, text="Fecha de lanzamiento:")
        card_duration_label.grid(row=3, column=0, sticky="w")
        card_duration = Label(card, text=self._series["release_date"])
        card_duration.grid(row=3, column=1, sticky="e")

        edit_button = Button(card, text="Editar", command=self.__edit_series)
        edit_button.grid(row=5, column=0, sticky="w", pady=8)
        delete_button = Button(card, text="Eliminar",
                               command=self.__delete_series)
        delete_button.grid(row=5, column=1, sticky="e", pady=8)
