from tkinter import Label, Frame, Button, Entry, messagebox
from tkinter.font import Font
from MoviesSeriesController import MoviesSeriesController


class AddElement:
    def __init__(self, root: Frame, navigation_callback) -> None:
        self._root = root
        self._navigation_callback = navigation_callback
        self.__build_screen()

    def __build_screen(self):
        add_element_frame = Frame(
            self._root, padx=150, pady=20, width=500)
        add_element_frame.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
        add_element_frame.columnconfigure((0, 1), weight=1)
        add_element_frame.pack(fill="both")

        label_font = Font(family="Arial", size=20, weight="bold")
        movie_section_title = Label(
            add_element_frame, text="Agregar nuevo", font=label_font, anchor="w")
        movie_section_title.grid(
            row=0, column=0, padx=10, pady=10, sticky="we")

        options_font = Font(family="Arial", size=16)

        name_label = Label(add_element_frame,
                           text="Nombre: ", font=options_font, anchor="center")
        name_label.grid(row=1, column=0, padx=10, pady=20, sticky="we")
        name_entry = Entry(add_element_frame,
                           font=options_font, borderwidth=2, relief="groove")
        name_entry.grid(row=1, column=1, sticky="we", pady=20)

        duration_label = Label(add_element_frame,
                               text="Duración: ", font=options_font, anchor="center")
        duration_label.grid(row=2, column=0, padx=10, pady=20, sticky="we")
        duration_entry = Entry(add_element_frame,
                               font=options_font, borderwidth=2, relief="groove")
        duration_entry.grid(row=2, column=1, sticky="we", pady=20)

        rating_label = Label(add_element_frame,
                             text="Rating: ", font=options_font, anchor="center")
        rating_label.grid(row=3, column=0, padx=10, pady=20, sticky="we")
        rating_entry = Entry(add_element_frame,
                             font=options_font, borderwidth=2, relief="groove")
        rating_entry.grid(row=3, column=1, sticky="we", pady=20)

        genre_label = Label(add_element_frame,
                            text="Género: ", font=options_font, anchor="center")
        genre_label.grid(row=4, column=0, padx=10, pady=20, sticky="we")
        genre_entry = Entry(add_element_frame,
                            font=options_font, borderwidth=2, relief="groove")
        genre_entry.grid(row=4, column=1, sticky="we", pady=20)

        cancel_button = Button(
            add_element_frame, text="Cancelar", command=self._navigation_callback)
        cancel_button.grid(row=5, column=0)
        save_button = Button(add_element_frame, text="Guardar", command=lambda: self.save_element(
            name_entry, duration_entry, rating_entry, genre_entry))
        save_button.grid(row=5, column=1)

    def save_element(self, name_entry: Entry, duration_entry: Entry, rating_entry: Entry, genre_entry: Entry):
        name, duration, rating, genre = name_entry.get(
        ), duration_entry.get(), rating_entry.get(), genre_entry.get()

        if (not bool(name) or not bool(duration) or not bool(rating) or not bool(genre)):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        controller = MoviesSeriesController()
        controller.save_movie_series(
            [name, "pelicula", duration, rating, genre])
        self._navigation_callback()
