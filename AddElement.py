from tkinter import Label, Frame, Button, Entry, messagebox
from tkinter.font import Font
from MoviesSeriesController import MoviesSeriesController


class AddElement:
    controller = MoviesSeriesController()

    def __init__(self, root: Frame, navigation_callback) -> None:
        self._root = root
        self._navigation_callback = navigation_callback
        self._is_to_update = False
        self._element_to_update = {}
        self._element = ""
        self.__build_screen()

    def __build_screen(self):
        self._element = self.controller.get_element_type()
        self._element_to_update = self.controller.get_element_to_update()
        self._is_to_update = self.controller.get_is_to_update()

        row_quantity = (0, 1, 2, 3, 4, 5, 6, 7, 8) if self._element == "serie" else (
            0, 1, 2, 3, 4, 5, 6, 7)
        duration_season_text = "Temporadas:" if self._element == "serie" else "Duración:"
        buttons_row = 6 if self._element == "serie" else 5

        add_element_frame = Frame(
            self._root, padx=150, pady=20, width=500)
        add_element_frame.rowconfigure(row_quantity, weight=1)
        add_element_frame.columnconfigure((0, 1), weight=1)
        add_element_frame.pack(fill="both")

        window_title = f"Editar {self._element}" if self._is_to_update else f"Agregar nueva {self._element}"
        label_font = Font(family="Arial", size=20, weight="bold")

        movie_section_title = Label(
            add_element_frame, text=window_title, font=label_font, anchor="w")
        movie_section_title.grid(
            row=0, column=0, padx=10, pady=10, sticky="we")

        options_font = Font(family="Arial", size=16)

        name_label = Label(add_element_frame,
                           text="Nombre: ", font=options_font, anchor="w")
        name_label.grid(row=1, column=0, padx=10, pady=20, sticky="we")
        name_entry = Entry(add_element_frame,
                           font=options_font, borderwidth=2, relief="groove")
        name_entry.grid(row=1, column=1, sticky="we", pady=20)

        duration_season_label = Label(add_element_frame,
                                      text=duration_season_text, font=options_font, anchor="w")
        duration_season_label.grid(
            row=2, column=0, padx=10, pady=20, sticky="we")
        duration_season_entry = Entry(add_element_frame,
                                      font=options_font, borderwidth=2, relief="groove")
        duration_season_entry.grid(row=2, column=1, sticky="we", pady=20)

        rating_label = Label(add_element_frame,
                             text="Clasificación: ", font=options_font, anchor="w")
        rating_label.grid(row=3, column=0, padx=10, pady=20, sticky="we")
        rating_entry = Entry(add_element_frame,
                             font=options_font, borderwidth=2, relief="groove")
        rating_entry.grid(row=3, column=1, sticky="we", pady=20)

        genre_label = Label(add_element_frame,
                            text="Género: ", font=options_font, anchor="w")
        genre_label.grid(row=4, column=0, padx=10, pady=20, sticky="we")
        genre_entry = Entry(add_element_frame,
                            font=options_font, borderwidth=2, relief="groove")
        genre_entry.grid(row=4, column=1, sticky="we", pady=20)

        release_label = Label(add_element_frame,
                              text="Fecha de lanzamiento: ", font=options_font, anchor="w")
        release_entry = Entry(add_element_frame,
                              font=options_font, borderwidth=2, relief="groove")

        if (self._element == "serie"):
            release_label.grid(row=5, column=0, padx=10, pady=20, sticky="we")
            release_entry.grid(row=5, column=1, sticky="we", pady=20)
        if (self._is_to_update):
            self.fill_fields(name_entry, duration_season_entry,
                             rating_entry, genre_entry, release_entry)

        cancel_button = Button(
            add_element_frame, text="Cancelar", command=self._navigation_callback)
        cancel_button.grid(row=buttons_row, column=0)
        save_button = Button(add_element_frame, text="Guardar", command=lambda: self.save_element(
            name_entry, duration_season_entry, rating_entry, genre_entry, release_entry))
        save_button.grid(row=buttons_row, column=1)

    def fill_fields(self, name_entry: Entry, duration_seasons_entry: Entry, rating_entry: Entry, genre_entry: Entry, release_entry: Entry):
        name_entry.insert(0, self._element_to_update.name)
        rating_entry.insert(0, self._element_to_update.rating)
        genre_entry.insert(0, self._element_to_update.genre)
        duration_seasons_entry.insert(
            0, self._element_to_update.duration)

        if (self._element == "serie"):
            release_entry.insert(0, self._element_to_update.release_date)

    def save_element(self, name_entry: Entry, duration_seasons_entry: Entry, rating_entry: Entry, genre_entry: Entry, release_entry: Entry):
        if (self._element == "serie"):
            self.save_serie(name_entry, duration_seasons_entry,
                            rating_entry, genre_entry, release_entry)
        else:
            self.save_movie(name_entry, duration_seasons_entry,
                            rating_entry, genre_entry)

    def save_movie(self, name_entry: Entry, duration_entry: Entry, rating_entry: Entry, genre_entry: Entry):
        name, duration, rating, genre = name_entry.get(
        ), duration_entry.get(), rating_entry.get(), genre_entry.get()

        if (not bool(name) or not bool(duration) or not bool(rating) or not bool(genre)):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        if (self._is_to_update):
            self.controller.update_movie(
                [self._element_to_update.id, name, duration, rating, genre])
        else:
            self.controller.save_movie_series(
                [name, "pelicula", duration, rating, genre])

        self._navigation_callback()

    def save_serie(self, name_entry: Entry, seasons_entry: Entry, rating_entry: Entry, genre_entry: Entry, release_entry: Entry):
        name, season, rating, genre, release = name_entry.get(
        ), seasons_entry.get(), rating_entry.get(), genre_entry.get(), release_entry.get()

        if (not bool(name) or not bool(season) or not bool(rating) or not bool(genre) or not bool(release)):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        if (self._is_to_update):
            self.controller.update_series(
                [self._element_to_update.id, name, season, rating, genre, release])
        else:
            self.controller.save_movie_series(
                [name, "serie", season, rating, genre, release])

        self._navigation_callback()
